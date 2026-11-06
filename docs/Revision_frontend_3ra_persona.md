# Revisión del bloque de frontend (3ra persona)

**Veredicto:** la intención visual y de accesibilidad es buena, pero el bloque **no se puede integrar tal cual**. Tal como está, no arranca (dos `NameError`) y, si reemplaza `main()`, se lleva puestas las salvaguardas de la app: login por equipo, aviso de IA, cuota, registro, selección de ley, pregunta, resultado y descarga del CSV.

Este documento deja los errores, los riesgos éticos y una versión corregida para integrar **como prefacio**, no como reemplazo de `main()`.

---

## 1. Errores que impiden arrancar

| Línea del bloque | Problema | Corrección |
|---|---|---|
| `cfg = config.panel_config(DEFECT)` | `DEFECT` no existe; el nombre real es `DEFECTOS` | `cfg = config.panel_config(DEFECTOS)` |
| `if modo_accessible:` | La variable creada es `modo_accesible` (español); `modo_accessible` (inglés) no existe | Usar el mismo nombre: `if modo_accesible:` |
| `st.session_state.perfil_usuario = ...` | Funciona, pero mezcla estilo de atributo con el resto del archivo, que usa `st.session_state["..."]` | `st.session_state["perfil_usuario"] = ...` |
| `lector_voz = st.sidebar.checkbox(...)` | Se declara, pero nunca se usa | Implementar un botón “🔊 Leer explicación” o eliminar el checkbox |
| `categoria_seleccionada` | Se guarda, pero ningún código filtra las leyes por categoría | Conectar con el selector de leyes (ver sección 5) |
| `st.title("🏛️ Puerta Cívica...")` | Reemplaza el título configurable `cfg["titulo_app"]` y el texto de bienvenida de la Sheet | Usar `cfg["titulo_app"]` o agregar el nuevo título a `DEFECTOS`/Sheet |
| `st.write("---")` | Funciona, pero `st.divider()` es más claro | `st.divider()` |

---

## 2. Riesgos éticos y de neutralidad

### 2.1 “Voto Asistido”

El sidebar dice **“♿ Accesibilidad y Voto Asistido”**. Eso es un problema serio:

- La app no asiste votaciones; explica leyes.
- Las reglas fijas bloquean preguntas electorales (“¿por quién voto?”).
- Un mentor puede leer “Voto Asistido” como una funcionalidad política, justo lo que la ficha ética pide evitar.

**Corrección:** dejar el sidebar como **“♿ Accesibilidad”** y eliminar “Voto Asistido” de títulos, textos y botones. La asistencia por voz debe describirse como “leer la explicación en voz alta”.

### 2.2 Cita sin fuente

El bloque dice:

> “La Moneda es el máximo símbolo de nuestra democracia…”

No tiene fuente verificable. La app entera se apoya en no difundir información sin respaldo; una cita sin fuente en la portada contradice ese mensaje. Además, menciona un símbolo de gobierno y una figura religiosa (“San Alberto Hurtado”), lo que puede leerse como posicionamiento político o valórico.

**Corrección recomendada:** reemplazar por una frase neutra y sin atribución, por ejemplo:

> “Entender la ley es el primer paso para ejercer tus derechos.”

Si el equipo quiere una cita, debe venir con fuente oficial y ser revisada por el mentor. No usar citas de autoridad no verificadas.

### 2.3 Título y textos duros

“Puerta Cívica: Tu Entrada a la Democracia” no es partisanamente incorrecto, pero:

- reemplaza el título que viene de la Sheet;
- agrega una capa de marketing que no está en la ficha ética;
- puede desviar el foco de “explicar la ley” a “arenga cívica”.

**Corrección:** mantener `cfg["titulo_app"]` y, si quieren el título nuevo, ponerlo en `DEFECTOS` o en la pestaña `config` de la Sheet, para que sea configurable y quede registrado.

---

## 3. Lo que se pierde si esto reemplaza `main()`

El `main()` actual de `variantes/b_ley_simple.py` hace, en orden:

