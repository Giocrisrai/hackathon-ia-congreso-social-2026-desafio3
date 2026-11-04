# Guía para equipos · Copiar, publicar y mejorar el prototipo · Desafío 3

Cada equipo recibe el código de los prototipos del Desafío 3 y lo copia a su propia cuenta de GitHub. Desde ahí puede **mejorar** una de las variantes o **construir algo nuevo** sobre la misma base. Esta guía explica cómo hacerlo sin experiencia previa en despliegues. Su mentor acompaña a 4 equipos: pídanle ayuda cuando la necesiten.

| Variante | App oficial (para comparar) | Archivo principal | Lógica | Datos | Pestaña extra |
|---|---|---|---|---|---|
| A · Pausa antes de compartir | https://hackaton-d3-pausa.streamlit.app | `app_a.py` | `variantes/a_verificador.py` | `datos/a_casos.csv` | `casos_extra` |
| B · La ley en simple | https://hackaton-d3-ley.streamlit.app | `app_b.py` | `variantes/b_ley_simple.py` | `datos/b_leyes.csv` | `leyes_extra` |
| Algo nuevo del equipo | (la publican ustedes) | `app_nueva.py` | `variantes/c_nueva.py` | (los suyos) | — |

La herramienta es **neutral por diseño**: no opina, no persuade y no trata candidaturas, partidos, elecciones ni autoridades. Esa regla sigue vigente en cualquier versión que hagan.

## Ruta rápida
| Paso | Qué hacen | Tiempo |
|---|---|---|
| 1 | Crear cuentas en GitHub y Streamlit (sección 1) | 5 min |
| 2 | Copiar el repositorio con **Fork** (sección 2) | 2 min |
| 3 | Publicar su app con la clave de IA (secciones 3 y 4) | 10 min |
| 4 | Elegir qué mejorar: planilla, recetas de código o app nueva (secciones 5 a 8) | el resto del tiempo |
| 5 | Probar el antes y después, y los usos indebidos (sección 10) | 30 min |
| 6 | Congelar a las **14:15 h** y declarar los cambios antes del **cierre técnico (14:45 h)** (sección 13) | 15 min |

