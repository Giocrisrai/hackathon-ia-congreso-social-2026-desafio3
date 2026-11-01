"""Salvaguardas fijas: aviso de IA, ingreso por equipo y cuota de uso.
Este módulo NO debe ser modificado por los equipos.

Equipos en los secrets, en cualquiera de los dos formatos:
    [equipos]                      [equipos.E01]
    E01 = "clave"          o       nombre = "Equipo 01"
                                   clave = "clave"
Los códigos que empiezan con M son de mentores: tienen cuota propia y ven el diagnóstico de la IA.
"""

import time
from threading import Lock
import streamlit as st

from nucleo import llm, registro

AVISO_IA = (
    "⚠️ **Esta herramienta usa inteligencia artificial.** "
    "Las respuestas pueden contener errores y no reemplazan el juicio humano. "
    "Revisa siempre las fuentes citadas. Todas las consultas quedan registradas."
)


def mostrar_aviso():
    """Aviso visible y permanente de uso de IA."""
    st.info(AVISO_IA)


def _equipos() -> dict:
    """{código: (clave, nombre)} desde los secrets."""
    try:
        crudo = st.secrets.get("equipos", {})
    except Exception:
        crudo = {}
    salida = {}
    for cod, val in dict(crudo).items():
        if isinstance(val, str):
            salida[cod.upper()] = (val, cod.upper())
        elif hasattr(val, "get"):
            salida[cod.upper()] = (str(val.get("clave", "")), str(val.get("nombre", cod.upper())))
    return salida


def _barra_lateral(equipo: str):
    with st.sidebar:
        st.divider()
        st.markdown(f"**👥 {st.session_state.get('equipo_nombre', equipo)}** · `{equipo}`")
        enlaces = llm.describir()
        if enlaces:
            with st.expander("🤖 IA en uso"):
                st.caption("Se prueban en este orden; si uno falla, pasa al siguiente.")
                for e in enlaces:
                    st.write(f"- {e}")
        # El botón del registro se llena al final de la página (pie), cuando ya quedó registrada la última acción
        st.session_state["_ph_registro"] = st.empty()
        if st.button("Cerrar sesión"):
            for k in ("equipo", "equipo_nombre", "ultimo", "ultimo_b"):
                st.session_state.pop(k, None)
            st.rerun()


def ingresar_equipo() -> str | None:
    """Pide código y clave del equipo. Devuelve el código si es válido."""
    if st.session_state.get("equipo"):
        _barra_lateral(st.session_state["equipo"])
        return st.session_state["equipo"]

    st.subheader("Ingreso del equipo")
    codigo = st.text_input("Código del equipo (ej: E01)").strip().upper()
    clave = st.text_input("Clave del equipo", type="password").strip()

    if st.button("Ingresar"):
        equipos = _equipos()
        if codigo in equipos and equipos[codigo][0] == clave:
            st.session_state["equipo"] = codigo
            st.session_state["equipo_nombre"] = equipos[codigo][1]
            st.rerun()
        else:
            st.error("Código o clave incorrectos.")
    st.caption("El código y la clave los entrega tu mentor.")
    return None


@st.cache_resource
def _contador():
    """Contador compartido entre todas las sesiones de esta app."""
    return {"usos": {}, "lock": Lock()}


def _limite() -> int:
    try:
        ia = st.secrets.get("ia", {})
        return int(st.secrets.get("CUOTA_POR_EQUIPO", ia.get("limite_consultas_por_equipo", 120)))
    except Exception:
        return 120


def consumir_cuota(equipo: str) -> bool:
    """Descuenta una consulta. Devuelve False si el equipo agotó su cuota."""
    c = _contador()
    with c["lock"]:
        usados = c["usos"].get(equipo, 0)
        if usados >= _limite():
            return False
        c["usos"][equipo] = usados + 1
        return True


def cuota_restante(equipo: str) -> int:
    return max(_limite() - _contador()["usos"].get(equipo, 0), 0)


def _es_mentor(equipo: str) -> bool:
    return equipo == "T00" or equipo.startswith("M")


def pie(equipo: str):
    """Al final de la página: consultas restantes y registro descargable, ya actualizados."""
    quien = "de tu código de mentor" if _es_mentor(equipo) else "del equipo"
    st.caption(f"Consultas restantes {quien}: {cuota_restante(equipo)} de {_limite()}")
    ph = st.session_state.get("_ph_registro")
    filas = registro.filas(equipo)
    if ph is not None and filas:
        ph.download_button(f"⬇️ Descargar registro ({len(filas)})", registro.exportar_csv(filas),
                           file_name=f"registro_{equipo}.csv", mime="text/csv")


def es_repeticion(firma: str, segundos: int = 20) -> bool:
    """True si es la misma consulta que se acaba de hacer (doble clic o Enter + clic):
    así no se gasta otra consulta ni se registra dos veces."""
    ultima = st.session_state.get("_ultima_consulta")
    ahora = time.time()
    if ultima and ultima[0] == firma and ahora - ultima[1] < segundos:
        return True
    st.session_state["_ultima_consulta"] = (firma, ahora)
    return False
