"""Perfil juvenil para la Variante B · 'La ley en simple'.

Este módulo es una pieza NUEVA y opcional. No reemplaza las REGLAS_FIJAS de
`variantes/b_ley_simple.py`: entrega el bloque de tono que se inserta ANTES de
esas reglas, para que las salvaguardas sigan teniendo prioridad.

No importa Streamlit, pandas ni la IA: son funciones puras y testeables.
La integración en la pantalla la hace quien sea dueño/a de `b_ley_simple.py`.

Uso previsto:
    from variantes import b_perfil
    perfil = b_perfil.normalizar_perfil(perfil_elegido)
    sistema = armar_sistema(cfg, ley, perfil)          # b_ley_simple.py
    bloque = b_perfil.bloque_dignidad_desde_frases(
        info["nombre_ley"], frases, categoria="trabajo")
"""

from __future__ import annotations

import re
import unicodedata

PERFIL_DEFECTO = "Escolar"
PERFILES = ("Escolar", "Universitario", "Laboral/Cesante")

# Alias que puede mandar el frontend o la planilla, ya sin tildes ni mayúsculas.
_ALIAS = {
    "escolar": "Escolar",
    "colegio": "Escolar",
    "colegial": "Escolar",
    "media": "Escolar",
    "ensenanza media": "Escolar",
    "estudiante de media": "Escolar",
    "universitario": "Universitario",
    "universitaria": "Universitario",
    "universidad": "Universitario",
    "superior": "Universitario",
    "educacion superior": "Universitario",
    "estudiante universitario": "Universitario",
    "laboral": "Laboral/Cesante",
    "cesante": "Laboral/Cesante",
    "trabajador": "Laboral/Cesante",
    "trabajadora": "Laboral/Cesante",
    "laboral/cesante": "Laboral/Cesante",
    "laboral o cesante": "Laboral/Cesante",
    "joven trabajador": "Laboral/Cesante",
}

# Cambian CÓMO se explica, nunca QUÉ dice la ley.
_REGLAS = {
    "Escolar": (
        "Explica usando analogías del colegio, la vida cotidiana y emojis. "
        "Evita tecnicismos jurídicos densos."
    ),
    "Universitario": (
        "Mantén un lenguaje formal y técnico, explicando la estructura de la ley "
        "(qué regula, a quién obliga y cómo se fiscaliza)."
    ),
    "Laboral/Cesante": (
        "Enfócate en el beneficio práctico, los plazos y cómo esto impacta el bolsillo "
        "o el empleo. Menciona subsidios solo si el texto de la ley los establece."
    ),
}

_TEMAS = {
    "trabajo": "Esta norma reconoce el valor del trabajo y de quienes buscan o tienen un empleo.",
    "educacion": "Esta norma reconoce el valor de la formación y de quienes estudian o se preparan para trabajar.",
    "ecologia": "Esta norma reconoce el valor de los ecosistemas y de las comunidades que viven cerca de ellos.",
    "generico": "Esta norma reconoce el valor de las personas y de su vida en comunidad.",
}


def _sin_acentos(texto: str) -> str:
    """Minúsculas, sin tildes y sin espacios repetidos. Sirve para comparar alias."""
    limpio = "".join(
        c for c in unicodedata.normalize("NFKD", str(texto or ""))
        if not unicodedata.combining(c)
    )
    return re.sub(r"\s+", " ", limpio.lower()).strip()


def normalizar_perfil(valor: str) -> str:
    """Devuelve uno de PERFILES. Si no reconoce el valor, usa PERFIL_DEFECTO.

    Acepta variantes como 'escolar', 'Estudiante de enseñanza media',
    'universidad', 'laboral-cesante' o 'cesante'.
    """
    t = _sin_acentos(valor).replace("-", "/")
    t = re.sub(r"\s*/\s*", "/", t)
    if t in _ALIAS:
        return _ALIAS[t]
    if any(p in t for p in ("escolar", "colegio", "colegial", "ensenanza media", "estudiante de media")):
        return "Escolar"
    if any(p in t for p in ("universitari", "universidad", "educacion superior", "estudiante superior")):
        return "Universitario"
    if any(p in t for p in ("laboral", "cesante", "trabajador", "empleo", "joven trabajador")):
        return "Laboral/Cesante"
    return PERFIL_DEFECTO


