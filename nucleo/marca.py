"""Logos de las instituciones organizadoras (PUC a la izquierda, Duoc UC a la derecha)."""
import base64
from pathlib import Path

import streamlit as st

CARPETA = Path(__file__).resolve().parent.parent / "assets"


@st.cache_data
def _b64(nombre: str) -> str:
    try:
        return base64.b64encode((CARPETA / nombre).read_bytes()).decode()
    except Exception:
        return ""


def logos():
    uc, duoc = _b64("logo_uc.png"), _b64("logo_duoc.png")
    if not (uc and duoc):
        return
    st.markdown(
        f"""<div style="display:flex;justify-content:space-between;align-items:center;gap:16px;margin:-8px 0 6px 0">
        <img src="data:image/png;base64,{uc}" alt="Pontificia Universidad Católica de Chile" style="height:56px;width:auto">
        <img src="data:image/png;base64,{duoc}" alt="Duoc UC" style="height:34px;width:auto">
        </div>""",
        unsafe_allow_html=True,
    )
