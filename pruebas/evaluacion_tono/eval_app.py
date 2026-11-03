"""App de evaluación: corre el flujo real de una variante con la configuración dada (sin planilla)."""
import time
import streamlit as st
from variantes import a_verificador as A, b_ley_simple as B
from nucleo import llm
ss = st.session_state
t0 = time.time()
if ss["var"] == "A":
    cfg = dict(A.DEFECTOS); cfg.update(ss["cfg"]); corpus = A.cargar_corpus()
    if hasattr(A, "revisar"):
        r, caso, modo, estilo = A.revisar(cfg, corpus, ss["texto"], "libre")
    else:  # versión publicada antes de este cambio
        r, modo = llm.consultar(A.armar_sistema(cfg, corpus), ss["texto"], A.ESQUEMA, "revision_contenido", "A",
                                "libre", A.RESPALDO_DEMO, razonamiento="medium")
        r, caso = A.validar(r, corpus); estilo = False
    ss["out"] = {"r": r, "calif": None if caso is None else caso["calificacion"], "caso": None if caso is None else caso["id_caso"],
                 "verificada": None if caso is None else caso["explicacion"], "modo": modo, "estilo": estilo,
                 "modelo": ss.get("ia_ultimo"), "seg": round(time.time() - t0, 1)}
else:
    cfg = dict(B.DEFECTOS); cfg.update(ss["cfg"]); base = B.cargar_corpus()
    ley = base[base["id_ley"] == base["id_ley"].iloc[0]]
    msg = ss["texto"] or "Explícame esta ley en lenguaje claro."
    if hasattr(B, "explicar"):
        r, frases, desc, modo, estilo = B.explicar(cfg, ley, msg, "libre")
    else:
        r, modo = llm.consultar(B.armar_sistema(cfg, ley), msg, B.ESQUEMA, "explicacion_ley", "B", "libre", B.RESPALDO_DEMO)
        frases, desc = B.validar(r, ley); estilo = False
    ss["out"] = {"r": r, "frases": frases, "desc": desc, "modo": modo, "estilo": estilo, "modelo": ss.get("ia_ultimo"),
                 "seg": round(time.time() - t0, 1)}
