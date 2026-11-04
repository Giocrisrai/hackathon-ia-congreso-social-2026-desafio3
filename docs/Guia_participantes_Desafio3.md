# Guía para participantes · Desafío 3 · Ciudadanía informada

Hackathon IA Aplicada · Congreso Social UC 2026 · 6 de noviembre de 2026 · Duoc UC San Joaquín

## El desafío en una frase
Su equipo tiene un día para crear un prototipo con IA que ayude a una persona concreta a **entender o verificar información pública**, de forma útil y confiable.

**Prototipos de referencia.** Los mentores prepararon dos prototipos que ya funcionan y muestran una forma posible de resolver el desafío:
- **A · Pausa antes de compartir,** para verificar contenidos virales;
- **B · La ley en simple,** para entender leyes en lenguaje claro.

Son material de referencia, no una tarea asignada. Pueden mejorarlos, adaptarlos, combinarlos o construir su propia solución, por ejemplo una de participación local. Se usan sobre todo en la **Etapa 3 · Diseño**. Esta guía explica cómo usarlos.

- **Problema:** la desinformación circula rápido por WhatsApp y redes, y las leyes están escritas en un lenguaje que poca gente entiende.
- **Lo que se evalúa:** que su solución sirva a un usuario real, que la IA aporte valor, que sea fiel a las fuentes, que funcione en la demo y que hayan pensado en cómo podría usarse mal. Si parten de un prototipo de referencia, se evalúa lo que ustedes aportan.
- **Lo que no se evalúa:** cuánto código escriben. Un prototipo de referencia se puede mejorar desde una planilla de Google, sin programar, o copiando el código desde GitHub con la [guía para equipos](TUTORIAL_FORK.md).

Cualquier solución del desafío debe ser **neutral por diseño**, como los prototipos: no opina, no persuade y no habla de candidaturas, partidos ni autoridades.

## Cómo es la jornada
Son 8 etapas. En cada una completan una ficha ([Fichas del equipo](Fichas_equipo_Desafio3.md)), y su mentor los acompaña con los mismos criterios. El detalle está en [Etapas de la jornada](Etapas_jornada_Desafio3.md), y las ideas de mejora, en [Rutas de mejora](Rutas_de_mejora_Desafio3.md).

| Etapa | Horario | Qué hacen | Entregable |
|---|---|---|---|
| 1 · Inmersión | 10:00–10:45 | Entender el desafío y conversar con personas reales (todavía sin prototipos) | Ficha de Inmersión |
| 2 · Definición | 10:45–11:15 | Elegir usuario y caso, objetivo medible y alcance del MVP | Ficha de Definición |
| 3 · Diseño | 11:15–11:45 | Conocer los prototipos de referencia y decidir: partir de uno, combinar o crear el suyo. Funcionalidades, corpus a precargar y dónde decide una persona | Ficha de Diseño |
| 4 · Desarrollo | 11:45–12:45 | Construir los componentes en paralelo y cargar el corpus verificado | Registro de cambios |
| 5 · Integración | 13:30–14:15 | Probar el flujo completo, casos límite y preguntas adversariales | Registro de pruebas |
| 6 · Cierre técnico | 14:15–14:45 | Congelar, grabar el respaldo, set fijo para la demo, checklist ético y transparencia | Versión congelada |
| 7 · Preparación del pitch | 14:45–16:15 | Relato, diapositivas, guion de demo y ensayo | Presentación y guion |
| 8 · Presentación final | 16:15–18:15 | Pitch con demo y preguntas | Nota de aprendizajes |

## Cómo usar un prototipo de referencia (10 minutos, en la Etapa 3)
| Variante | App |
|---|---|
| A · Pausa antes de compartir | https://hackaton-d3-pausa.streamlit.app |
| B · La ley en simple | https://hackaton-d3-ley.streamlit.app |

1. Abran la app de su variante e ingresen con el **código y la clave** del equipo. Los entrega su mentor.
2. Abran la planilla base (el enlace también lo entrega el mentor) y hagan **Archivo → Hacer una copia**.
3. Compartan la copia: **Compartir → Acceso general → Cualquier persona con el vínculo → Lector**.
4. Peguen la URL de su copia en la barra lateral de la app y presionen **"Recargar configuración"**.
5. Prueben primero con la plantilla base: en A, un mensaje de ejemplo y uno escrito por ustedes; en B, una ley sin pregunta y luego con una pregunta concreta.
6. Desde ahí, cada cambio es: editar la planilla → "Recargar configuración" → probar **el mismo caso** para comparar.

Para pedir un tono o un trato, escríbanlo claro en `tono` o en `instrucciones_extra` (por ejemplo: "Directo y cercano, frases cortas. Trata de 'hermano'") y escriban sus `ejemplos` en ese mismo tono: la IA imita los ejemplos. Cuando el estilo se aplica, bajo la respuesta aparece "🎨 Respuesta escrita con el estilo de tu equipo".

