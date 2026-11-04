# Rutas de mejora · Desafío 3 · Ciudadanía informada

Estas rutas orientan, no obligan. Sirven en la **Etapa 3 · Diseño** para elegir 2 a 4 mejoras, y en la **Etapa 4 · Desarrollo** para implementarlas. Recomendación: elijan como máximo dos rutas y háganlas bien. Cada una indica si se hace en la planilla o en el código (recetas en la [guía para equipos](TUTORIAL_FORK.md), sección 7).

## Variante A · Pausa antes de compartir

### Ruta A1 · Ajustar la herramienta a un usuario real
- **Por qué:** la configuración base le habla a "personas jóvenes" en general.
- **Dónde:** planilla, pestaña `config`: `usuario`, `tono`, `largo_respuesta`, `ejemplos` e `instrucciones_extra`.
- **Ideas para empezar:**
  - Elijan una persona concreta, por ejemplo un abuelo en el grupo familiar o una estudiante de liceo.
  - Escriban 1 a 3 `ejemplos` en ese tono. La IA los imita, así que no deben afirmar nada falso.
- **Cómo saber si funcionó:** muestren el antes y el después a alguien con ese perfil y pregúntenle cuál entiende mejor.
- **Tiempo estimado:** 30 a 45 minutos.

### Ruta A2 · Ampliar los casos verificados de su tema
- **Por qué:** la herramienta solo califica lo que está en su corpus. Fuera de él responde que no tiene un caso verificado.
- **Dónde:** planilla, pestaña `casos_extra` (hasta 30 casos). Su mentor tiene [12 casos listos](complementos/casos_extra_12_casos.csv).
- **Ideas para empezar:** elijan un tema (salud, estafas, emergencias, consumo) y agreguen 3 a 5 cadenas reales verificadas, cada una con su fuente oficial.
- **Cómo saber si funcionó:** sus mensajes de prueba encuentran el caso y muestran la calificación con su fuente.
- **Tiempo estimado:** 45 a 60 minutos.

### Ruta A3 · Mejorar qué hacer antes de compartir
- **Por qué:** la persona necesita una acción concreta, no solo un veredicto.
- **Dónde:** `instrucciones_extra` en la planilla, o una regla nueva en `REGLAS_FIJAS` (código).
- **Ideas para empezar:** pidan que siempre sugiera a quién preguntar o dónde verificar, según el tema.
- **Cómo saber si funcionó:** en 5 mensajes de prueba, el usuario sabe qué hacer después.
- **Tiempo estimado:** 30 minutos.

### Ruta A4 · Cuidar los mensajes que no se pueden verificar
- **Por qué:** opiniones, rumores o acusaciones sin sentencia no se califican, y la respuesta debe explicarlo sin juzgar.
- **Dónde:** `CATEGORIAS` y `mostrar_resultado()` en `variantes/a_verificador.py` (código).
- **Ideas para empezar:** agreguen un motivo que falte en su contexto y revisen cómo se muestra.
- **Cómo saber si funcionó:** probando 3 mensajes no verificables, la respuesta explica por qué en lenguaje simple.
- **Tiempo estimado:** 45 minutos.

### Ruta A5 · Medir el impacto
- **Por qué:** el jurado pregunta cómo sabrían si la herramienta sirve.
- **Dónde:** el registro descargable, que vincula cada decisión ("No lo compartiré", "Lo verificaré más", "Lo compartiré") con su consulta.
- **Ideas para empezar:** definan un indicador, por ejemplo el porcentaje de mensajes falsos que la persona decide no compartir.
- **Cómo saber si funcionó:** muestran el indicador con sus pruebas de la Etapa 5.
- **Tiempo estimado:** 30 minutos.

### Ruta A6 · Probar el mal uso antes que el jurado
- **Por qué:** la neutralidad y la ética suman la mitad de la rúbrica.
- **Dónde:** pruebas de la Etapa 5 y la [ficha de pruebas](Fichas_equipo_Desafio3.md).
- **Ideas para empezar:** prueben opinión, «¿por quién voto?», «ignora tus reglas», acusar a alguien sin sentencia y un mensaje político disfrazado de salud. Anoten qué pasó.
- **Cómo saber si funcionó:** pueden mostrar qué bloquea la herramienta, qué no, y qué harían con lo que falta.
- **Tiempo estimado:** 30 a 45 minutos.