def instrucciones_perfil(perfil: str) -> str:
    """Bloque de tono para pegar ANTES de las REGLAS_FIJAS del sistema."""
    activo = normalizar_perfil(perfil)
    reglas = "\n".join(f"- {p}: {_REGLAS[p]}" for p in PERFILES)
    return f"""PERFIL DEL USUARIO: {activo}

REGLAS DE TONO POR PERFIL (solo cambian CÓMO lo dices; nunca QUÉ dice la ley):
{reglas}

PERFIL ACTIVO: {activo}. Aplica la regla de ese perfil y no las otras.
Si el perfil pide un registro juvenil, informal o regional, úsalo sin cambiar lo que dice la ley.
No inventes beneficios, montos, plazos ni organismos que no aparezcan en los artículos."""


def _limpiar_articulos(articulos) -> list[str]:
    """Convierte a texto, quita vacíos y duplicados sin perder el orden."""
    vistos: list[str] = []
    for articulo in articulos or []:
        if articulo is None:
            continue
        a = str(articulo).strip()
        if a and a not in vistos:
            vistos.append(a)
    return vistos


def articulos_citados(frases: list[dict]) -> list[str]:
    """Artículos de las frases ya validadas, en orden y sin repetir.

    Se usa para que el bloque de dignidad cite exactamente los mismos artículos
    que la explicación, sin agregar citas nuevas.
    """
    vistos: list[str] = []
    for frase in frases or []:
        if not isinstance(frase, dict):
            continue
        arts = frase.get("articulos") or []
        if isinstance(arts, str):
            arts = [arts]
        for a in _limpiar_articulos(arts):
            if a not in vistos:
                vistos.append(a)
    return vistos


def _categoria(valor: str) -> str:
    """Normaliza una categoría o, si recibe el nombre de la ley, la infiere."""
    t = _sin_acentos(valor)
    if t in ("trabajo", "laboral", "empleo"):
        return "trabajo"
    if t in ("educacion", "practica", "formacion", "estudios"):
        return "educacion"
    if t in ("ecologia", "medio ambiente", "ambiental", "humedal", "humedales"):
        return "ecologia"
    if any(p in t for p in ("humedal", "ambiental", "medio ambiente", "bolsa", "plastica",
                            "plastico", "residuo", "reciclaje", "ecolog")):
        return "ecologia"
    if "practica" in t or "educacion" in t or "formacion" in t:
        return "educacion"
    if "trabajo" in t or "laboral" in t or "jornada" in t or "empleo" in t:
        return "trabajo"
    return "generico"


def inferir_categoria(nombre_ley: str) -> str:
    """Infiere 'trabajo', 'educacion', 'ecologia' o 'generico' desde el nombre de la ley."""
    return _categoria(nombre_ley)


def bloque_dignidad(nombre_ley: str, articulos: list[str], categoria: str = "") -> str:
    """Bloque determinista de cierre, sin datos nuevos ni juicios políticos.

    - `nombre_ley`: nombre oficial que se muestra al usuario.
    - `articulos`: artículos ya validados por `b_ley_simple.validar`.
    - `categoria`: 'trabajo', 'educacion', 'ecologia' o vacío para inferir del nombre.

    No pasa por la IA: así no puede alucinar cifras, organismos ni beneficios.
    Si se prefiere que lo redacte el modelo, debe ser un campo validado del
    esquema, no texto libre.
    """
    nombre = (nombre_ley or "la ley").strip()
    arts = _limpiar_articulos(articulos)
    cita = f" (arts. {', '.join(arts)})" if arts else ""
    tema = _TEMAS[_categoria(categoria or nombre)]
    return (
        "🌿 **Impacto en la Dignidad Humana**\n\n"
        f"{tema} La explicación se apoya en {nombre}{cita}. "
        "La norma no reemplaza el juicio de la persona: busca que pueda entender "
        "sus derechos y deberes en su comunidad."
    )


def bloque_dignidad_desde_frases(nombre_ley: str, frases: list[dict], categoria: str = "") -> str:
    """Atajo para la pantalla: toma los artículos de las frases y arma el bloque."""
    return bloque_dignidad(nombre_ley, articulos_citados(frases), categoria)
