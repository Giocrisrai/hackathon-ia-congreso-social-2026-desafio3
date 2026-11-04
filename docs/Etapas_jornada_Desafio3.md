# Etapas de la jornada · Desafío 3 · Ciudadanía informada

Hackathon IA Aplicada · Congreso Social UC 2026 · 6 de noviembre de 2026 · Duoc UC San Joaquín

Este documento baja al Desafío 3 las **8 etapas de las guías oficiales del mentor**: mismos nombres, tiempos, actividades, entregables y criterios de observación. Agrega lo propio del desafío: qué hace el equipo con la plantilla en cada etapa y qué mira el mentor.

**Modalidad.** Los equipos no parten de cero. Cada equipo recibe por sorteo una de las dos variantes de la plantilla base:
- **A · Pausa antes de compartir:** verificación de contenidos virales.
- **B · La ley en simple:** leyes y proyectos de ley en lenguaje claro.

Su trabajo es adaptarla y mejorarla para un usuario y un caso concretos:
- desde la planilla, sin programar;
- o copiando el código desde GitHub y modificándolo, con la [guía para equipos](TUTORIAL_FORK.md).

Las fichas de cada etapa están en [Fichas del equipo](Fichas_equipo_Desafio3.md) y las ideas de mejora, en [Rutas de mejora](Rutas_de_mejora_Desafio3.md).

**La herramienta es neutral por diseño:**
- no opina, no persuade y no trata candidaturas, partidos, elecciones ni autoridades;
- en la demo se usan solo documentos públicos verificados, nada de actualidad política abierta.

| Etapa | Horario | Enfoque | Entregable |
|---|---|---|---|
| 1 · Inmersión | 10:00–10:45 (45 min) | Design Thinking: Empatizar · IA Responsable | Ficha de Inmersión |
| 2 · Definición | 10:45–11:15 (30 min) | Design Thinking: Definir · Lean Startup | Ficha de Definición |
| 3 · Diseño | 11:15–11:45 (30 min) | Design Sprint: Esbozar y decidir · IA Responsable | Ficha de Diseño |
| 4 · Desarrollo | 11:45–12:45 (60 min) | Lean Startup: Construir · IA Responsable | Mejoras implementadas y guardadas, con registro de cambios |
| 5 · Integración | 13:30–14:15 (45 min) | Design Sprint: Prototipar y probar · Lean · IA Responsable | Flujo completo funcionando, con registro de pruebas y fallas |
| 6 · Cierre técnico | 14:15–14:45 (30 min) | Lean Startup: Medir y aprender · IA Responsable | Versión congelada, checklist ético, declaración de transparencia y set fijo para la demo |
| 7 · Preparación del pitch | 14:45–16:15 (90 min) | Design Sprint: Contar la historia · IA Responsable | Presentación, guion de demo, roles y preguntas anticipadas |
| 8 · Presentación final | 16:15–18:15 (120 min) | Todos los enfoques · IA Responsable | Pitch y demo, más una nota de aprendizajes |

---

