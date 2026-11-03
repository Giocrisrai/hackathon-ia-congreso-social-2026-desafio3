"""Conexión con la IA: varios proveedores compatibles con OpenAI, salida JSON estructurada,
cambio automático de proveedor y modo demo.
Este módulo NO debe ser modificado por los equipos.

Secrets (formato recomendado, igual al Desafío 2):
    [ia]
    orden = ["groq", "mistral"]          # se prueban en este orden
    [ia.groq]
    api_key = "gsk_..."
    modelos = ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
    [ia.mistral]
    api_key = "..."
    modelos = ["mistral-small-latest", "ministral-8b-latest"]

Un proveedor que no esté en PROVEEDORES necesita además  url = "https://.../v1".
Formato anterior (sigue funcionando): OPENAI_API_KEY, MODELO y, opcional, OPENAI_BASE_URL.
"""

import json
import os
import time
from pathlib import Path
from threading import Lock

import streamlit as st
from openai import (OpenAI, RateLimitError, APIConnectionError, APITimeoutError,
                    InternalServerError, AuthenticationError, PermissionDeniedError,
                    NotFoundError, BadRequestError)

CARPETA_DATOS = Path(__file__).resolve().parent.parent / "datos"

PROVEEDORES = {
    "groq":       "https://api.groq.com/openai/v1",
    "mistral":    "https://api.mistral.ai/v1",
    "openai":     "https://api.openai.com/v1",
    "gemini":     "https://generativelanguage.googleapis.com/v1beta/openai/",
    "openrouter": "https://openrouter.ai/api/v1",
    "cerebras":   "https://api.cerebras.ai/v1",
    "together":   "https://api.together.xyz/v1",
    "deepseek":   "https://api.deepseek.com",
}
PAUSA_SATURADO, PAUSA_INVALIDO = 45, 600  # segundos que se salta un modelo saturado (429) o con clave/modelo inválido
TIMEOUT = 40
TEMPERATURA = 0.2  # baja: la misma consulta debe dar respuestas consistentes
RAZONAMIENTO = "low"  # esfuerzo de razonamiento de los modelos gpt-oss


def _secreto(clave, defecto=None):
    try:
        return st.secrets.get(clave, defecto)
    except Exception:  # sin archivo de secrets
        return defecto


def cadena() -> list[dict]:
    """Lista ordenada de (proveedor, modelo, clave, url) que se van a probar."""
    ia = _secreto("ia")
    eslabones = []
    if ia:
        for p in ia.get("orden", []):
            bloque = ia.get(p, {})
            clave = str(bloque.get("api_key", "") or "")
            url = bloque.get("url") or PROVEEDORES.get(p, "")
            modelos = list(bloque.get("modelos") or [m for m in (bloque.get("modelo"),) if m])
            if clave and url:
                eslabones += [{"proveedor": p, "modelo": str(m), "clave": clave, "url": url} for m in modelos]
    elif _secreto("OPENAI_API_KEY") and _secreto("MODELO"):  # formato anterior
        url = _secreto("OPENAI_BASE_URL") or os.environ.get("OPENAI_BASE_URL") or PROVEEDORES["openai"]
        prov = next((p for p, u in PROVEEDORES.items() if u.rstrip("/") == url.rstrip("/")), "openai")
        eslabones = [{"proveedor": prov, "modelo": str(_secreto("MODELO")),
                      "clave": str(_secreto("OPENAI_API_KEY")), "url": url}]
    return eslabones


@st.cache_resource
def _cliente(url: str, clave: str) -> OpenAI:
    # max_retries=0: los reintentos y el cambio de proveedor los controlamos nosotros
    return OpenAI(api_key=clave, base_url=url, timeout=TIMEOUT, max_retries=0)


@st.cache_resource
def _pausas():
    """Modelos en pausa, compartido entre todas las sesiones de la app."""
    return {"hasta": {}, "lock": Lock()}


def _id(e):
    return (e["proveedor"], e["modelo"], hash(e["clave"]) % 10**8)


def _pausar(e, segundos):
    p = _pausas()
    with p["lock"]:
        p["hasta"][_id(e)] = time.time() + segundos


def _pausado(e) -> bool:
    return _pausas()["hasta"].get(_id(e), 0) > time.time()


def describir() -> list[str]:
    """Texto para la barra lateral: la cadena en uso, con ⏸️ en los modelos en pausa."""
    return [f"{'⏸️ ' if _pausado(e) else ''}{e['proveedor']} · {e['modelo']}" for e in cadena()]


@st.cache_data
def _demo(variante: str) -> dict:
    ruta = CARPETA_DATOS / f"demo_{variante.lower()}.json"
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except Exception:
        return {}


def respuesta_demo(variante: str, clave: str, respaldo: dict) -> dict:
    """Busca una respuesta precalculada; si no existe, usa el respaldo genérico.
    Devuelve una copia para no modificar los datos guardados."""
    return json.loads(json.dumps(_demo(variante).get(clave, respaldo)))


def _extraer_json(texto: str) -> dict:
    texto = (texto or "").strip()
    try:
        return json.loads(texto)
    except Exception:
        ini, fin = texto.find("{"), texto.rfind("}")
        if ini >= 0 and fin > ini:
            return json.loads(texto[ini:fin + 1])
        raise ValueError("la respuesta no trae JSON")


