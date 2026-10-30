"""Registro de cada interacción.
- Siempre: copia en memoria de la app, descargable desde la barra lateral (cada equipo ve lo suyo;
  tutores T00 y mentores M.. ven todo).
- Si los secrets traen REGISTRO_FORM_URL: además se envía al Google Form de la organización.
Este módulo es una salvaguarda: los equipos NO deben modificarlo."""

import csv as csv_mod
import io
from datetime import datetime
from threading import Lock
from zoneinfo import ZoneInfo

import requests
import streamlit as st

# Identificadores de los campos del Form (no son secretos)
CAMPOS = {
    "fecha_hora": "entry.1474272147",
    "variante": "entry.649513176",
    "equipo": "entry.328284184",
    "entrada": "entry.433310011",
    "salida": "entry.515570122",
    "modo": "entry.1204640115",
}

ZONA_HORARIA = ZoneInfo("America/Santiago")
LARGO_MAXIMO = 4000  # recorta textos muy largos para no exceder el Form
MAX_FILAS = 5000     # tope de la copia en memoria


@st.cache_resource
def _memoria():
    return {"filas": [], "lock": Lock()}


def registrar(variante: str, equipo: str, entrada: str, salida: str, modo: str) -> bool:
    """Guarda una fila. Devuelve True si se envió al Form.
    Nunca interrumpe la app: si falla, solo avisa en el registro de Streamlit."""
    fila = {
        "fecha_hora": datetime.now(ZONA_HORARIA).strftime("%Y-%m-%d %H:%M:%S"),
        "variante": variante,
        "equipo": equipo,
        "entrada": str(entrada)[:LARGO_MAXIMO],
        "salida": str(salida)[:LARGO_MAXIMO],
        "modo": modo,
        "modelo": st.session_state.get("ia_ultimo", "") if modo in ("real", "demo") else "",
    }
    m = _memoria()
    with m["lock"]:
        m["filas"].append(fila)
        del m["filas"][:-MAX_FILAS]

    try:
        url = st.secrets.get("REGISTRO_FORM_URL")
    except Exception:
        url = None
    if not url:
        return False
    try:
        r = requests.post(url, data={CAMPOS[k]: fila[k] for k in CAMPOS}, timeout=5)
        return r.status_code == 200
    except Exception as e:
        print(f"[registro] fallo al registrar: {e}", flush=True)
        return False


def filas(equipo: str) -> list[dict]:
    todas = list(_memoria()["filas"])
    if equipo == "T00" or equipo.startswith("M"):
        return todas
    return [f for f in todas if f["equipo"] == equipo]


def exportar_csv(filas_: list[dict]) -> bytes:
    buf = io.StringIO()
    w = csv_mod.DictWriter(buf, fieldnames=["fecha_hora", "variante", "equipo", "entrada", "salida", "modo", "modelo"])
    w.writeheader()
    w.writerows(filas_)
    return buf.getvalue().encode("utf-8-sig")