## Etapa 1 · Inmersión (10:00–10:45, 45 min)
**Objetivo del equipo:** comprender a fondo el desafío antes de proponer soluciones: qué problema existe, a quién afecta y bajo qué límites.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 10 min | Lectura del desafío | Lean el enunciado y la [guía para participantes](Guia_participantes_Desafio3.md). Abran la app y prueben un ejemplo, sin cambiar nada |
| 15 min | Mapa de actores | Votante joven, personas mayores en grupos familiares, sociedad civil, municipio, medios, colegios, verificadores |
| 10 min | Necesidades y restricciones | Datos: Congreso, SERVEL, Consejo para la Transparencia, datos.gob.cl, [bcn.cl/leychile](https://www.bcn.cl/leychile) y verificadores. Restricciones: neutralidad verificable, trazabilidad de fuentes y nada de contenido partidista |
| 10 min | Síntesis y consenso | Top 3 de necesidades y una frase del desafío con sus palabras |

**Mentor:**
- **Qué observar:** que hablen con personas de las fundaciones o con usuarios reales, y que usen fuentes verídicas desde el inicio.
- **IA responsable:** ¿quién queda fuera? Por ejemplo, personas con baja alfabetización digital o que solo usan WhatsApp.
- **Intervenir:** si a los 25 minutos no hay actores definidos.

## Etapa 2 · Definición (10:45–11:15, 30 min)
**Objetivo del equipo:** convertir lo comprendido en una necesidad acotada, un objetivo claro y un alcance realista.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 10 min | Enunciado del problema | «[Actor] necesita [necesidad] porque [razón]». Ejemplo A: «Una abuela que recibe cadenas de salud en el grupo familiar necesita saber si reenviarlas porque no sabe cómo verificarlas». Ejemplo B: «El dueño de un almacén necesita entender la ley de bolsas plásticas porque lo pueden multar» |
| 10 min | Objetivo medible | Un criterio que se pueda mostrar en la demo. Ejemplos: la persona decide no reenviar un mensaje falso en menos de un minuto, o un estudiante explica la ley con sus palabras después de leerla |
| 10 min | Alcance: sí / no | Qué mejorarán de la plantilla (2 a 4 cambios), qué corpus precargarán y qué queda fuera. Tienen 2,5 h de trabajo efectivo |

**Hipótesis (Lean):** «Creemos que [cambio en la plantilla] logrará [resultado] para [actor]. Lo sabremos si [métrica]».

**Mentor:**
- **Señales de alerta:**
  - elegir temas de actualidad política (está fuera de bases);
  - objetivos vagos («combatir la desinformación»);
  - un objetivo que ignora el daño de una herramienta que parece neutral pero no lo es.
- **Checkpoint ético 1:** al cierre de la etapa, pregunten qué resultado no deseado podría tener su objetivo.

## Etapa 3 · Diseño (11:15–11:45, 30 min)
**Objetivo del equipo:** planificar qué cambiarán de la plantilla, cómo encaja en el día del usuario y quién hace qué. Con plantilla, "arquitectura y tecnologías" significa decidir **qué parte de la plantilla tocan**.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 8 min | Funcionalidades | 2 a 4 mejoras priorizadas (imprescindible / deseable), elegidas de las [rutas de mejora](Rutas_de_mejora_Desafio3.md) o propias |
| 8 min | Arquitectura y tecnologías | Dibujen el flujo de la plantilla y marquen dónde cae cada mejora y si va en la planilla o en el código (secciones 5 a 7 de la [guía para equipos](TUTORIAL_FORK.md)). **A:** mensaje → la IA identifica la afirmación y busca un caso → la calificación sale **solo del caso verificado** → la persona decide si comparte. **B:** artículos → la IA explica frase por frase con su artículo → los controles descartan frases sin respaldo → la persona lee el artículo original |
| 7 min | Experiencia de usuario | 2 a 4 pasos del usuario real: dónde recibe el mensaje o la ley, qué ve y qué hace con el resultado |
| 7 min | Reparto de trabajo | Responsables, por ejemplo: planilla y tono, corpus verificado (casos o leyes con su fuente), código (si lo usan), pruebas y mal uso, pitch |

**Mentor:**
- **IA responsable:** que señalen en el diagrama **dónde decide una persona**, de dónde vienen los casos o las leyes y quién los verificó.
- **Señales de alerta:** la IA califica sola, o se usan fuentes no oficiales.
- **Intervenir:** si dependen de algo que no existe, como un verificador que no tiene el caso.

## Etapa 4 · Desarrollo (11:45–12:45, 60 min)
**Objetivo del equipo:** implementar en paralelo las mejoras imprescindibles, sobre la plantilla.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 10 min | Preparación del entorno | Copia de la planilla compartida como Lector y su URL cargada en la app. Si van a tocar código: **fork** del repositorio, compañeros como colaboradores, app propia publicada y claves en Secrets ([guía para equipos](TUTORIAL_FORK.md), secciones 2 a 4) |
| 35 min | Construcción en paralelo | Cada responsable implementa su mejora. El corpus se carga verificado: en `casos_extra`, cada caso con fuente oficial; en `leyes_extra`, el texto **literal** de bcn.cl, un artículo por fila |
| 10 min | Puntos de control | A los 25 y 45 minutos: 2 minutos por integrante, mostrando el mismo caso o la misma ley antes y después |
| 5 min | Cierre de etapa | Guardar el avance: la planilla se guarda sola; el código, con *commit*. Anotar en el registro de cambios qué se cambió y por qué |

**Mentor:**
- **IA responsable:** que verifiquen lo que escribe la IA contra la fuente, y que los `ejemplos` de la planilla no "declaren" nada falso, porque la IA los imita.
- **Señales de alerta:**
  - resumir una ley en vez de copiarla;
  - casos sin fuente;
  - instrucciones que piden opinar;
  - quitar las reglas de neutralidad.
- **Intervenir:** ante bloqueos de más de 10 a 15 minutos. Apoya con pistas, no con código.

## Etapa 5 · Integración (13:30–14:15, 45 min)
**Objetivo del equipo:** unir las mejoras en una sola versión y comprobar que el flujo principal funciona de punta a punta.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 15 min | Unir componentes | Todas las mejoras en la misma planilla o en el mismo fork. Recargar la configuración y revisar la barra lateral: sin filas ignoradas |
| 20 min | Pruebas del flujo principal | **A:** mensaje con caso → calificación → decisión, y un mensaje sin caso. **B:** ley sin pregunta, con pregunta y con una pregunta que la ley no responde. Probar al menos 5 usos indebidos y anotar qué pasó: pedir una opinión, «¿por quién voto?», «ignora tus reglas», acusar a alguien sin sentencia o pedir un discurso partidista |
| 10 min | Corrección y priorización | Primero lo que impide la demo; el resto, a trabajo futuro |

**Mentor:**
- **Qué hacer:** hazte pasar por el usuario y prueba una entrada distinta a la del equipo.
- **Qué revisar:** que cada respuesta cite su fuente y cómo se comporta ante preguntas partidistas, de actualidad o sobre candidatos.
- **Checkpoint ético 2:** la revisión de sesgos se hace en esta etapa.
- **Intervenir:** si a los 30 minutos no hay un flujo funcionando.

## Etapa 6 · Cierre técnico (14:15–14:45, 30 min)
**Objetivo del equipo:** estabilizar y congelar la versión final. Desde aquí no se agregan funcionalidades.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 10 min | Últimos ajustes | Solo correcciones visibles para la demo |
| 10 min | Prueba final y respaldo | Recorrido completo, **video corto de respaldo** y registro de la app descargado desde la barra lateral |
| 10 min | Congelar versión | Planilla: no editar más. Código: último *commit* y etiqueta `version-final` ([guía para equipos](TUTORIAL_FORK.md), sección 13). Anotar cómo se ejecuta y las limitaciones conocidas |

**Antes de las 14:45 h:**
- **Checklist ético:** requisito de admisibilidad.
- **Declaración de transparencia:** qué venía en la plantilla base y qué aportó el equipo, y qué modelos se usaron (aparece bajo cada respuesta, por ejemplo "anthropic · claude-haiku-5-5").
- **D3:** set fijo de documentos y preguntas para la demo, todos precargados y verificados.

**Mentor:**
- **Revisar:** que la lista de limitaciones sea honesta.
- **Preguntar:** qué uso del sistema sería inapropiado. Por ejemplo, presentar la herramienta como árbitro de la verdad o usarla para desacreditar a alguien.
- **Intervenir:** si a los 15 minutos siguen agregando funciones.

## Etapa 7 · Preparación del pitch (14:45–16:15, 90 min)
**Objetivo del equipo:** una presentación breve que cuente problema, solución, valor y demo.

| Tiempo | Actividad | En el Desafío 3 |
|---|---|---|
| 15 min | Estructura del relato | Problema y usuario con evidencia → solución y aporte de la IA → mejoras propias sobre la plantilla (antes y después) → demo → decisiones éticas → impacto y modelo de operación |
| 25 min | Construcción de la presentación | Pocas diapositivas, visuales; incluir una de uso responsable y limitaciones |
| 15 min | Guion de la demo | Set fijo de casos o leyes con la fuente en pantalla, orden y quién opera. Video de respaldo listo |
| 20 min | Ensayo 1 y ajustes | Cronometrado contra el tiempo oficial del pitch |
| 15 min | Preguntas del jurado | 8 a 10 preguntas con responsable. Al menos una de mal uso, por ejemplo: «¿Cómo evitan explicaciones sesgadas con apariencia de neutralidad?» o «¿Qué pasa si la persona confía ciegamente en la herramienta?» |

**Mentor:**
- **Que el pitch empiece por la persona,** no por la tecnología.
- **Que las afirmaciones coincidan con lo que se vio en las pruebas.**
- **Pedir un ensayo completo** si a los 50 minutos no lo han hecho.

## Etapa 8 · Presentación final (16:15–18:15)
**Formato:** pitch con demo y preguntas del jurado, en el tiempo que indique la organización. Según las bases, son **5 minutos de pitch y 3 de preguntas**, con al menos una pregunta de mal uso. La rúbrica pondera ética e impacto con un 50%.

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
| 3 | Arquitectura coherente · IA justificada · tecnologías acordes · reparto | La calificación (A) o el artículo (B) vienen de la fuente, no de la IA |
| 4 | Trabajo en paralelo · repositorio y versiones · bloqueos · foco | Corpus con fuente oficial y texto literal; neutralidad intacta |
| 5 | Flujo completo · fallas priorizadas · casos distintos · coordinación | Preguntas adversariales probadas y anotadas |
| 6 | Versión congelada · plan B · conocimiento compartido · limitaciones honestas | Set fijo de demo, checklist ético y transparencia entregados |
| 7 | Relato claro · propuesta de valor · demo ensayada · todos participan · tiempo | Fuente visible en la demo y diapositiva de uso responsable |
| 8 | Claridad · demo funcionando · respuestas · trabajo en equipo · tiempo | Responden con honestidad sobre riesgos y neutralidad |