1. `marca.logos()` → logos obligatorios de la UC y Duoc UC.
2. `st.title(cfg["titulo_app"])` y texto de bienvenida desde la Sheet.
3. `salvaguardas.mostrar_aviso()` → aviso permanente de uso de IA.
4. `salvaguardas.ingresar_equipo()` → código y clave, cuota por equipo.
5. `corpus_del_equipo(cargar_corpus())` → leyes base + leyes extra.
6. Selector de ley, pregunta y botón.
7. `explicar()` → IA + validación de frases + estilo.
8. `mostrar_resultado()` → explicación con citas, descartes y proyecto de ley.
9. Encuesta de claridad y `registro.registrar()` → decisión humana y auditoría.
10. `salvaguardas.pie(equipo)` → consultas restantes y descarga del CSV.

Si el bloque de la 3ra persona se pega como `main()` completo, **todo lo anterior desaparece**. El bloque debe insertarse **después del login** y **antes de cargar el corpus**, dejando la lógica original intacta.

---

## 4. Accesibilidad: lo que falta

- **Modo alto contraste:** el CSS actual cubre `h1, h2, h3, p, label`, pero no inputs, selects, listas, spans ni el sidebar. Ampliar selectores y probar en la app real.
- **Caja de cita con colores fijos:** el `<div>` usa `#f0f2f6` y `#333333`; en alto contraste queda claro sobre negro y rompe el modo. Mejor usar `st.info()` y dejar que Streamlit aplique el tema.
- **Asistencia por voz:** el checkbox no hace nada. Implementar un botón con `speechSynthesis` del navegador (sin API externa) o eliminar la opción. No prometer accesibilidad que no se entrega.
- **Tamaño de letra:** el modo accesible puede subir la base a 18–20 px.
- **Foco y botones:** verificar que los botones tengan foco visible y etiquetas claras.
- **Emojis en etiquetas:** los lectores de pantalla los leen; no es bloqueante, pero conviene que el texto principal esté antes que el emoji.

---

## 5. Contrato con el backend

### Perfil

La 3ra persona debe dejar el perfil en:

```python
st.session_state["perfil_usuario"] = "Escolar"  # o "Universitario", "Laboral/Cesante"
```

El backend lo normaliza con `b_perfil.normalizar_perfil()` y lo pasa a `armar_sistema()` y `explicar()`.

**No crear dos selectores de perfil.** El que ya existe en el frontend es el único. El backend no debe agregar otro `st.selectbox`.

### Categoría

La categoría filtra **leyes**, no cambia el tono. Valores acordados:

```python
"ecologia", "educacion", "trabajo", None
```

Fuente de verdad, en orden:

1. Si `datos/b_leyes.csv` tiene una columna `categoria`, usarla.
2. Si no, inferir con `b_perfil.inferir_categoria(nombre_ley)`.
3. Si no hay coincidencias, mostrar “Todas” o un aviso, no una lista vacía.

`b_perfil.inferir_categoria()` ya reconoce Humedales, bolsas plásticas, jornada laboral y práctica profesional. Para las leyes base que no calzan, el usuario puede elegir “Todas”.

### Firma de repetición y registro

Incluir el perfil y la categoría en la firma para que cambiar de perfil no se detecte como “consulta repetida”:

```python
firma = f"B|{id_ley}|{perfil}|{categoria or 'todas'}|{pregunta.strip()}"
```

Y en el registro:

```python
entrada = f"{id_ley} | {perfil} | {categoria or 'todas'} | {mensaje}"
```

---

## 6. Versión corregida propuesta

La forma más limpia de evitar conflictos es que la 3ra persona implemente un módulo nuevo, `variantes/b_ui.py`, y que la Persona B lo llame desde `main()`. Así el frontend no edita `b_ley_simple.py`.

