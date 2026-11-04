# Guía breve para mentores · Desafío 3 · Ciudadanía informada

Plantillas: **"Pausa antes de compartir"** (A) y **"La ley en simple"** (B), asignadas por sorteo. Cada equipo recibe el enlace a la app, su código y clave, y la planilla para personalizarla. La herramienta ya funciona, pero está pensada para "cualquier persona": **el trabajo del equipo es volverla útil, segura y confiable para alguien concreto.**

| Variante | App |
|---|---|
| A · Pausa antes de compartir | https://hackaton-d3-pausa.streamlit.app |
| B · La ley en simple | https://hackaton-d3-ley.streamlit.app |

Acompañas a 4 equipos con las **guías oficiales del mentor** (8 etapas). Este documento agrega lo propio del Desafío 3. Los equipos pueden cambiar la herramienta desde la planilla, sin programar, o copiando el código desde GitHub con la [guía para equipos](TUTORIAL_FORK.md).

## Tu rol en cada etapa
Detalle por etapa (actividades, señales de alerta y criterios de observación) en [Etapas de la jornada](Etapas_jornada_Desafio3.md). Los equipos completan las [Fichas del equipo](Fichas_equipo_Desafio3.md).

| Etapa | Tu foco en el Desafío 3 |
|---|---|
| 1 · Inmersión | Que entiendan el problema antes de tocar la app, conversen con personas reales y usen fuentes verídicas |
| 2 · Definición | Recortar: 2 a 4 mejoras, objetivo medible y tema dentro de bases. **Checkpoint ético 1:** ¿qué daño podría causar su objetivo? |
| 3 · Diseño | Que el diagrama muestre dónde decide una persona y de dónde viene cada caso o ley |
| 4 · Desarrollo | Corpus con fuente oficial y texto literal; que no quiten las reglas de neutralidad |
| 5 · Integración | Probar como usuario. **Checkpoint ético 2:** preguntas partidistas, de actualidad o sobre candidatos |
| 6 · Cierre técnico | Congelar, set fijo para la demo, checklist ético y transparencia antes de las 14:45 h |
| 7 · Preparación del pitch | Ensayo cronometrado, fuente visible en la demo, diapositiva de uso responsable |
| 8 · Presentación final | No intervenir; después, 2 fortalezas, 1 mejora y una observación ética |

## Antes de la jornada
- Entra a ambas apps con **tu código de mentor** (M01, M02…, lo entrega la organización) y recorre un caso completo en cada una. Tu código tiene cuota propia, no gasta las consultas de ningún equipo, y si la IA falla te muestra el diagnóstico.
- El día del evento, abre ambas apps antes de las 9:00 h: se duermen tras 12 horas sin uso.
- Ten a mano los códigos y claves de tus equipos, el enlace a las planillas base, `Riesgos_eticos_Desafio3`, las [rutas de mejora](Rutas_de_mejora_Desafio3.md) y las fichas de cada etapa para tus 4 equipos (impresas o compartidas).
- Repasa la regla de la demo: solo documentos o casos precargados y verificados, con la fuente en pantalla. Nada de actualidad política, candidaturas, partidos ni autoridades.

## Errores frecuentes
| Error | Cómo se ve | Qué decir |
|---|---|---|
| Querer analizar política contingente | La app se niega a responder | "Está fuera de bases. Elijan salud, estafas, consumo, trámites o una ley de su interés." |
| Ejemplos con errores en `ejemplos` | La IA repite el error en todas las respuestas | Revisar cada ejemplo contra el texto oficial antes de usarlo |
| `instrucciones_extra` que piden opinar o persuadir | La validación lo bloquea o la IA lo ignora | Las reglas fijas mandan: reformular |
| Resumir una ley en `leyes_extra` | Explicaciones "fieles" a un texto que no es el oficial | Copiar el texto **literal** desde bcn.cl/leychile, un artículo por fila |
| Caso agregado sin verificar | Sale en la demo un caso con fuente débil | Todo caso de `casos_extra` necesita fuente oficial |
| Filas mal completadas | La barra lateral muestra filas ignoradas | Abrir el aviso: dice qué corregir |
| Editar y no recargar | No cambia nada | Presionar "Recargar configuración" |
| "Se muestra una respuesta de demostración" | La IA no respondió | Esperar un minuto; si persiste, entrar con tu código de mentor para ver el diagnóstico y avisar a la organización |

## Preguntas típicas de los equipos
- **¿Podemos cambiar el prompt?** No completo: las reglas de neutralidad son fijas. Sí pueden cambiar usuario, tono, largo, ejemplos, instrucciones extra y los textos de la pantalla.
- **¿Podemos agregar otra ley?** Sí, en `leyes_extra`, con el texto literal copiado de la fuente oficial. Si no está completa, deben marcar "artículos seleccionados".
- **¿Cómo pedimos un tono o un trato?** En `tono` o en `instrucciones_extra`, en palabras simples: "Directo y cercano. Trata de 'hermano'". La app aplica ese estilo a lo que escribe la IA (aparece "🎨 Respuesta escrita con el estilo de tu equipo"). Si sus `ejemplos` están en otro tono, conviene reescribirlos en el tono que quieren.
- **¿Por qué el tono no cambia la explicación del caso?** La explicación verificada se muestra tal cual; el tono se aplica al resumen "En simple" y a lo que escribe la IA. Si quieren otra explicación, la escriben en `casos_extra`.
- **¿Por qué la herramienta no dice "es falso"?** Porque la calificación solo puede venir de un caso verificado, nunca de la IA, y la decisión final es de la persona.
- **¿Cuántas consultas tenemos?** 120 por equipo; la barra lateral y el pie de la app muestran cuántas quedan.
- **¿Qué modelo usamos?** Aparece bajo cada respuesta ("Respondió…"); va en la declaración de transparencia.

## Cómo destrabar a un equipo bloqueado (en 5 minutos)
1. **Sin usuario claro:** "**[persona concreta]** necesita **[entender o verificar algo]** cuando **[momento]**". Ejemplos: abuelos que reciben cadenas en el grupo familiar; estudiantes de liceo en formación ciudadana; dueños de almacén ante una ley que les afecta.
2. **Sin dirección:** que elijan como máximo dos rutas de mejora y las hagan bien.
3. **Técnico:** revisar en la barra lateral si la planilla se leyó y si hay filas ignoradas. Si nada funciona, borrar la URL de la planilla y trabajar con la base.
4. **Ética trabada:** usar la ruta A6 o B6 ("Probar el mal uso antes que el jurado", en [Rutas de mejora](Rutas_de_mejora_Desafio3.md)) y `Riesgos_eticos_Desafio3`: decidir qué harán **y qué no**.
5. **Sin flujo funcionando a los 30 minutos de la Etapa 5:** reducir alcance y asegurar un recorrido mínimo.
6. **Al empezar el cierre técnico (14:15 h) sin demo estable:** dejar de agregar, asegurar lo que funciona y grabar un video de respaldo.

## Para el pitch (16:15 a 18:15 h)
Mostrar la versión del equipo funcionando con documentos o casos verificados, qué cambiaron respecto de la plantilla y cómo medirían si ayuda a su usuario. Formato según las bases: 5 minutos de pitch con demo y 3 de preguntas; se evalúa la versión congelada a las 14:45 h. El jurado preguntará cómo se podría usar mal: "¿Cómo evitan que alguien produzca explicaciones sesgadas con apariencia de neutralidad?" y "¿Qué pasa si la persona confía ciegamente en la herramienta?"