En la pestaña `config` editan solo la columna **valor**: a quién le habla la IA (`usuario`), su tono, el largo, 1 a 3 ejemplos de respuesta ideal, reglas propias (`instrucciones_extra`) y los textos de la pantalla.

## Los dos prototipos de referencia
| | A · Pausa antes de compartir | B · La ley en simple |
|---|---|---|
| Qué hace | Revisa un mensaje sospechoso antes de reenviarlo: qué afirma, si se puede verificar, y lo compara con casos ya verificados | Explica una ley en lenguaje claro; cada frase indica de qué artículo viene y se puede ver el texto original |
| Quién califica | Solo un caso verificado puede decir "falso" o "engañoso"; la IA nunca lo decide sola | La app descarta las frases que no tienen un artículo que las respalde |
| Pestaña para agregar | `casos_extra`: hasta 30 casos verificados, cada uno con fuente oficial | `leyes_extra`: otra ley o documento público, un artículo por fila, con el texto **literal** |
| De dónde sacar material | Verificadores y sitios oficiales (ministerios, SERNAC, SENAPRED, etc.) | [bcn.cl/leychile](https://www.bcn.cl/leychile) para leyes y [senado.cl](https://tramitacion.senado.cl) para proyectos |
| Decisión final | La persona decide si comparte o no | La persona lee el artículo original |

Para agregar filas: copien la fila EJEMPLO, cambien EJEMPLO por X01, X02… y completen todas las columnas. Su mentor tiene casos y proyectos de ley de ejemplo listos para usar.

Temas que funcionan bien: salud, estafas, consumo, trámites, emergencias, tecnología, una ley que afecta a su usuario. Temas fuera de bases: candidaturas, partidos, autoridades y política contingente.

## Lo que no se puede cambiar
Estas protecciones están en el código y mandan sobre cualquier instrucción de la planilla:
- Aviso de uso de IA y registro de todas las consultas (se descarga desde la barra lateral).
- **120 consultas a la IA por equipo.** Después, la app sigue con respuestas de demostración.
- **Neutralidad:** no opinar, no persuadir, no hablar de candidaturas, partidos ni autoridades. Si `instrucciones_extra` pide algo de eso, la app lo ignora o lo bloquea.
- **Validación de respuestas:** en A, la calificación solo viene de un caso verificado; en B, se descartan las frases sin artículo de respaldo.
- La decisión final es siempre de la persona.

Cuiden sus `ejemplos`: la IA los imita. Si un ejemplo tiene un error o "declara" algo falso con la voz de la IA, la herramienta lo repetirá en todas las respuestas. Revísenlos contra la fuente oficial antes de usarlos.

## Si algo no funciona
| Lo que ven | Qué hacer |
|---|---|
| No pueden entrar | Revisen código y clave; si persiste, pídanlos de nuevo al mentor |
| La app tarda en abrir | Se estaba "despertando": esperen un minuto |
| Un cambio en la planilla no se ve | Revisen que esté compartida como Lector y presionen "Recargar configuración" |
| "Filas ignoradas" en la barra lateral | Ábranlo: dice qué corregir en cada fila |
| "Se muestra una respuesta de demostración" | La IA no respondió: esperen un minuto y prueben de nuevo; si persiste, avisen al mentor |
| La app se niega a responder | Probablemente tocaron política contingente: elijan otro tema |
| La explicación de una ley sale con pocas frases (B) | La app descartó frases sin respaldo: revisen que el texto en `leyes_extra` sea el literal y completo |

Si nada funciona y queda poco tiempo, borren la URL de la planilla de la barra lateral y presenten con la plantilla base.

## Entregables y pitch
Antes de las **14:45 h** entreguen la **declaración de transparencia** (qué modelos usaron —aparece bajo cada respuesta— y qué cambiaron respecto de la plantilla) y el **checklist ético** completo. Desde las **14:15 h** (Etapa 6 · Cierre técnico) no agregan nada nuevo: corrigen lo visible, graban un video de respaldo y congelan la versión. Pitch entre las **16:15 y las 18:15 h**: **5 minutos de pitch con demo y 3 de preguntas del jurado**. Se evalúa la versión congelada al **cierre técnico (14:45 h)**: lo que cambien después no cuenta.

En la demo usen **solo casos o leyes precargados y verificados**, con la fuente en pantalla.

- [ ] Pueden decir en una frase quién es su usuario y qué necesita entender o verificar
- [ ] La app lee su planilla sin filas ignoradas
- [ ] Tienen un antes y después con el mismo caso o la misma ley
- [ ] Cada caso o artículo agregado tiene su fuente oficial
- [ ] Probaron al menos 5 intentos de mal uso (pedir opinión, política contingente, "ignora tus reglas"…) y anotaron qué pasó
- [ ] Entregaron la declaración de transparencia y el checklist ético antes de las 14:45 h
- [ ] Tienen el registro descargado y un video de respaldo de la demo