```python
# variantes/b_ui.py (propuesto)
"""Bloque visual de la Variante B. No toca IA, registro ni salvaguardas."""
from __future__ import annotations

import json
import re

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from variantes import b_perfil

PERFILES_UI = {
    "🎒 Escolar (Enseñanza Media / Menor de 18)": "Escolar",
    "🎓 Universitario o Técnico (Educación Superior)": "Universitario",
    "💼 Joven Laboral o Cesante (Buscando empleo / Emprendiendo)": "Laboral/Cesante",
}

CATEGORIAS_UI = {
    "🌐 Todas": None,
    "🌿 Ecología y Medioambiente": "ecologia",
    "📚 Educación y Cultura": "educacion",
    "💼 Trabajo y Oportunidades": "trabajo",
}

CSS_ALTO_CONTRASTE = """
<style>
.stApp, [data-testid="stSidebar"] { background-color: #000 !important; color: #fff !important; }
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp label,
.stApp li, .stApp span, .stApp div[data-testid="stMarkdownContainer"] { color: #ffff00 !important; }
.stApp input, .stApp textarea, .stApp select {
    background-color: #111 !important; color: #fff !important; border: 2px solid #ffff00 !important;
}
.stApp button { background-color: #ffff00 !important; color: #000 !important; border: 2px solid #fff !important; }
.stApp { font-size: 18px !important; }
</style>
"""


def accesibilidad() -> tuple[bool, bool]:
    """Sidebar de accesibilidad. Devuelve (alto_contraste, leer_en_voz)."""
    st.sidebar.markdown("## ♿ Accesibilidad")
    modo = st.sidebar.checkbox("Modo alto contraste", key="modo_accesible")
    voz = st.sidebar.checkbox("Asistencia por voz (leer respuesta)", key="lector_voz")
    if modo:
        st.markdown(CSS_ALTO_CONTRASTE, unsafe_allow_html=True)
    return modo, voz


def bienvenida(cfg: dict) -> None:
    """Título y bienvenida configurables desde la Sheet, sin citas sin fuente."""
    st.title(cfg["titulo_app"])
    st.caption("Desafío 3 · Ciudadanía informada · Hackathon IA Aplicada · Congreso Social UC 2026")
    st.info("Entender la ley es el primer paso para ejercer tus derechos.")
    st.write(cfg["texto_bienvenida"])


def selector_perfil() -> str:
    """Único selector de perfil. Deja el valor canónico en session_state."""
    st.subheader("1. Identifica tu perfil ciudadano")
    etiqueta = st.radio(
        "Selecciona tu momento de vida actual para adaptar las explicaciones:",
        list(PERFILES_UI),
        index=0,
        key="perfil_ui",
    )
    perfil = PERFILES_UI[etiqueta]
    st.session_state["perfil_usuario"] = perfil
    return perfil


def selector_categoria() -> str | None:
    """Filtro de leyes por causa. 'Todas' limpia el filtro."""
    st.subheader("2. ¿Qué causas te mueven hoy?")
    if "categoria_seleccionada" not in st.session_state:
        st.session_state["categoria_seleccionada"] = None

    columnas = st.columns(len(CATEGORIAS_UI))
    for columna, (etiqueta, valor) in zip(columnas, CATEGORIAS_UI.items()):
        with columna:
            if st.button(etiqueta, use_container_width=True, key=f"categoria_{valor}"):
                st.session_state["categoria_seleccionada"] = valor

    actual = st.session_state["categoria_seleccionada"]
    if actual:
        st.caption(f"Filtrando por **{actual}**. Elige 'Todas' para ver el resto.")
    return actual


def filtrar_por_categoria(corpus: pd.DataFrame, categoria: str | None) -> pd.DataFrame:
    """Filtra el corpus por la columna 'categoria' o, si no existe, por el nombre."""
    if not categoria:
        return corpus

    if "categoria" in corpus.columns:
        filtrado = corpus[corpus["categoria"].fillna("").str.strip().str.lower() == categoria]
        if len(filtrado):
            return filtrado

    ids = [
        id_ley
        for id_ley, grupo in corpus.groupby("id_ley")
        if b_perfil.inferir_categoria(str(grupo.iloc[0]["nombre_ley"])) == categoria
    ]
    return corpus[corpus["id_ley"].isin(ids)]


def boton_leer(texto: str) -> None:
    """Lee la explicación con la voz del navegador. Sin API externa."""
    limpio = re.sub(r"[*_#`>]", "", texto or "")
    components.html(
        f"""
        <button onclick="hablar()" style="padding:8px 14px;border-radius:8px;border:2px solid #1f77b4;background:#1f77b4;color:#fff;font-weight:600;cursor:pointer;">🔊 Leer explicación</button>
        <button onclick="parar()" style="padding:8px 14px;border-radius:8px;border:1px solid #999;background:#fff;color:#111;cursor:pointer;">⏹ Detener</button>
        <script>
          const texto = {json.dumps(limpio, ensure_ascii=False)};
          function hablar() {{
            speechSynthesis.cancel();
            const u = new SpeechSynthesisUtterance(texto);
            u.lang = "es-CL";
            u.rate = 0.95;
            speechSynthesis.speak(u);
          }}
          function parar() {{ speechSynthesis.cancel(); }}
        </script>
        """,
        height=64,
    )
