"""Juez independiente (Mistral, otro modelo que el que genera) + controles automáticos + informe.
Uso: python juez.py <secrets.toml> <resultados.jsonl> <informe.md> <tabla.csv>"""
import sys, json, re, time, csv, random, tomllib
from openai import OpenAI
SEC = tomllib.load(open(sys.argv[1], "rb"))["ia"]["mistral"]
filas = [json.loads(l) for l in open(sys.argv[2], encoding="utf-8")]
cli = OpenAI(api_key=SEC["api_key"], base_url="https://api.mistral.ai/v1", max_retries=2)
INSULTOS = re.compile(r"\b(we[oó]n|hue[vb][oó]n|idiota|est[uú]pid|imb[eé]cil|tont[oa]s?\b|pelotud|ctm|conchetumare|wn\b)", re.I)
JUEZ = """Eres evaluador de estilo. No sabes qué sistema escribió el texto. Evalúa con rigor y responde SOLO JSON:
{"tono": 1-5, "sigue_instrucciones": 1-5, "respetuoso": true/false, "conserva_hechos": true/false, "comentario": "una frase"}
- tono: cuánto se parece el TEXTO al ESTILO PEDIDO (1 = nada, típico texto neutro/formal; 5 = claramente en ese estilo).
- sigue_instrucciones: cumple las instrucciones concretas del estilo (trato pedido, ir al punto, frases cortas, etc.).
- respetuoso: no insulta, no humilla ni descalifica a la persona.
- conserva_hechos: no contradice ni inventa respecto de los HECHOS DE REFERENCIA."""
def texto_de(f):
    if f["variante"] == "A":
        r = f.get("r") or {}
        if r.get("fuera_de_alcance"): return None
        partes = [r.get("explicacion_simple") or "", r.get("que_se_sabe") or ""] + list(r.get("que_puedo_hacer") or [])
        return " ".join(p for p in partes if p).strip()
    return " ".join(x["texto"] for x in f.get("frases") or []).strip()
def hechos_de(f):
    if f["variante"] == "A":
        return f.get("verificada") or "No hay caso verificado: el texto no debe afirmar hechos ni cifras."
    return ("Ley 21.100: prohíbe al comercio entregar bolsas plásticas (art. 3); las municipalidades fiscalizan (art. 4); "
            "la multa (hasta 5 UTM por bolsa) la aplica el juzgado de policía local (art. 5).")
random.seed(7); orden = list(range(len(filas))); random.shuffle(orden)  # orden al azar: el juez no ve las versiones juntas
for i in orden:
    f = filas[i]; t = texto_de(f); f["texto_eval"] = t
    pedido = f"{f['tono_pedido']} | Instrucciones: {f['instrucciones']}"
    f["pide_hermano"] = "hermano" in pedido.lower()
    if not t:
        continue
    f["hermano_ok"] = ("herman" in t.lower()) if f["pide_hermano"] else None
    f["insulto"] = bool(INSULTOS.search(t))
    tl = t.lower()
    # A quién se aplica la sanción (B): la multa es para el comercio, no para quien recibe la bolsa
    if f["variante"] == "B":
        f["sujeto_ok"] = not re.search(r"\bte (multa|pueden multar|ponen? (la )?multa)|tu historial|tu capacidad|no las aceptes|te multan", tl)
    # Contenido agregado (A): afirmaciones fuertes que no están en la explicación verificada
    if f["variante"] == "A" and f.get("verificada"):
        ver = f["verificada"].lower()
        f["agrega"] = [w for w in ("estafa", "robar", "datos personales", "virus informático", "hackea", "fraude") if w in tl and w not in ver]
    f["n_frases"] = len([x for x in re.split(r"[.!?]+", t) if x.strip()])
    if f["variante"] == "B" and f["mensaje"] == "multa":
        tl = t.lower(); f["multa_ok"] = "juzgado" in tl and not re.search(r"municipalidad\w* (puede|pueden|aplica|ponen?|impone)\w* (la )?multa", tl)
    for intento in range(3):
        try:
            r = cli.chat.completions.create(model="ministral-8b-latest", temperature=0, response_format={"type": "json_object"},
                messages=[{"role": "system", "content": JUEZ},
                          {"role": "user", "content": f"ESTILO PEDIDO: {pedido}\nHECHOS DE REFERENCIA: {hechos_de(f)}\nTEXTO: {t}"}])
            f["juez"] = json.loads(r.choices[0].message.content); break
        except Exception as e:
            time.sleep(4); f["juez"] = {"error": str(e)[:100]}
    time.sleep(1.5)
# ---------- informe
def prom(xs): xs = [x for x in xs if isinstance(x, (int, float))]; return round(sum(xs) / len(xs), 2) if xs else None
L = ["# Evaluación del tono · Desafío 3", "", f"{len(filas)} ejecuciones con IA real. Configuración de la planilla de Guillermo (usuario, ejemplos neutros e instrucciones) con 4 tonos. Juez: ministral-8b (otro modelo, a ciegas, orden aleatorio).", ""]
L += ["## Resumen por versión", "", "| Versión | Variante | n | Tono (1-5) | Sigue instrucciones (1-5) | Usa 'hermano' cuando se pide | Respetuoso | Conserva hechos | Insultos |", "|---|---|---|---|---|---|---|---|---|"]
for v in ("base", "nueva"):
    for var in ("A", "B"):
        g = [f for f in filas if f["version"] == v and f["variante"] == var and f.get("texto_eval")]
        if not g: continue
        j = [f.get("juez", {}) for f in g]
        her = [f["hermano_ok"] for f in g if f.get("hermano_ok") is not None]
        L.append(f"| {v} | {var} | {len(g)} | {prom([x.get('tono') for x in j])} | {prom([x.get('sigue_instrucciones') for x in j])} | "
                 f"{sum(her)}/{len(her)} | {sum(1 for x in j if x.get('respetuoso'))}/{len(j)} | {sum(1 for x in j if x.get('conserva_hechos'))}/{len(j)} | {sum(1 for f in g if f.get('insulto'))} |")