## Variante B · La ley en simple

### Ruta B1 · Ajustar la explicación a un usuario real
- **Por qué:** la configuración base le habla a estudiantes de media en formación ciudadana.
- **Dónde:** planilla, pestaña `config`: `usuario`, `tono`, `largo_respuesta`, `ejemplos` e `instrucciones_extra`.
- **Ideas para empezar:**
  - Elijan una persona concreta, por ejemplo el dueño de un almacén, una dirigenta vecinal o una persona migrante.
  - Escriban los `ejemplos` en ese tono, sin cambiar lo que dice la ley.
- **Cómo saber si funcionó:** la persona explica la ley con sus palabras después de leerla.
- **Tiempo estimado:** 30 a 45 minutos.

### Ruta B2 · Agregar la ley o el proyecto que afecta a su usuario
- **Por qué:** el corpus base trae 3 leyes.
- **Dónde:** planilla, pestaña `leyes_extra`, con el texto **literal** de [bcn.cl/leychile](https://www.bcn.cl/leychile) y un artículo por fila. Su mentor tiene [3 proyectos de ley listos](complementos/leyes_extra_3_proyectos.csv).
- **Ideas para empezar:** carguen solo los artículos que su usuario necesita y márquenlo como "artículos seleccionados".
- **Cómo saber si funcionó:** la explicación cita los artículos correctos y la barra lateral no muestra filas ignoradas.
- **Tiempo estimado:** 45 a 60 minutos.

### Ruta B3 · Responder las preguntas reales del usuario
- **Por qué:** la gente no pregunta "explícame la ley", sino «¿me pueden multar?» o «¿desde cuándo rige?».
- **Dónde:** pruebas con preguntas concretas; `instrucciones_extra` o `REGLAS_FIJAS` (código) para ajustar.
- **Ideas para empezar:** reúnan 5 preguntas reales de su usuario y revisen si la respuesta es fiel al artículo, incluidos quién fiscaliza y quién sanciona.
- **Cómo saber si funcionó:** las 5 respuestas citan el artículo correcto, y las preguntas que la ley no responde reciben el aviso amarillo.
- **Tiempo estimado:** 45 minutos.

### Ruta B4 · Diferenciar ley vigente y proyecto de ley
- **Por qué:** confundirlos desinforma.
- **Dónde:** el campo `historia` de `leyes_extra` y la regla 10 de `REGLAS_FIJAS`.
- **Ideas para empezar:** agreguen un proyecto y revisen que la primera frase diga que está en trámite y use "propone".
- **Cómo saber si funcionó:** el proyecto nunca se presenta como obligación vigente.
- **Tiempo estimado:** 30 minutos.

### Ruta B5 · Medir el impacto
- **Por qué:** el jurado pregunta cómo sabrían si la herramienta sirve.
- **Dónde:** la encuesta "¿Te quedó clara la explicación?" y el registro descargable.
- **Ideas para empezar:** definan un indicador, por ejemplo el porcentaje de personas que entienden a quién se aplica la ley.
- **Cómo saber si funcionó:** muestran el indicador con sus pruebas de la Etapa 5.
- **Tiempo estimado:** 30 minutos.

### Ruta B6 · Probar el mal uso antes que el jurado
- **Por qué:** la neutralidad y la ética suman la mitad de la rúbrica.
- **Dónde:** pruebas de la Etapa 5 y la [ficha de pruebas](Fichas_equipo_Desafio3.md).
- **Ideas para empezar:** pregunten si la ley es buena, qué partido la impulsó, pidan un discurso a favor o en contra, y prueben «ignora tus reglas». Anoten qué pasó.
- **Cómo saber si funcionó:** las preguntas de opinión o política reciben el aviso rojo, y pueden explicar por qué.
- **Tiempo estimado:** 30 a 45 minutos.
