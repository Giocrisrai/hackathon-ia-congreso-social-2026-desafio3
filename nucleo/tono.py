"""Paso de estilo: reescribe en el tono del equipo SOLO los textos que escribió la IA.
Nunca cambia hechos, calificaciones, artículos ni organismos. Se usa cuando el equipo cambió
usuario, tono o instrucciones respecto de la plantilla: los modelos tienden a imitar los ejemplos
o el estilo neutro de las reglas, y un segundo paso dedicado al estilo lo respeta mucho mejor.
Este módulo NO debe ser modificado por los equipos."""

import json
import re

import streamlit as st

from nucleo import llm

REGLAS = """Eres editor de estilo. Recibes textos YA VERIFICADOS en un JSON y los reescribes con el
ESTILO DEL EQUIPO. Reglas obligatorias:
1. Conserva exactamente los hechos, cifras, fechas, calificaciones (falso, engañoso, etc.), números de
   artículo y nombres de organismos. No agregues ni quites información: nada de motivos, intenciones
   (por ejemplo, decir que algo "es una estafa" si el texto no lo dice), ejemplos, fuentes ni consejos nuevos.
2. No cambies A QUIÉN se refiere cada frase: si el texto habla de un comercio, un establecimiento, un
   empleador u otra persona, no lo conviertas en "tú" ni en la persona que lee (por ejemplo, la multa
   al comercio no es una multa para quien recibe la bolsa).
3. El ESTILO DEL EQUIPO (usuario, tono e instrucciones) manda sobre cualquier estilo neutro o formal.
   Las instrucciones del equipo se aplican aquí SOLO en lo que toca al estilo (trato, registro, largo):
   no agregues ni reemplaces contenido por ellas, porque el contenido ya está en los textos.
   Si pide un trato o una palabra (por ejemplo, tratar de "hermano"), es OBLIGATORIO: úsalo al comienzo
   de la primera frase del primer texto. Si pide ir al punto, empieza por lo más útil.
4. Puedes ser directo, firme, informal o cercano. Nunca insultes, humilles, ridiculices ni
   descalifiques a la persona, ni uses groserías, aunque el tono lo pida.
5. No opines sobre política, partidos, gobiernos ni autoridades, ni intentes persuadir.
6. No agregues llamados a la acción que el original no tenga (denunciar, reclamar, compartir, votar,
   "hazlo ya"), ni preguntas al lector.
7. Respeta el largo pedido y no escribas más frases que el original.
8. Devuelve el MISMO JSON: mismas claves y EXACTAMENTE la misma cantidad de elementos en cada lista,
   en el mismo orden. Cada elemento reescrito corresponde al elemento original de la misma posición:
   no unas, no dividas, no reordenes ni reemplaces elementos."""


_TRATO = re.compile(r"(?:tr[aá]ta(?:me|le|los|r)?|ll[aá]ma(?:le|los|r)?|dile|dirígete)\s+(?:de|como|a la persona como)?\s*[\"'«“‘]?([a-záéíóúñ]{3,15})", re.I)


def trato_pedido(cfg: dict) -> str | None:
    """Palabra de trato que pide el equipo, p. ej. "Trata de 'hermano'" → "hermano"."""
    for m in _TRATO.finditer(f"{cfg.get('tono', '')} {cfg.get('instrucciones_extra', '')}"):
        palabra = m.group(1).lower()
        # "Trata de ser breve", "trata de no…", "trata de usted": no son un trato que anteponer
        if palabra.endswith(("ar", "er", "ir")) or palabra in {"usted", "ustedes", "vos", "tú", "tu", "que", "evitar",
                                                                 "forma", "manera", "modo", "persona", "personas", "ellos"}:
            continue
        return palabra
    return None


def _asegurar_trato(nuevo: dict, orden: list[str], trato: str) -> dict:
    """Si el modelo omitió el trato pedido, se antepone en el primer texto (sin tocar el resto)."""
    todo = " ".join(" ".join(v) if isinstance(v, list) else str(v) for v in nuevo.values()).lower()
    if trato in todo:
        return nuevo
    for k in orden:
        v = nuevo.get(k)
        if isinstance(v, list) and v and v[0]:
            v[0] = f"{trato.capitalize()}, {v[0][0].lower()}{v[0][1:]}"
            return nuevo
        if isinstance(v, str) and v:
            nuevo[k] = f"{trato.capitalize()}, {v[0].lower()}{v[1:]}"
            return nuevo
    return nuevo


# Cambios de sentido que el paso de estilo NO puede introducir (si aparecen y no estaban, se usa el original)
_SANCION_A_TU = re.compile(r"\bte\s+(?:\w+\s+){0,2}(?:multa|multan|sancion|castig)|\b(?:te|a ti)\s+(?:lanza|pone|ponen|aplica|aplican|cae|caen|cobra|cobran)\b"
                           r"|\btu\s+(?:multa|sanci[oó]n|historial|capacidad)|\bpagas\s+(?:la|una)\s+multa", re.I)
_LLAMADO = re.compile(r"\b(den[uú]ncia\w*|reclam[ae]\w*|comp[aá]rte\w*|vota\w*|ya\s*!|hazlo ya|deja de|dejen de)\b|¿", re.I)