def _llamar(e, sistema, usuario, esquema, nombre_esquema, razonamiento=None) -> dict:
    extra = {"reasoning_effort": razonamiento or RAZONAMIENTO} if "gpt-oss" in e["modelo"] else {}
    mensajes = [{"role": "system", "content": sistema}, {"role": "user", "content": usuario}]
    formato = {"type": "json_schema", "json_schema": {"name": nombre_esquema, "schema": esquema, "strict": True}}
    try:
        r = _cliente(e["url"], e["clave"]).chat.completions.create(
            model=e["modelo"], messages=mensajes, response_format=formato, temperature=TEMPERATURA,
            extra_body=extra or None)
    except BadRequestError as err:
        if "response_format" not in str(err) and "schema" not in str(err).lower():
            raise
        # Proveedor sin salida estructurada estricta: se pide JSON y se le entrega el esquema en el prompt
        mensajes[0]["content"] += ("\n\nResponde SOLO con un objeto JSON válido que cumpla este esquema:\n"
                                   + json.dumps(esquema, ensure_ascii=False))
        r = _cliente(e["url"], e["clave"]).chat.completions.create(
            model=e["modelo"], messages=mensajes, response_format={"type": "json_object"},
            temperature=TEMPERATURA, extra_body=extra or None)
    datos = _extraer_json(r.choices[0].message.content)
    faltan = [c for c in esquema.get("required", []) if c not in datos]
    if faltan:
        raise ValueError(f"faltan campos en la respuesta: {faltan}")
    return datos


def consultar(sistema: str, usuario: str, esquema: dict, nombre_esquema: str,
              variante: str, clave_demo: str, respaldo_demo: dict, razonamiento: str | None = None) -> tuple[dict, str]:
    """Devuelve SIEMPRE (respuesta, modo). modo = 'real' o 'demo'.
    razonamiento: esfuerzo de los modelos gpt-oss ("low" o "medium"); más alto sigue mejor el tono pero gasta más."""

    # Modo demo forzado desde los secrets (contingencia manual)
    if str(_secreto("MODO_DEMO", "no")).lower() == "si":
        return respuesta_demo(variante, clave_demo, respaldo_demo), "demo"

    eslabones = cadena()
    if not eslabones:
        st.error("Falta configurar la IA en los secrets (bloque [ia] o OPENAI_API_KEY y MODELO).")
        return respuesta_demo(variante, clave_demo, respaldo_demo), "demo"

    errores = []
    # Primero los modelos disponibles; los pausados solo si no queda otro
    for e in [x for x in eslabones if not _pausado(x)] or eslabones:
        t0 = time.time()
        try:
            datos = _llamar(e, sistema, usuario, esquema, nombre_esquema, razonamiento)
            seg = round(time.time() - t0, 1)
            st.session_state["ia_ultimo"] = f"{e['proveedor']} · {e['modelo']}"
            st.caption(f"🤖 Respondió {e['proveedor']} · {e['modelo'].split('/')[-1]} · {seg} s")
            return datos, "real"
        except RateLimitError as err:
            _pausar(e, PAUSA_SATURADO)
            errores.append(f"{e['proveedor']}/{e['modelo']}: saturado (429) {str(err)[:160]}")
        except (AuthenticationError, PermissionDeniedError, NotFoundError) as err:
            _pausar(e, PAUSA_INVALIDO)
            errores.append(f"{e['proveedor']}/{e['modelo']}: clave o modelo inválido · {type(err).__name__} {str(err)[:160]}")
        except (APIConnectionError, APITimeoutError, InternalServerError) as err:
            errores.append(f"{e['proveedor']}/{e['modelo']}: no responde · {type(err).__name__}")
        except Exception as err:
            errores.append(f"{e['proveedor']}/{e['modelo']}: {type(err).__name__} {str(err)[:160]}")
        print(f"[llm] {errores[-1]}", flush=True)

    st.session_state["ia_ultimo"] = "demostración"
    st.warning("El servicio de IA no respondió. Se muestra una respuesta de demostración.")
    equipo = str(st.session_state.get("equipo", ""))
    if equipo == "T00" or equipo.startswith("M"):  # diagnóstico solo para tutores y mentores
        st.code("\n".join(errores))
    return respuesta_demo(variante, clave_demo, respaldo_demo), "demo"


def consultar_silencioso(sistema: str, usuario: str, esquema: dict, nombre_esquema: str,
                         temperatura: float = 0.6, razonamiento: str | None = None) -> dict | None:
    """Igual que consultar, pero sin mensajes en pantalla ni respuesta de demostración: devuelve
    None si nadie responde. Se usa para pasos auxiliares (por ejemplo, aplicar el tono del equipo)."""
    if str(_secreto("MODO_DEMO", "no")).lower() == "si":
        return None
    global TEMPERATURA
    anterior = TEMPERATURA
    try:
        TEMPERATURA = temperatura
        for e in [x for x in cadena() if not _pausado(x)]:
            try:
                return _llamar(e, sistema, usuario, esquema, nombre_esquema, razonamiento)
            except RateLimitError:
                _pausar(e, PAUSA_SATURADO)
            except (AuthenticationError, PermissionDeniedError, NotFoundError):
                _pausar(e, PAUSA_INVALIDO)
            except Exception as err:
                print(f"[llm] paso auxiliar {e['proveedor']}/{e['modelo']}: {type(err).__name__} {str(err)[:120]}", flush=True)
        return None
    finally:
        TEMPERATURA = anterior
