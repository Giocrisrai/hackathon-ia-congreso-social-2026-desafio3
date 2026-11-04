# Etapas de la jornada · Desafío 3 · Ciudadanía informada

Hackathon IA Aplicada · Congreso Social UC 2026 · 6 de noviembre de 2026 · Duoc UC San Joaquín

Este documento baja al Desafío 3 las **8 etapas de las bases y de las guías oficiales del mentor**: mismos nombres, tiempos, actividades, entregables y criterios de observación. Agrega lo propio del desafío y cómo se usan los prototipos de referencia.

## Cómo se trabaja
Cada equipo de 5 integrantes desarrolla **su propio prototipo funcional (MVP) apoyado por IA** para el desafío. La IA debe aportar valor real, y debe haber un punto de decisión humana explícito.

**Los mentores prepararon dos prototipos de referencia del Desafío 3.** Muestran una forma posible de resolverlo, con IA y con las protecciones del desafío ya funcionando:

| Prototipo de referencia | Qué hace | App |
|---|---|---|
| A · Pausa antes de compartir | Revisa un mensaje sospechoso; la calificación sale solo de un caso verificado | https://hackaton-d3-pausa.streamlit.app |
| B · La ley en simple | Explica una ley en lenguaje claro, frase por frase con su artículo | https://hackaton-d3-ley.streamlit.app |

Son **material de referencia**, no una tarea asignada. Cada equipo puede:
1. **Usar uno como base y mejorarlo:** desde la planilla, sin programar, o copiando el código desde GitHub con la [guía para equipos](TUTORIAL_FORK.md).
2. **Adaptarlo o combinar ideas** de los dos.
3. **Construir su propia solución,** con la plantilla de app nueva (`app_nueva.py`) o con las herramientas que dominen. Por ejemplo, la tercera línea de las bases: participación local.

Los prototipos se usan sobre todo en la **Etapa 3 · Diseño**. En las etapas 1 y 2 el foco es el desafío y la persona, no el prototipo. Las fichas de cada etapa están en [Fichas del equipo](Fichas_equipo_Desafio3.md) y hay ideas de mejora en [Rutas de mejora](Rutas_de_mejora_Desafio3.md).

**Regla de las bases para la demo:**
- solo documentos públicos precargados y verificados por el equipo, con la fuente oficial en pantalla;
- nada de consultas abiertas de actualidad política, candidaturas, partidos ni personas en cargos públicos.

**IA durante el evento.** La organización entrega una clave de la API de Claude (Anthropic) y comunica el día del evento qué modelo usar. Los prototipos de referencia ya están preparados para esa clave.

| Etapa | Horario | Enfoque | Entregable |
|---|---|---|---|
| 1 · Inmersión | 10:00–10:45 (45 min) | Design Thinking: Empatizar · IA Responsable | Ficha de Inmersión |
| 2 · Definición | 10:45–11:15 (30 min) | Design Thinking: Definir · Lean Startup | Ficha de Definición |
| 3 · Diseño | 11:15–11:45 (30 min) | Design Sprint: Esbozar y decidir · IA Responsable | Ficha de Diseño |
| 4 · Desarrollo | 11:45–12:45 (60 min) | Lean Startup: Construir · IA Responsable | Componentes principales funcionando y guardados, con registro de cambios |
| 5 · Integración | 13:30–14:15 (45 min) | Design Sprint: Prototipar y probar · Lean · IA Responsable | Prototipo integrado de punta a punta, con registro de pruebas y fallas |
| 6 · Cierre técnico | 14:15–14:45 (30 min) | Lean Startup: Medir y aprender · IA Responsable | Versión congelada, checklist ético, declaración de transparencia y set fijo para la demo |
| 7 · Preparación del pitch | 14:45–16:15 (90 min) | Design Sprint: Contar la historia · IA Responsable | Presentación, guion de demo, roles y preguntas anticipadas |
| 8 · Presentación final | 16:15–18:15 (120 min) | Todos los enfoques · IA Responsable | Pitch y demo, más una nota de aprendizajes |