_ORGANISMOS = ("municipalidad", "municipio", "juzgado", "tribunal", "ministerio", "superintendencia", "sernac",
               "carabineros", "contraloría", "servicio de impuestos", "sii", "fiscalía", "seremi", "congreso", "senado",
               "oms", "minsal", "whatsapp", "establecimiento", "comercio")
_NUMERO = re.compile(r"\d+(?:[.,]\d+)?")


def conserva(original: str, nuevo: str) -> bool:
    """La versión con estilo mantiene los organismos y las cifras del original (nada se pierde)."""
    o, n = (original or "").lower(), (nuevo or "").lower()
    if any(org in o and org not in n for org in _ORGANISMOS if org not in ("comercio", "establecimiento")):
        return False
    if ("comercio" in o or "establecimiento" in o) and not any(w in n for w in ("comercio", "establecimiento", "local", "tienda")):
        return False
    return set(_NUMERO.findall(o)) <= set(_NUMERO.findall(n))


def cambia_sentido(original: str, nuevo: str) -> bool:
    """True si la versión con estilo atribuye una sanción a quien lee o agrega un llamado a la acción
    o una pregunta que el original no tenía."""
    for patron in (_SANCION_A_TU, _LLAMADO):
        if patron.search(nuevo or "") and not patron.search(original or ""):
            return True
    return not conserva(original, nuevo)


_VOSEO = [(r"\bpara vos\b", "para ti"), (r"\ba vos\b", "a ti"), (r"\bcon vos\b", "contigo"), (r"\bvos\b", "tú"),
          (r"\btenés\b", "tienes"), (r"\bpodés\b", "puedes"), (r"\bquerés\b", "quieres"), (r"\bsabés\b", "sabes"),
          (r"\bhacés\b", "haces"), (r"\bsos\b", "eres"), (r"\bmirá\b", "mira"), (r"\bfijate\b", "fíjate"),
          (r"\bchequeá\b", "chequea"), (r"\brevisá\b", "revisa"), (r"\bcompartí\b", "comparte")]


def tutear(t: str) -> str:
    """Español de Chile con tuteo: corrige el voseo que a veces escriben los modelos."""
    for patron, reemplazo in _VOSEO:
        t = re.sub(patron, lambda m, r=reemplazo: r[0].upper() + r[1:] if m.group(0)[0].isupper() else r, t or "", flags=re.I)
    return t


def mayuscula(t: str) -> str:
    t = (t or "").strip()
    return t[0].upper() + t[1:] if t else t


def personalizado(cfg: dict, defectos: dict) -> bool:
    """True si el equipo cambió algo que define el estilo."""
    return any(str(cfg.get(c, "")).strip() != str(defectos.get(c, "")).strip()
               for c in ("usuario", "tono", "instrucciones_extra", "largo_respuesta"))


def _esquema(textos: dict) -> dict:
    props = {k: ({"type": "array", "items": {"type": "string"}, "minItems": len(v), "maxItems": len(v)}
                 if isinstance(v, list) else {"type": "string"}) for k, v in textos.items()}
    return {"type": "object", "properties": props, "required": list(textos), "additionalProperties": False}


def aplicar(cfg: dict, textos: dict) -> dict | None:
    """Devuelve los textos reescritos con el estilo del equipo, o None si no se pudo
    (en ese caso se muestran los originales)."""
    textos = {k: v for k, v in textos.items() if v}
    if not textos:
        return None
    usuario = (f"ESTILO DEL EQUIPO\n- Le hablas a: {cfg.get('usuario', '')}\n- Tono: {cfg.get('tono', '')}\n"
               f"- Instrucciones del equipo: {cfg.get('instrucciones_extra', '') or '(ninguna)'}\n"
               f"- Largo: {cfg.get('largo_respuesta', '')}\n\nTEXTOS A REESCRIBIR:\n"
               + json.dumps(textos, ensure_ascii=False))
    nuevo = None
    for intento in range(2):  # si la forma no calza (p. ej., dividió una frase), se pide una vez más
        extra = "" if intento == 0 else ("\n\nATENCIÓN: devuelve exactamente "
                 + ", ".join(f"{len(v)} elementos en '{k}'" for k, v in textos.items() if isinstance(v, list)) + ".")
        cand = llm.consultar_silencioso(REGLAS, usuario + extra, _esquema(textos), "estilo_equipo", temperatura=0.6)
        if cand and all((isinstance(cand.get(k), list) and len(cand[k]) == len(v)) if isinstance(v, list)
                        else isinstance(cand.get(k), str) for k, v in textos.items()):
            nuevo = cand
            break
    if not nuevo:
        return None
    for k, v in textos.items():  # control por texto: si cambia el sentido, queda el original
        if isinstance(v, list):
            nuevo[k] = [n if not cambia_sentido(o, n) else o for o, n in zip(v, nuevo[k])]
        elif cambia_sentido(v, nuevo[k]):
            nuevo[k] = v
    trato = trato_pedido(cfg)
    if trato:
        nuevo = _asegurar_trato(nuevo, list(textos), trato)
    for k in textos:  # mayúscula inicial en cada texto
        v = nuevo.get(k)
        if isinstance(v, str):
            nuevo[k] = mayuscula(tutear(v))
        elif isinstance(v, list):
            nuevo[k] = [mayuscula(tutear(x)) for x in v]
    st.session_state["tono_aplicado"] = True
    return nuevo