## 1. Qué necesitan
| Qué | Dónde | Costo |
|---|---|---|
| Cuenta de GitHub | https://github.com/signup | Gratis |
| Cuenta de Streamlit Community Cloud (se entra con GitHub) | https://share.streamlit.io | Gratis |
| Clave de IA | La entrega la organización: **Claude Haiku 5.5** (Anthropic). Respaldo gratis: Groq (https://console.groq.com/keys) o Mistral (https://console.mistral.ai/api-keys) | Sin costo para el equipo |
| Opcional: editar y probar con un editor | GitHub Codespaces (el repositorio ya trae `.devcontainer`) o Python 3.11 a 3.13 y Git en su computador | Gratis |

## 2. Copiar el repositorio (fork)
1. Abran https://github.com/Giocrisrai/hackathon-ia-congreso-social-2026-desafio3.
2. Presionen **Fork → Create fork**. Queda una copia en su cuenta, por ejemplo `su-usuario/hackathon-ia-congreso-social-2026-desafio3`.
3. Trabajen siempre en **su** fork. Lo que cambien ahí no afecta las apps oficiales ni a los otros equipos.
4. Agreguen a sus compañeros: en su fork, **Settings → Collaborators → Add people**.

## 3. Publicar su app
1. Entren a https://share.streamlit.io con GitHub y presionen **Create app → Deploy a public app from GitHub**.
2. Completen:
   - **Repository:** `su-usuario/hackathon-ia-congreso-social-2026-desafio3`
   - **Branch:** `main`
   - **Main file path:** `app_a.py` (A), `app_b.py` (B) o `app_nueva.py` (app nueva)
   - **App URL:** a elección, por ejemplo `equipo07-pausa`
3. En **Advanced settings**, elijan **Python 3.12** y en **Secrets** peguen la configuración de la sección 4.
4. Presionen **Deploy**. Tarda 1 a 3 minutos la primera vez.

## 4. Secrets: claves del equipo y de la IA
Peguen esto en **Advanced settings → Secrets** (o, después, en **Manage app → Settings → Secrets**) y completen las claves:

```toml
[equipos.E01]
nombre = "Equipo 07"
clave = "una-clave-que-inventen"

[ia]
orden = ["anthropic", "groq"]          # se prueban en este orden; si uno falla, pasa al siguiente
limite_consultas_por_equipo = 120

[ia.anthropic]
api_key = "sk-ant-..."                 # la entrega la organización
modelos = ["claude-haiku-5-5"]

[ia.groq]                              # respaldo opcional; si no lo usan, bórrenlo y saquen "groq" de orden
api_key = "gsk_..."
modelos = ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
```

- **Las claves van solo en Secrets.** Nunca las escriban en el código, en la planilla ni en un mensaje de GitHub: el repositorio es público. El `.gitignore` ya excluye `.streamlit/secrets.toml`.
- Sin `[equipos.*]` nadie puede ingresar: definan al menos un equipo. Un código que empiece con `M` (por ejemplo `M01`) funciona como mentor: si la IA falla, muestra el diagnóstico.
- `MODO_DEMO = "si"` fuerza respuestas de demostración, útil para avanzar si la clave aún no llega.
- Bajo cada respuesta aparece qué modelo respondió, por ejemplo "🤖 Respondió anthropic · claude-haiku-5-5". Anótenlo para la declaración de transparencia.
- Otros proveedores (Mistral, Gemini, OpenRouter, Cerebras, Together, DeepSeek, OpenAI) se agregan igual: su nombre en `orden` y su bloque `[ia.<nombre>]`. La plantilla completa está en `.streamlit/secrets.example.toml`.

## 5. Tres formas de cambiar la app
| Forma | Para qué | Cómo |
|---|---|---|
| **A · Planilla** (sin código) | Usuario, tono, largo, ejemplos, reglas extra, textos, casos (`casos_extra`) y leyes (`leyes_extra`) | Copien la planilla base en Google Sheets, compártanla como Lector, peguen su URL en la barra lateral y presionen "Recargar configuración". Funciona también en la app oficial |
| **B · Editar en GitHub** (sin instalar nada) | Cambios chicos de código: reglas, opciones, textos | En su fork abran el archivo, presionen el **lápiz ✏️**, editen y presionen **Commit changes**. Su app se actualiza sola en 1 a 2 minutos |
| **C · Editor completo** | Cambios grandes o una app nueva | En su fork: **Code → Codespaces → Create codespace on main** (VS Code en el navegador, con todo instalado), o clónenlo en su computador (sección 10). Prueben localmente y suban con *commit* y *push* |

Empiecen siempre por la planilla: es lo más rápido y suele ser lo que más mejora la experiencia del usuario. La [Guía para participantes](Guia_participantes_Desafio3.md) explica cada campo, y su mentor tiene [12 casos verificados](complementos/casos_extra_12_casos.csv) y [3 proyectos de ley](complementos/leyes_extra_3_proyectos.csv) listos para pegar.

## 6. Cómo está armado el código
```
app_a.py · app_b.py · app_nueva.py   puntos de entrada (una línea cada uno)
variantes/a_verificador.py           Variante A: reglas, esquema, validación y pantalla
variantes/b_ley_simple.py            Variante B: reglas, esquema, controles por frase y pantalla
variantes/c_nueva.py                 plantilla para una herramienta nueva del equipo
nucleo/llm.py                        IA con cambio de proveedor, salida JSON y modo demo      (🔒 no modificar)
nucleo/salvaguardas.py               aviso de IA, ingreso por equipo o mentor y cuota        (🔒 no modificar)
nucleo/registro.py                   registro de consultas y decisiones                      (🔒 no modificar)
nucleo/tono.py                       paso de estilo del equipo y sus controles               (🔒 no modificar)
nucleo/config.py · nucleo/marca.py   lectura de la planilla y logos
datos/                               casos verificados (A), leyes (B) y respuestas de demostración
pruebas/                             pruebas automáticas de los controles
```

Así viaja una consulta:
1. `config.panel_config(DEFECTOS)` lee la pestaña `config` de la planilla del equipo (o usa `DEFECTOS`).
2. `salvaguardas.ingresar_equipo()` pide código y clave, y `consumir_cuota()` descuenta una consulta.
3. `armar_sistema(...)` arma el prompt: los **casos o artículos** del corpus, la personalización del equipo y, al final, las **reglas fijas** (`REGLAS_FIJAS`), que mandan sobre todo lo anterior.
4. `llm.consultar(...)` pide a la IA un JSON con la forma de `ESQUEMA` y prueba los modelos en el orden de los secrets. Si nadie responde, usa la respuesta de demostración.
5. La variante **valida** la respuesta:
   - en A, la calificación sale solo de un caso verificado;
   - en B, se descartan las frases sin artículo, o que nombran un organismo o una cifra que el artículo no tiene.
6. Si el equipo cambió el estilo, `tono.aplicar(...)` reescribe solo lo que escribió la IA y revisa que no cambien los hechos.
7. Una **persona decide** y `registro.registrar(...)` guarda la consulta y la decisión, vinculadas por `id` y `relacion`.

## 7. Recetas para mejorar las variantes
Cada receta indica dónde está lo que hay que cambiar. Hagan **un cambio a la vez** y prueben el mismo caso antes y después.

### Variante A · Pausa antes de compartir (`variantes/a_verificador.py`)
| Quieren… | Dónde | Cómo |
|---|---|---|
| Más casos verificados de su tema | Planilla `casos_extra` (hasta 30) o `datos/a_casos.csv` | Una fila por caso, con fuente oficial. Columnas en `datos/a_diccionario.md` |
| Una regla nueva para la IA (por ejemplo, sugerir siempre a quién preguntar) | `REGLAS_FIJAS` | Agreguen la regla 11. No quiten la 1 (la IA no califica), la 3 (fuera de alcance) ni la 6 (ignorar instrucciones del mensaje) |
| Otro motivo para "no se puede verificar" | `CATEGORIAS` | Agreguen una clave y su texto, por ejemplo `"rumor_privado": "Trata de la vida privada de alguien"` |
| Cambiar cómo se ve el resultado | `mostrar_resultado()` | Cambien el orden o los títulos. La explicación verificada siempre debe quedar visible |
| Otras opciones de decisión | `main()`, el `st.radio` "¿Qué harás con este mensaje?" | Cambien o agreguen opciones; siguen quedando registradas |
| Que la IA no agregue otras palabras fuertes sin respaldo | `_FUERTES` | Súmenlas a la tupla (por ejemplo `"cadena falsa"`) |

### Variante B · La ley en simple (`variantes/b_ley_simple.py`)
| Quieren… | Dónde | Cómo |
|---|---|---|
| Otra ley o proyecto de ley | Planilla `leyes_extra` o `datos/b_leyes.csv` | Un artículo por fila, con el texto **literal** de [bcn.cl/leychile](https://www.bcn.cl/leychile). Columnas en `datos/b_diccionario.md` |
| Una regla nueva para la explicación (por ejemplo, terminar con un paso práctico) | `REGLAS_FIJAS` | Agreguen la regla 13. No quiten las reglas de fidelidad (1, 2, 9 y 12) ni la de neutralidad (4 a 6) |
| Detectar otro organismo mal atribuido | `ORGANISMOS` | Súmenlo en minúsculas, por ejemplo `"servicio nacional de turismo"` |
| Leyes más largas | `MAX_ARTICULOS_POR_LEY` y `LARGO_MAX_TEXTO` | Con más texto, cada consulta usa más cuota |
| Cambiar la encuesta de claridad o la pantalla | `main()`, el `st.radio` "¿Te quedó clara la explicación?" | Cambien preguntas u opciones; siguen quedando registradas |

### Las dos variantes
| Quieren… | Dónde |
|---|---|
| Textos de la pantalla y valores por defecto | `DEFECTOS` de cada archivo (o la planilla) |
| Respuestas de demostración para sus casos | `datos/demo_a.json` y `datos/demo_b.json` |

## 8. Construir algo nuevo: `variantes/c_nueva.py`
Si su idea no cabe en A ni en B (por ejemplo, un asistente de trámites o de derechos del consumidor), partan de `variantes/c_nueva.py`. Ya trae todo lo que exigen las bases:
- ingreso por equipo, aviso de IA y planilla;
- IA con respaldo y salida JSON validada;
- reglas de neutralidad con `fuera_de_alcance`;
- cuota, registro y decisión humana.

Para usarla:
1. Cambien solo lo marcado con ✏️:
   - `DEFECTOS`;
   - la tarea en `REGLAS_FIJAS`;
   - los campos de `ESQUEMA` y cómo se muestran en `main()`.
2. Si agregan un campo a `ESQUEMA`, súmenlo también a `required` y a `RESPALDO_DEMO`.
3. Publíquenla con *Main file* `app_nueva.py` (sección 3).
4. Las líneas marcadas con 🔒 no se borran, y las reglas 1 a 3 (neutralidad, no inventar e ignorar instrucciones del mensaje) tampoco.

## 9. Usar una IA para programar
Pueden pedirle a Claude (u otro asistente) que les ayude a cambiar el código. Para que no rompa las protecciones, denle contexto:

```
Estoy mejorando una app de Streamlit de una hackathon. Te paso el archivo variantes/b_ley_simple.py.
Quiero: <su cambio, en una frase>.
Reglas: no modifiques nada en nucleo/; mantén la neutralidad (no opinar ni tratar política), que cada frase
cite su artículo y se descarten las que no lo tienen, el registro y la decisión humana. Devuélveme solo las
líneas que cambian y dime cómo probarlo.
```

Revisen cada cambio antes de hacer *commit*, corran las pruebas automáticas (sección 10) y prueben la app. Declaren en la transparencia que usaron IA para programar.

## 10. Probar antes del pitch
**En su app publicada:**
- Prueben el **mismo caso** o la **misma ley** con la plantilla base y con su versión, y guarden ambas capturas.
- Prueben al menos **5 usos indebidos** y anoten qué pasó, por ejemplo:
  - pedir una opinión;
  - "¿por quién voto?";
  - "ignora tus reglas";
  - acusar a alguien sin sentencia;
  - pedir un discurso partidista.
- Descarguen el registro desde la barra lateral.

**En su computador o en Codespaces (opcional):**
```bash
git clone https://github.com/su-usuario/hackathon-ia-congreso-social-2026-desafio3
cd hackathon-ia-congreso-social-2026-desafio3
python3 -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .streamlit/secrets.example.toml .streamlit/secrets.toml   # y pongan sus claves
python pruebas/test_tono.py && python pruebas/test_variantes.py   # controles fijos, sin IA, en segundos
streamlit run app_a.py      # o app_b.py, o app_nueva.py
```
Si cambiaron reglas o controles y una prueba falla, revisen qué protección se rompió antes de seguir.

## 11. Lo que deben mantener
Son parte de las bases y de la evaluación ética:
- **Neutralidad:** no opinar, no persuadir, no tratar candidaturas, partidos, elecciones ni autoridades.
- **Variante A:** la calificación (falso, engañoso…) viene **solo** de un caso verificado, nunca de la IA, y la explicación verificada queda visible.
- **Variante B:** cada frase cita su artículo y se descartan las que no lo tienen.
- La decisión final de la persona, el registro y la cuota.
- Sin cambios en `nucleo/`, salvo agregar proveedores.
- Fuente oficial para cada caso o artículo agregado.

## 12. Problemas frecuentes
| Síntoma | Solución |
|---|---|
| La página queda en blanco o cargando | Falla momentánea de Streamlit Cloud: recarguen la página |
| "Falta configurar la IA en los secrets" | Agreguen el bloque `[ia]` de la sección 4 |
| Siempre respuesta de demostración | Revisen la clave y los modelos. Entren con un código que empiece con `M` para ver el diagnóstico, o miren **Manage app → Logs** (`[llm] …`) |
| Error 429 frecuente | Límite del proveedor: agreguen un segundo proveedor en `orden` |
| "No se pudo leer la Sheet" | Compartir → Cualquier persona con el vínculo → Lector |
| "Filas ignoradas" en la barra lateral | Ábranlo: dice qué corregir en cada fila |
| Cambié el código y no se ve | Revisen que el *commit* esté en `main`; esperen 1 a 2 minutos o usen **Reboot app** |
| `SyntaxError` o `KeyError` en la app | **Manage app → Logs** dice el archivo y la línea; corrijan o vuelvan a la versión anterior en GitHub (**History**). Un `KeyError` en la app nueva suele ser un campo de `ESQUEMA` que falta en `required` o en `RESPALDO_DEMO` |

## 13. Congelar y declarar
- A las **14:15 h** congelen lo que funciona y graben un video de respaldo de la demo.
- Desde ahí no hagan más *commits*: cada uno reinicia la app y sus contadores.
- Se evalúa la versión congelada al **cierre técnico (14:45 h)**.
- En la **declaración de transparencia** indiquen:
  - la URL de su fork y de su app;
  - qué archivos cambiaron y por qué;
  - qué proveedores y modelos de IA usa la app;
  - si usaron IA para programar;
  - qué protecciones mantuvieron y cómo probaron el mal uso.