**Checkpoints éticos.** Durante la jornada hay dos checkpoints éticos guiados por Pastoral, y su checklist es requisito de admisibilidad: debe estar completo al cierre técnico (14:45 h). La organización indica cuándo se hacen; las guías sugieren el cierre de la Etapa 2 y la Etapa 5.

---

## Etapa 1 · Inmersión (10:00–10:45, 45 min)
**Objetivo del equipo:** comprender a fondo el desafío antes de proponer soluciones: qué problema existe, a quién afecta y bajo qué límites.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 10 min | Lectura del desafío | Lean el desafío en las bases: contexto, pregunta desafío, usuarios, líneas posibles, datos, restricciones éticas y la nota para la demostración. **Todavía no abren los prototipos de referencia:** primero el problema |
| 15 min | Mapa de actores | Votantes jóvenes, personas mayores en grupos familiares, sociedad civil, municipios, medios locales, colegios (formación ciudadana), verificadores |
| 10 min | Necesidades y restricciones | Datos: Congreso (Cámara y Senado), SERVEL, Consejo para la Transparencia, datos.gob.cl, presupuestos municipales y [bcn.cl/leychile](https://www.bcn.cl/leychile). Restricciones: neutralidad política verificable, trazabilidad de fuentes, nada de contenido persuasivo partidista y mecanismos contra la manipulación |
| 10 min | Síntesis y consenso | Top 3 de necesidades y una frase del desafío con sus palabras |

**Mentor:**
- **Qué observar:** que no salten a la solución, ni a los prototipos, en el minuto 1; que hablen con personas de las fundaciones o con usuarios reales, y que usen fuentes verídicas desde el inicio.
- **IA responsable:** ¿quién queda fuera? Por ejemplo, personas con baja alfabetización digital o que solo usan WhatsApp.
- **Intervenir:** si a los 25 minutos no hay actores definidos.

## Etapa 2 · Definición (10:45–11:15, 30 min)
**Objetivo del equipo:** convertir lo comprendido en una necesidad acotada, un objetivo claro y un alcance realista.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 10 min | Enunciado del problema | «[Actor] necesita [necesidad] porque [razón]». Ejemplos: «Una abuela que recibe cadenas de salud en el grupo familiar necesita saber si reenviarlas porque no sabe cómo verificarlas», o «El dueño de un almacén necesita entender la ley de bolsas plásticas porque lo pueden multar» |
| 10 min | Objetivo medible | Un criterio que se pueda mostrar en la demo. Ejemplos: la persona decide no reenviar un mensaje falso en menos de un minuto, o un estudiante explica la ley con sus palabras después de leerla |
| 10 min | Alcance: sí / no | Qué incluye el prototipo (MVP), qué documentos o casos precargarán para la demo y qué queda fuera. Tienen unas 2,5 h de desarrollo e integración |

**Hipótesis (Lean):** «Creemos que [solución] logrará [resultado] para [actor]. Lo sabremos si [métrica]».

**Mentor:**
- **Señales de alerta:**
  - temas de actualidad política (fuera de bases);
  - objetivos vagos («combatir la desinformación»);
  - un objetivo que ignora el daño de una herramienta que parece neutral pero no lo es.
- **Para el checkpoint ético:** ¿qué resultado no deseado podría tener su objetivo?

## Etapa 3 · Diseño (11:15–11:45, 30 min)
**Objetivo del equipo:** planificar cómo se construirá la solución: qué hará, con qué tecnologías, cómo se conectan sus partes y cómo la usará la persona. **Aquí entran los prototipos de referencia:** los exploran y deciden si parten de uno, si combinan ideas o si construyen su propia solución.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 8 min | Funcionalidades | Recorran los prototipos A y B (con el código de equipo que entrega el mentor) y contrástenlos con su problema: ¿qué les sirve y qué no? Listen las funcionalidades de su MVP (imprescindible / deseable). Hay ideas en las [rutas de mejora](Rutas_de_mejora_Desafio3.md) |
| 8 min | Arquitectura y tecnologías | Diagrama simple: documentos verificados → modelo de IA → controles (que cada respuesta tenga su fuente) → **decisión de una persona** → registro. Decidan con qué lo construyen: prototipo de referencia mejorado (planilla o código), plantilla de app nueva u otras herramientas que dominen. Si parten del código, revisen las secciones 5 a 8 de la [guía para equipos](TUTORIAL_FORK.md) |
| 7 min | Experiencia de usuario | 2 a 4 pasos del usuario real: dónde recibe el mensaje o el documento, qué ve y qué hace con el resultado |
| 7 min | Reparto de trabajo | Responsable por componente y plan de integración. Por ejemplo: corpus verificado (casos o leyes con su fuente), prompts y tono, código o configuración, pruebas y mal uso, pitch |

**Mentor:**
- **IA responsable:** que señalen en el diagrama **dónde decide una persona**, de dónde vienen los documentos y quién los verificó.
- **Señales de alerta:**
  - la IA califica u opina sola;
  - fuentes no oficiales;
  - IA usada solo para "cumplir";
  - copiar el prototipo sin un aporte propio.
- **Intervenir:** si dependen de algo que no existe, como un verificador que no tiene el caso.

## Etapa 4 · Desarrollo (11:45–12:45, 60 min)
**Objetivo del equipo:** construir en paralelo los componentes principales, priorizando lo imprescindible del diseño.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 10 min | Preparación del entorno | **Repositorio compartido:** fork del prototipo de referencia (o su propio repositorio), compañeros como colaboradores, app publicada y la clave de IA de la organización en Secrets ([guía para equipos](TUTORIAL_FORK.md), secciones 1 a 4). Si solo usan la planilla, hagan su copia y compártanla como Lector |
| 35 min | Construcción en paralelo | Cada integrante desarrolla su componente. El corpus se carga verificado: casos con fuente oficial y leyes con el texto **literal** de bcn.cl, un artículo por fila |
| 10 min | Puntos de control | A los 25 y 45 minutos: 2 minutos por integrante, con avance y bloqueos |
| 5 min | Cierre de etapa | Guardar el avance con *commit* (la planilla se guarda sola). Anotar en el registro de cambios qué se hizo y por qué, y lo pendiente para la integración |

**Mentor:**
- **IA responsable:** que verifiquen lo que escribe la IA contra la fuente, y que los ejemplos que le dan a la IA no "declaren" nada falso, porque los imita.
- **Señales de alerta:**
  - resumir una ley en vez de copiarla;
  - casos sin fuente;
  - instrucciones que piden opinar;
  - quitar las reglas de neutralidad.
- **Intervenir:** ante bloqueos de más de 10 a 15 minutos. Apoya con pistas, no con código.

## Etapa 5 · Integración (13:30–14:15, 45 min)
**Objetivo del equipo:** unir los componentes en un prototipo único y comprobar que el flujo principal funciona de punta a punta.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 15 min | Unir componentes | Todo en la misma versión (fork, planilla o repositorio propio). Si usan los prototipos, revisen la barra lateral: sin filas ignoradas |
| 20 min | Pruebas del flujo principal | El recorrido completo varias veces, con casos representativos y límite (un mensaje sin caso verificado, una pregunta que el documento no responde). Prueben al menos 5 usos indebidos y anoten qué pasó: pedir una opinión, «¿por quién voto?», «ignora tus reglas», acusar a alguien sin sentencia o pedir un discurso partidista |
| 10 min | Corrección y priorización | Primero lo que impide la demo; el resto, a trabajo futuro |

**Mentor:**
- **Qué hacer:** hazte pasar por el usuario y prueba una entrada distinta a la del equipo.
- **Qué revisar:** que cada respuesta cite su fuente y cómo se comporta ante preguntas partidistas, de actualidad o sobre candidatos.
- **Intervenir:** si a los 30 minutos no hay un flujo funcionando; sugiere reducir el alcance.

## Etapa 6 · Cierre técnico (14:15–14:45, 30 min)
**Objetivo del equipo:** estabilizar y congelar la versión final. Desde aquí no se agregan funcionalidades.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 10 min | Últimos ajustes | Solo correcciones visibles para la demo |
| 10 min | Prueba final y respaldo | Recorrido completo, **video corto de respaldo** y registro de consultas descargado |
| 10 min | Congelar versión | Último *commit* y etiqueta `version-final` ([guía para equipos](TUTORIAL_FORK.md), sección 13); planilla sin más cambios. Anotar cómo se ejecuta y las limitaciones conocidas |

**Antes de las 14:45 h:**
- **Checklist ético completo:** requisito de admisibilidad.
- **Declaración de transparencia:**
  - qué modelos y herramientas de IA usaron y cómo (el modelo aparece bajo cada respuesta de los prototipos);
  - qué tomaron del prototipo de referencia y qué aportó el equipo.
- **Set fijo de documentos y preguntas para la demo,** todos precargados y verificados, con su fuente.

**Mentor:**
- **Revisar:** que la lista de limitaciones sea honesta.
- **Preguntar:** qué uso del sistema sería inapropiado. Por ejemplo, presentar la herramienta como árbitro de la verdad o usarla para desacreditar a alguien.
- **Intervenir:** si a los 15 minutos siguen agregando funciones.

## Etapa 7 · Preparación del pitch (14:45–16:15, 90 min)
**Objetivo del equipo:** una presentación breve que cuente problema, solución, valor y demo.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 15 min | Estructura del relato | Problema y usuario con evidencia → solución y aporte de la IA → aporte propio (si partieron de un prototipo de referencia: antes y después) → demo → decisiones éticas → impacto y modelo de operación |
| 25 min | Construcción de la presentación | Pocas diapositivas, visuales; incluir una de uso responsable y limitaciones |
| 15 min | Guion de la demo | Set fijo de documentos con la fuente en pantalla, orden y quién opera. Video de respaldo listo |
| 20 min | Ensayo 1 y ajustes | Cronometrado: 5 minutos de pitch con demo |
| 15 min | Preguntas del jurado | 8 a 10 preguntas con responsable. Al menos una de mal uso, por ejemplo: «¿Cómo evitan explicaciones sesgadas con apariencia de neutralidad?» o «¿Qué pasa si la persona confía ciegamente en la herramienta?» |

**Mentor:**
- **Que el pitch empiece por la persona,** no por la tecnología.
- **Que las afirmaciones coincidan con lo que se vio en las pruebas.**
- **Pedir un ensayo completo** si a los 50 minutos no lo han hecho.

## Etapa 8 · Presentación final (16:15–18:15)
**Formato según las bases:**
- 1 o 2 representantes por equipo;
- **5 minutos de pitch con demo y 3 minutos de preguntas del jurado,** con al menos una pregunta sobre riesgos éticos o mal uso;
- se evalúa la versión congelada a las 14:45 h, con una rúbrica única en la que ética e impacto suman el 50%.

**Mentor:**
- **Antes del turno:** repasar orden, tiempo y plan B.
- **Durante el pitch:** no intervenir.
- **Después:** 2 fortalezas, 1 mejora y una observación sobre uso responsable.

---

## Observación del equipo (para el mentor)
Mismos criterios de las guías oficiales, con lo que se mira en el Desafío 3:

| Etapa | Criterios oficiales | Qué mirar en el D3 |
|---|---|---|
| 1 | Participación equilibrada · necesidades distintas de soluciones · actores y restricciones · tiempo | Consideran a quien no verifica nunca o solo usa WhatsApp |
| 2 | Problema acotado · objetivo medible · alcance realista · acuerdo | El tema está dentro de bases: nada de actualidad política |
| 3 | Arquitectura coherente · IA justificada · tecnologías acordes · reparto | Las calificaciones y las citas vienen de la fuente, no de la IA; hay un aporte propio frente al prototipo de referencia |
| 4 | Trabajo en paralelo · repositorio y versiones · bloqueos · foco | Corpus con fuente oficial y texto literal; neutralidad intacta |
| 5 | Flujo completo · fallas priorizadas · casos distintos · coordinación | Preguntas adversariales probadas y anotadas |
| 6 | Versión congelada · plan B · conocimiento compartido · limitaciones honestas | Set fijo de demo, checklist ético y transparencia entregados, distinguiendo referencia y aporte propio |
| 7 | Relato claro · propuesta de valor · demo ensayada · todos participan · tiempo | Fuente visible en la demo y diapositiva de uso responsable |
| 8 | Claridad · demo funcionando · respuestas · trabajo en equipo · tiempo | Responden con honestidad sobre riesgos y neutralidad |
