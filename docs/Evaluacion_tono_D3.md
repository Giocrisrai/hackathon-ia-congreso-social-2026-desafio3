# Evaluación del tono · Desafío 3 (3 de noviembre de 2026)

**Por qué:** en su prueba, Guillermo Pinto configuró en la planilla un tono confrontacional y directo que pedía tratar de "hermano", y las respuestas no cambiaban. La causa: sus **ejemplos estaban escritos en tono neutro** y el modelo los imitaba más que al campo `tono`; además, las reglas fijas pesaban más que el estilo.

## Qué se cambió
1. **Paso de estilo** (`nucleo/tono.py`): cuando el equipo cambia usuario, tono, instrucciones o largo, un segundo paso breve reescribe **solo lo que escribió la IA** con ese estilo. Nunca toca la calificación, los artículos ni el texto verificado. El tono y las instrucciones del equipo mandan sobre los ejemplos neutros.
2. **Controles fijos en el código**, que no dependen de que el modelo obedezca:

| Control | Qué impide | Dónde |
|---|---|---|
| Misma forma | Que se unan, dividan o reordenen frases (con un segundo intento) | `tono.aplicar` |
| Conservación | Que la versión con estilo pierda un organismo, una cifra o un año del original | `tono.conserva` |
| Sentido | Atribuir la sanción a "tú", o agregar llamados a la acción o preguntas | `tono.cambia_sentido` |
| Trato obligatorio | Si la planilla pide un trato ("Trata de 'hermano'") y el modelo lo omite, se antepone | `tono.trato_pedido` |
| Tuteo | Voseo de algunos modelos ("para vos" → "para ti") | `tono.tutear` |
| A · sin caso | Afirmar hechos sin caso verificado: se muestra "no hay un caso verificado" | `a_verificador.limpiar` |
| A · afirmaciones ajenas | Agregar "estafa", "fraude", "datos personales"… si el caso no lo dice | `a_verificador.limpiar` |
| A · enlaces | Sitios web que no están en el corpus (p. ej., un sitio de otro país) | `a_verificador.limpiar` |
| A · largo | Pasarse del "máximo N frases" de la planilla | `a_verificador.limpiar` |
| B · organismo | Nombrar un organismo que no está en los artículos citados | `b_ley_simple.validar` |
| B · quién sanciona | "La municipalidad multa" cuando la ley dice que sanciona el juzgado | `b_ley_simple.muni_sanciona` |
| B · a quién se sanciona | "Te multan" cuando la ley sanciona a comercios o establecimientos | `b_ley_simple.sancion_mal_atribuida` |
| B · cifras | Cifras o años que no están en los artículos ni en la historia de la ley | `b_ley_simple.cifras_sin_respaldo` |
| B · citas | "[art. 5]" escrito dentro del texto | `b_ley_simple.sin_citas` |
| B · reintento | Si todas las frases se descartan, un reintento con aviso | `b_ley_simple.explicar` |

## Cómo se evaluó
- **Configuración real de Guillermo**: su usuario, sus ejemplos neutros y sus instrucciones, con 4 tonos: el suyo ("amable y pausado"), "juvenil, corto, preciso y agresivo", su descripción larga en el campo `tono` y la misma descripción en `instrucciones_extra`.
- **Mensajes**: dos casos del corpus (cadena de WhatsApp, agua con limón), uno sin caso (agua de coco y diabetes) y una pregunta de voto. En la B, la Ley 21.100 sin pregunta y "¿Quién me pone la multa…?".
- **Antes y después**: la versión publicada contra la nueva, con los mismos casos.
- **Juez independiente**: `ministral-8b` (otro modelo que el que responde), a ciegas y en orden aleatorio, puntúa tono e instrucciones de 1 a 5. Como es un juez débil para los hechos, **cada respuesta se leyó además a mano** y se agregaron controles automáticos.
- **Siete rondas** con IA real (75 ejecuciones). En las últimas, el plan gratis de Groq agotó su cuota diaria y respondieron los modelos de respaldo (gpt-oss-20b, ministral-8b): sirvieron como **prueba de estrés**.

## Resultados
| | Versión publicada | Versión nueva (ronda final) |
|---|---|---|
| Tono según el juez (1-5) | 2,6 | A 4,0 · B 3,2 |
| Sigue las instrucciones (1-5) | 2,3 | A 4,8 · B 3,7 |
| Usa "hermano" cuando se pide | 0 de 4 | 8 de 8 |
| Respetuoso · sin insultos | 6 de 6 | 12 de 12 |
| Calificación de A igual en todos los tonos | — | Sí (Falso en ambos casos del corpus) |
| Pregunta de voto con tono confrontacional | — | Fuera de alcance |
| La multa recae en el comercio, no en "tú" | Error en la versión publicada ("te multa…") | 6 de 6 |
| Tiempo de respuesta | ~2 s | ~3,5 a 4,8 s (un paso más) |

**Ejemplo (A, tono largo de Guillermo):** *"Hermano, esa cadena lleva años circulando; reenviarla no cambia nada de la app. No hay evidencia de que WhatsApp vaya a cobrar ni de que reenviar mensajes lo haga gratis."* La explicación verificada sigue visible debajo.

**Ejemplo (B, tono largo):** *"Hermano, el juzgado de policía local multa al comercio que entrega bolsas plásticas."*

## Errores encontrados en el camino y corregidos
Fusión de artículos; la multa atribuida a "tú"; "es una estafa" agregado; un sitio web de otro país inventado; "la municipalidad puede imponer multas"; "$500 mil en 2024" inventado; voseo; "[art. 5]" dentro del texto; un llamado al lector ("deja de usar bolsas"); exceso de frases; y un paso de estilo que fallaba cuando el modelo dividía una frase. Todos tienen su control y su prueba.

## Pruebas automáticas (sin IA, segundos)
`python pruebas/test_tono.py` y `python pruebas/test_variantes.py`: **16 pruebas**, todas en verde. El evaluador con IA está en `pruebas/evaluacion_tono/` (requiere claves en un archivo de secrets propio).

## Límites conocidos
- La B sube menos de tono que la A: el texto legal admite menos cambio de registro, y está bien que así sea.
- Con los modelos de respaldo la calidad baja. Los controles evitan errores de contenido, pero si descartan todo, la app muestra "no se pudo generar una explicación con respaldo": es preferible a mostrar algo falso. **Con el plan pagado de Groq, responde siempre el modelo principal.**
- El paso de estilo usa una consulta extra a la IA (no descuenta cuota del equipo, pero sí tokens del proveedor).
