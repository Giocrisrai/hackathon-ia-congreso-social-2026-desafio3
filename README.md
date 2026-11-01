# Hackathon IA Aplicada · Congreso Social UC 2026 · Desafío 3 · Ciudadanía informada

Plantillas del Desafío 3, creadas por **Guillermo Pinto** ([repositorio original](https://github.com/gpintofuentes/HACKATON-D3)). Esta versión suma el mismo sistema de las plantillas del Desafío 2: IA con varios proveedores y cambio automático, códigos de mentor, registro descargable y documentación para equipos y mentores. Las reglas y la lógica de cada variante son las del repositorio original.

Cada equipo recibe una app que **ya funciona** y la adapta a un usuario real desde una planilla de Google, sin programar: código y clave por equipo, pestaña `config`, pestaña de extras con fila EJEMPLO, botón "Recargar configuración" y 120 consultas a la IA por equipo.

| Variante | App en línea | Qué hace |
|---|---|---|
| A · Pausa antes de compartir | https://hackaton-d3-pausa.streamlit.app | Revisa un mensaje sospechoso: qué afirma, si se puede verificar y si coincide con un caso verificado. La calificación viene **solo** del caso, nunca de la IA |
| B · La ley en simple | https://hackaton-d3-ley.streamlit.app | Explica una ley en lenguaje claro; cada frase cita su artículo y se descartan las que no lo tienen |

## Documentación
| Para | Documento |
|---|---|
| Participantes | [Guía para participantes](docs/Guia_participantes_Desafio3.md) |
| Mentores | [Guía para mentores](docs/Guia_mentores_Desafio3.md) · [Riesgos éticos](docs/Riesgos_eticos_Desafio3.md) · [Prueba piloto](docs/Prueba_piloto_Desafio3.md) |
| Material extra | [12 casos verificados para `casos_extra`](docs/complementos/casos_extra_12_casos.csv) · [3 proyectos de ley para `leyes_extra`](docs/complementos/leyes_extra_3_proyectos.csv) · [fuentes](docs/proyectos_ley_FUENTES.md) |
| Pruebas de mentores | [Plan de pruebas de las 4 apps (D2 y D3)](docs/Plan_de_pruebas_mentores.xlsx) |
| Quien quiera su propia versión | [Tutorial: fork, despliegue y cambios por variante](docs/TUTORIAL_FORK.md) |

## Estructura
```
app_a.py · app_b.py          puntos de entrada de cada variante
variantes/a_verificador.py   Variante A: reglas, esquema de respuesta y pantalla
variantes/b_ley_simple.py    Variante B: reglas, esquema, descarte de frases sin artículo y pantalla
nucleo/llm.py                IA multi-proveedor, salida JSON estructurada y modo demo      (no modificar)
nucleo/salvaguardas.py       aviso de IA, ingreso por equipo o mentor y cuota            (no modificar)
nucleo/registro.py           registro en la app y, opcional, en un Google Form            (no modificar)
nucleo/config.py             lectura de la planilla del equipo
datos/                       casos verificados (A), leyes (B), respuestas de demostración
docs/                        documentación del desafío
.streamlit/                  plantilla de secrets (secrets.toml nunca se sube)
```

## IA con varios proveedores
La app prueba los proveedores en el orden de `[ia] orden` y, dentro de cada uno, los modelos de su lista `modelos`. Si un modelo falla o se satura, pasa al siguiente sin que el equipo lo note: los saturados se saltan 45 s y los que tienen clave o nombre inválido, 10 min. Si todos fallan, muestra una respuesta de demostración y la app sigue funcionando. Bajo cada respuesta se indica qué modelo respondió, y la barra lateral muestra la cadena en uso.

| Orden por defecto | Modelos |
|---|---|
| Groq | `openai/gpt-oss-120b` → `openai/gpt-oss-20b` |
| Mistral | `mistral-small-latest` → `ministral-8b-latest` |

Para sumar otra clave no hay que tocar código: se agrega al final de `orden` y se crea su bloque `[ia.<nombre>]` con `api_key` y `modelos`. Gemini, OpenRouter, Cerebras, Together, DeepSeek y OpenAI ya traen su dirección; otro proveedor compatible con OpenAI necesita además `url`. El formato anterior (`OPENAI_API_KEY`, `MODELO` y, opcional, `OPENAI_BASE_URL`) sigue funcionando.

## Protecciones fijas (no se cambian desde la planilla)
- Aviso de uso de IA, registro de consultas y decisiones, límite de consultas por equipo.
- Neutralidad: no opinar, no persuadir, no analizar candidaturas, partidos, elecciones ni autoridades. Una estafa o un trámite que solo menciona al gobierno sí se analiza.
- A: la calificación (falso, engañoso…) viene solo de un caso verificado del corpus.
- B: cada frase cita su artículo y se descartan las que no lo tienen.
- La decisión final es de la persona y queda registrada.

## Despliegue (organización)
1. En https://share.streamlit.io, crear dos apps desde este repositorio, rama `main`, Python 3.12, con *Main file* `app_a.py` y `app_b.py`.
2. En cada app, **Settings → Secrets**: pegar `.streamlit/secrets.example.toml` con las claves de IA, un bloque `[equipos.EXX]` (nombre y clave) por equipo y uno `[equipos.MXX]` por mentor. Los códigos `MXX` tienen cuota propia y, si la IA falla, ven el diagnóstico.
3. Entregar a cada equipo su código y clave y el enlace a la planilla base de su variante.
4. Las apps se duermen sin visitas. La tarea [Mantener apps despiertas](https://github.com/Giocrisrai/hackathon-ia-congreso-social-2026-desafio2/actions/workflows/mantener_apps_despiertas.yml) (GitHub Actions, en el repositorio del D2) visita las 4 apps cada 4 horas y las despierta; igual conviene abrirlas antes de cada jornada. No subir cambios a `main` durante la jornada: cada cambio reinicia la app y reinicia los contadores de consultas. El registro queda en la memoria de la app (se descarga desde la barra lateral) y, si se configura `REGISTRO_FORM_URL`, también en el Google Form.

## Pruebas realizadas (30 de octubre de 2026, IA real)
- A: caso de salud y estafa del "bono del Gobierno" respondidos como **Falso** desde el caso verificado; mensaje vacío avisa; pregunta política bloqueada.
- B: Ley 21.100 explicada artículo por artículo; "¿quién me pone la multa?" responde el juzgado de policía local (art. 5); "¿qué opinas del gobierno?" queda fuera de alcance.
- Mal uso: inyección de instrucciones, voto, ataque a un candidato, opinión, acusación sin sentencia y pedido de discurso partidista bloqueados o tratados como no verificables; estafa del SII → Falso. Los 12 casos y 3 proyectos de ley de `docs/complementos` pasan los validadores de la app.
- Cambio de proveedor en 4 escenarios: normal, Groq con clave inválida (respondió Mistral), formato antiguo de secrets y todos caídos (demostración más diagnóstico para mentores). Ingreso de mentor y clave incorrecta.

## Licencia
MIT. Plantillas originales © 2026 Guillermo Pinto (gpintofuentes). Ver [LICENSE](LICENSE).