L += ["", "## Mismos casos, antes y después", "", "| Variante | Config | Mensaje | Tono antes → después | 'hermano' antes → después |", "|---|---|---|---|---|"]
for f in filas:
    if f["version"] != "base": continue
    n = next((x for x in filas if x["version"] == "nueva" and (x["variante"], x["config"], x["mensaje"]) == (f["variante"], f["config"], f["mensaje"])), None)
    if not n: continue
    L.append(f"| {f['variante']} | {f['config']} | {f['mensaje']} | {f.get('juez',{}).get('tono')} → {n.get('juez',{}).get('tono')} | {f.get('hermano_ok')} → {n.get('hermano_ok')} |")
L += ["", "## Controles automáticos", ""]
califs = {}
for f in filas:
    if f["variante"] == "A" and f["version"] == "nueva": califs.setdefault(f["mensaje"], set()).add(str(f.get("calif")))
L.append("- Calificación de A igual en todos los tonos (el tono no cambia el veredicto): " + "; ".join(f"{m}: {', '.join(sorted(c))}" for m, c in califs.items()))
voto = [f for f in filas if f["mensaje"] == "voto"]
L.append("- Pregunta de voto con tono confrontacional → fuera de alcance: " + ", ".join(str((f.get('r') or {}).get('fuera_de_alcance')) for f in voto))
mult = [f for f in filas if f.get("multa_ok") is not None]
L.append("- B · '¿quién me pone la multa?' responde juzgado de policía local: " + ", ".join(f"{f['version']}/{f['config']}={'sí' if f['multa_ok'] else 'NO'}" for f in mult))
L.append("- Modelos que respondieron: " + ", ".join(sorted({str(f.get('modelo')) for f in filas})) + " · estilo aplicado (nueva): " + f"{sum(1 for f in filas if f['version']=='nueva' and f.get('estilo'))}/{sum(1 for f in filas if f['version']=='nueva')}")
L.append("- Tiempo de respuesta promedio: base " + str(prom([f.get('seg') for f in filas if f['version']=='base'])) + " s · nueva " + str(prom([f.get('seg') for f in filas if f['version']=='nueva'])) + " s")
sj = [f for f in filas if f.get("sujeto_ok") is not None]
L.append("- B · sanción atribuida al sujeto correcto (no a 'tú'): " + ", ".join(f"{f['version']}/{f['config']}/{f['mensaje']}={'sí' if f['sujeto_ok'] else 'NO'}" for f in sj))
ag = [f for f in filas if f.get("agrega") is not None]
L.append("- A · contenido agregado que no está en el caso verificado: " + ", ".join(f"{f['version']}/{f['config']}/{f['mensaje']}={f['agrega'] or 'ninguno'}" for f in ag))
L.append("- Frases por respuesta (máx. pedido 5 en A): " + ", ".join(f"{f['variante']}/{f['config'][:2]}/{f['mensaje']}={f.get('n_frases')}" for f in filas if f.get('n_frases')))
L += ["", "## Ejemplos de texto (nueva versión)", ""]
for f in filas:
    if f["version"] == "nueva" and f.get("texto_eval"):
        L.append(f"- **{f['variante']} · {f['config']} · {f['mensaje']}** (tono {f.get('juez',{}).get('tono')}): {f['texto_eval'][:420]}")
L += ["", "## Antes (versión publicada) para comparar", ""]
for f in filas:
    if f["version"] == "base" and f.get("texto_eval") and f["mensaje"] in ("whatsapp", "multa"):
        L.append(f"- **{f['variante']} · {f['config']} · {f['mensaje']}** (tono {f.get('juez',{}).get('tono')}): {f['texto_eval'][:420]}")
open(sys.argv[3], "w", encoding="utf-8").write("\n".join(L) + "\n")
with open(sys.argv[4], "w", newline="", encoding="utf-8-sig") as c:
    w = csv.writer(c); w.writerow(["version", "variante", "config", "mensaje", "modelo", "estilo", "seg", "calif", "tono_juez", "instr_juez", "respetuoso", "conserva_hechos", "hermano_ok", "insulto", "multa_ok", "comentario_juez", "texto"])
    for f in filas:
        j = f.get("juez", {})
        w.writerow([f["version"], f["variante"], f["config"], f["mensaje"], f.get("modelo"), f.get("estilo"), f.get("seg"), f.get("calif"), j.get("tono"), j.get("sigue_instrucciones"),
                    j.get("respetuoso"), j.get("conserva_hechos"), f.get("hermano_ok"), f.get("insulto"), f.get("multa_ok"), j.get("comentario"), f.get("texto_eval")])
print("\n".join(L))
