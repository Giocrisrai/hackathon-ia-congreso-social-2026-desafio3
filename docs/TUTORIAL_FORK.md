# Tutorial · Tu propia versión de las apps del Desafío 3

Para un equipo que quiere ir más allá de la planilla: copiar el repositorio (fork), desplegar **su propia app** y cambiar el código. Sirve para las dos variantes. Tiempo: 20 a 30 minutos, sin experiencia previa en despliegues.

> **Antes de empezar.** En la competencia se evalúa la mejora sobre la plantilla oficial. Un fork es válido si lo declaran en la **declaración de transparencia** y mantienen las protecciones de la sección 6. Confírmenlo con su mentor.

| Variante | App oficial | Main file | Lógica | Datos | Pestaña extra |
|---|---|---|---|---|---|
| A · Pausa antes de compartir | https://hackaton-d3-pausa.streamlit.app | `app_a.py` | `variantes/a_verificador.py` | `datos/a_casos.csv` | `casos_extra` |
| B · La ley en simple | https://hackaton-d3-ley.streamlit.app | `app_b.py` | `variantes/b_ley_simple.py` | `datos/b_leyes.csv` | `leyes_extra` |

## 1. Qué necesitan
| Qué | Dónde | Costo |
|---|---|---|
| Cuenta de GitHub | https://github.com/signup | Gratis |
| Cuenta de Streamlit Community Cloud (se entra con GitHub) | https://share.streamlit.io | Gratis |
| Una clave de IA compatible con OpenAI | Groq: https://console.groq.com/keys · Mistral: https://console.mistral.ai/api-keys | Gratis con límites |
| Opcional: probar en su computador | Python 3.11 a 3.13 y Git, o GitHub Codespaces (el repo trae `.devcontainer`) | Gratis |

## 2. Hacer el fork
1. Abran https://github.com/Giocrisrai/hackathon-ia-congreso-social-2026-desafio3.
2. Presionen **Fork → Create fork**. Sus cambios no afectan las apps oficiales.

## 3. Desplegar su app
1. En https://share.streamlit.io presionen **Create app → Deploy a public app from GitHub**.
2. Repository: `su-usuario/hackathon-ia-congreso-social-2026-desafio3` · Branch: `main` · Main file path: `app_a.py` (A) o `app_b.py` (B) · App URL a elección, por ejemplo `equipo07-pausa`.
3. En **Advanced settings** elijan **Python 3.12** y peguen los secrets de la sección 4.
4. **Deploy**. Tarda 1 a 3 minutos la primera vez.

## 4. Secrets mínimos
```toml
[equipos.E01]
nombre = "Equipo 07"
clave = "una-clave-que-inventen"

[ia]
orden = ["groq"]
limite_consultas_por_equipo = 120

[ia.groq]
api_key = "gsk_..."
modelos = ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
```

- Para sumar un respaldo, agreguen su nombre a `orden` y su bloque (`[ia.mistral]`, `[ia.gemini]`, `[ia.cerebras]`…). Si uno falla o se satura, la app pasa al siguiente. La plantilla completa está en `.streamlit/secrets.example.toml`.
- El formato del repositorio original también funciona: `OPENAI_API_KEY`, `MODELO` y, para Groq, `OPENAI_BASE_URL = "https://api.groq.com/openai/v1"`.
- `MODO_DEMO = "si"` fuerza respuestas de demostración (contingencia sin IA). `REGISTRO_FORM_URL` envía el registro a un Google Form; sin él, el registro se descarga desde la barra lateral.
- **Nunca suban `.streamlit/secrets.toml` a GitHub.** El `.gitignore` ya lo excluye.

**Ojo con los límites:** el plan gratis de Groq permite unos 8.000 tokens por minuto con `gpt-oss-120b` y cada consulta usa unos 3.000, así que admite pocas consultas por minuto. Para un equipo que prueba está bien.

## 5. Probar en su computador (opcional)
```bash
git clone https://github.com/su-usuario/hackathon-ia-congreso-social-2026-desafio3
cd hackathon-ia-congreso-social-2026-desafio3
python3 -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .streamlit/secrets.example.toml .streamlit/secrets.toml   # y pongan su clave
streamlit run app_a.py      # Variante A
streamlit run app_b.py      # Variante B
```

## 6. Qué pueden cambiar y qué deben mantener
| Quieren cambiar | Dónde |
|---|---|
| Usuario, tono, ejemplos, textos | (sin código) pestaña `config` de su copia de la planilla |
| Casos verificados base (A) | `datos/a_casos.csv` (diccionario en `datos/a_diccionario.md`) |
| Leyes base (B) | `datos/b_leyes.csv` (diccionario en `datos/b_diccionario.md`), texto literal de bcn.cl/leychile |
| Respuestas de demostración | `datos/demo_a.json`, `datos/demo_b.json` |
| Reglas del prompt y esquema de respuesta (A) | `variantes/a_verificador.py`: `REGLAS_FIJAS`, `armar_sistema()` y `ESQUEMA` |
| Reglas, esquema y descarte de frases sin artículo (B) | `variantes/b_ley_simple.py` |
| Pantalla, textos por defecto | `DEFECTOS` y `main()` de cada archivo en `variantes/` |
| Proveedores de IA conocidos | `PROVEEDORES` en `nucleo/llm.py` (normalmente basta con los secrets) |
| Lectura de la planilla | `nucleo/config.py` |

**No modifiquen, o mantengan equivalente:** `nucleo/salvaguardas.py` (aviso de IA, ingreso por equipo, cuota), `nucleo/registro.py` (registro de consultas) y `nucleo/llm.py` (salida estructurada, cambio de proveedor, modo demo). Deben mantener además:
- La neutralidad: no opinar, no persuadir, no analizar candidaturas, partidos, elecciones ni autoridades.
- En A, que la calificación (falso, engañoso…) venga **solo** de un caso verificado, nunca de la IA.
- En B, que cada frase cite su artículo y se descarten las que no lo tienen.
- La decisión final de la persona y el registro.

## 7. Problemas frecuentes
| Síntoma | Solución |
|---|---|
| "Falta configurar la IA en los secrets" | Agreguen el bloque `[ia]` de la sección 4 |
| Siempre respuesta de demostración | Revisen la clave y los modelos. Entren con un código que empiece con `M` para ver el diagnóstico, o miren **Manage app → Logs** (`[llm] …`) |
| Error 429 frecuente | Límite del plan gratis: agreguen un segundo proveedor o modelo |
| Con Groq: `model_not_found` | Usen `openai/gpt-oss-120b` u `openai/gpt-oss-20b` |
| "No se pudo leer la Sheet" | Compartir → Cualquier persona con el vínculo → Lector |
| Cambié el código y no se ve | Hagan *commit* en `main`; la app se actualiza sola en 1 a 2 minutos o con **Reboot app** |

## 8. Qué declarar en la transparencia
URL del fork y de la app, archivos cambiados y por qué, proveedores y modelos de IA, qué protecciones mantuvieron y cómo probaron el mal uso.