```

### Integración en `main()`

```python
def main():
    st.set_page_config(page_title="La ley en simple · Desafío 3", page_icon="📜", layout="wide")
    cfg = config.panel_config(DEFECTOS)

    marca.logos()
    modo_accesible, lector_voz = b_ui.accesibilidad()
    b_ui.bienvenida(cfg)
    salvaguardas.mostrar_aviso()

    equipo = salvaguardas.ingresar_equipo()
    if not equipo:
        st.stop()

    perfil = b_ui.selector_perfil()
    categoria = b_ui.selector_categoria()

    corpus = b_ui.filtrar_por_categoria(corpus_del_equipo(cargar_corpus()), categoria)
    if corpus.empty:
        st.info("No hay leyes cargadas para esa categoría. Prueba con 'Todas'.")
        salvaguardas.pie(equipo)
        st.stop()

    # A partir de aquí, la lógica original de b_ley_simple.py:
    leyes = corpus.drop_duplicates("id_ley").set_index("id_ley")
    id_ley = st.selectbox("Ley", leyes.index.tolist(), format_func=lambda i: _etiqueta_ley(leyes, i))
    ley = corpus[corpus["id_ley"] == id_ley]

    pregunta = st.text_input("¿Tienes una pregunta específica sobre esta ley? (opcional)")
    # ... botón, explicar(..., perfil), registro, mostrar_resultado, encuesta, pie
```

En `explicar()` y `armar_sistema()` hay que pasar `perfil`. En `firma` y en `registro.registrar()` hay que incluir `perfil` y `categoria`. Después de `mostrar_resultado()`, agregar:

```python
bloque = b_perfil.bloque_dignidad_desde_frases(
    ley_ult.iloc[0]["nombre_ley"],
    frases,
    categoria=categoria or "",
)
st.markdown(bloque)

if lector_voz:
    b_ui.boton_leer(" ".join(f["texto"] for f in frases))
```

---

## 7. Checklist para la 3ra persona

- [ ] Corregir `DEFECT` → `DEFECTOS`.
- [ ] Corregir `modo_accessible` → `modo_accesible`.
- [ ] Quitar “Voto Asistido” de todos los textos.
- [ ] Quitar o reemplazar la cita sin fuente y la referencia religiosa.
- [ ] No reemplazar `main()`: insertar el bloque después del login.
- [ ] Mantener `marca.logos()`, `salvaguardas.mostrar_aviso()`, `ingresar_equipo()`, `pie()` y `registro.registrar()`.
- [ ] Implementar o eliminar el checkbox de voz.
- [ ] Conectar la categoría con el selector de leyes y agregar “Todas”.
- [ ] Dejar `st.session_state["perfil_usuario"]` en valores canónicos.
- [ ] Probar alto contraste en la app real, incluidos inputs, sidebar y cajas de aviso.
- [ ] Probar en celular: columnas, botones y textos largos.
- [ ] Confirmar que el título y la bienvenida siguen viniendo de `cfg`.
