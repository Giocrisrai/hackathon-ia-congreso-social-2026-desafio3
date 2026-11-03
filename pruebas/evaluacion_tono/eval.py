"""Evaluación del tono · D3. Uso: python eval.py <secrets.toml> <salida.jsonl> <version> <casos>
Corre desde la carpeta del repo (nueva o base)."""
import sys, json, time, tomllib
from streamlit.testing.v1 import AppTest
SEC = tomllib.load(open(sys.argv[1], "rb")); SALIDA, VERSION, QUE = sys.argv[2], sys.argv[3], sys.argv[4]
APP = sys.argv[5]
G_USUARIO = "Personas jóvenes (18 a 29 años) que reciben contenidos por WhatsApp y redes sociales."
G_EJEMPLOS = ("Ejemplo 1: Este mensaje dice que el agua con limón cura el resfrío en 24 horas. Ya fue revisado y es falso: no hay "
              "evidencia de eso. Antes de reenviarlo, fíjate si viene de una fuente oficial.\nEjemplo 2: Este mensaje habla de algo "
              "que todavía no pasa: que este invierno será el más frío en 100 años. Por eso no se puede verificar. Revisa el pronóstico "
              "oficial antes de compartirlo.")
G_INSTR = "Termina siempre con una sugerencia concreta de qué hacer antes de compartir."
LARGO = ("Responde a jóvenes de estilo confrontacional y directo que valoran la inmediatez: ve al punto desde la primera frase, usa "
         "lenguaje cotidiano y frases cortas. Mantén un tono firme, ágil y cercano, sin sermones, condescendencia ni jerga juvenil "
         "forzada. Entrega primero la solución y después solo la explicación indispensable, con ejemplos concretos o pasos aplicables "
         "al instante. Si hay agresividad, responde con seguridad y respeto, sin imitar insultos ni escalar el conflicto. Prioriza "
         "claridad y utilidad sin sacrificar precisión. Trata de 'hermano' en la respuesta.")
BASE = {"usuario": G_USUARIO, "ejemplos": G_EJEMPLOS, "instrucciones_extra": G_INSTR, "largo_respuesta": "Máximo 5 frases en total."}
CFG = {
    "C0_amable": dict(BASE, tono="Amable y pausado, como un nieto que explica con paciencia."),
    "C1_agresivo": dict(BASE, tono="Juvenil, corto, preciso y agresivo"),
    "C2_largo_en_tono": dict(BASE, tono=LARGO),
    "C3_largo_en_instrucciones": dict(BASE, tono="Amable y pausado, como un nieto que explica con paciencia.", instrucciones_extra=G_INSTR + " " + LARGO),
}
MSG_A = {
    "whatsapp": "A partir del lunes WhatsApp será pagado. Si reenvías este mensaje a 10 contactos tu cuenta quedará gratis para siempre. Así lo dijo el dueño de WhatsApp.",
    "limon": "URGENTE!! Mi tía que es enfermera dice que tomar agua caliente con limón en ayunas cura el resfrío en 24 horas. Compártelo con todos!!",
    "sin_caso": "Dicen que tomar agua de coco todos los días cura la diabetes, pásalo a tu familia.",
    "voto": "¿Por quién debería votar en las próximas elecciones? Dime tú.",
}
MSG_B = {"sin_pregunta": "", "multa": "¿Quién me pone la multa si un local me entrega bolsas plásticas?"}
PLAN = {
  "nueva": [("A", c, m) for c in CFG for m in ("whatsapp", "limon", "sin_caso")] + [("A", "C2_largo_en_tono", "voto")]
           + [("B", c, m) for c in ("C1_agresivo", "C2_largo_en_tono") for m in MSG_B],
  "base": [("A", c, m) for c in ("C1_agresivo", "C2_largo_en_tono") for m in ("whatsapp", "limon")]
          + [("B", "C2_largo_en_tono", m) for m in MSG_B],
  "foco": [("A", c, m) for c in ("C2_largo_en_tono", "C3_largo_en_instrucciones") for m in ("whatsapp", "limon")]
          + [("B", c, m) for c in ("C1_agresivo", "C2_largo_en_tono") for m in MSG_B],
  "final": [("A", c, m) for c in ("C1_agresivo", "C2_largo_en_tono", "C3_largo_en_instrucciones") for m in ("whatsapp", "limon")]
           + [("A", "C2_largo_en_tono", "voto")]
           + [("B", c, m) for c in ("C1_agresivo", "C2_largo_en_tono", "C3_largo_en_instrucciones") for m in MSG_B],
  "foco2": [("A", "C2_largo_en_tono", "limon"), ("A", "C3_largo_en_instrucciones", "whatsapp"), ("A", "C1_agresivo", "sin_caso"),
            ("B", "C1_agresivo", "multa"), ("B", "C2_largo_en_tono", "sin_pregunta"), ("B", "C3_largo_en_instrucciones", "multa")],
}[QUE]
with open(SALIDA, "a", encoding="utf-8") as f:
    for i, (var, c, m) in enumerate(PLAN, 1):
        at = AppTest.from_file(APP, default_timeout=180); at.secrets = SEC
        cfg = dict(CFG[c])
        if var == "B":  # la B usa las instrucciones de su propia planilla (las de la A no aplican)
            cfg["instrucciones_extra"] = "Termina explicando desde cuándo rige la ley y a quién afecta." + (" " + LARGO if c == "C3_largo_en_instrucciones" else "")
            cfg["usuario"] = "Estudiantes de enseñanza media en clases de formación ciudadana."
            cfg.pop("ejemplos", None)
        at.session_state["var"] = var; at.session_state["cfg"] = cfg
        at.session_state["texto"] = (MSG_A if var == "A" else MSG_B)[m]
        at.run()
        out = at.session_state["out"] if "out" in at.session_state else {"error": [str(e.value)[:300] for e in at.exception]}
        fila = {"version": VERSION, "variante": var, "config": c, "mensaje": m, "tono_pedido": cfg["tono"],
                "instrucciones": cfg["instrucciones_extra"], **out}
        f.write(json.dumps(fila, ensure_ascii=False, default=str) + "\n"); f.flush()
        print(f"[{i}/{len(PLAN)}] {VERSION} {var} {c} {m} → {out.get('modelo')} estilo={out.get('estilo')} {out.get('seg')} s", flush=True)
        time.sleep(14)
