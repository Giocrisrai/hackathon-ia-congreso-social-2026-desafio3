# Fuentes de las 3 normas de la demo · Variante B

Estado: **pendiente de carga**. Los textos deben copiarse desde la BCN (Ley Chile) antes de agregarlos a `datos/b_leyes.csv`. Ninguna de las filas de esta tabla está verificada todavía.

## 1. Normas a verificar

| id_ley | Norma a verificar | Qué confirmar antes de cargar | Enlace BCN | Estado |
|---|---|---|---|---|
| `L21165` | Estatuto Laboral Joven / jornada parcial | Número de ley y título oficial. La propuesta original indica Ley 21.165; confirmar en BCN. | por completar | pendiente |
| `L21202` | Humedales urbanos | Número de ley (propuesta: 21.202) y artículos que regulan la protección. | por completar | pendiente |
| `CDT8` | Código del Trabajo, art. 8 (prácticas, colación y movilización) | Que el art. 8 contiene la obligación que se quiere explicar. No existe una ley autónoma "de pago de prácticas". | https://www.bcn.cl/leychile/navegar?idNorma=207436 | pendiente |

Nota: la Ley 21.133 aparece en resultados de búsqueda como norma sobre trabajadores independientes; no debe usarse como "Estatuto Laboral Joven" sin verificarlo en BCN.

## 2. Cómo cargar cada norma

1. Abrir la norma en bcn.cl/leychile y copiar el texto de cada artículo seleccionado.
2. Una fila por artículo en `datos/b_leyes.csv`, **al final del archivo**, con las columnas:
   `id_ley,nombre_ley,articulo,titulo_articulo,texto,historia,url_oficial,cobertura`
3. `texto` sin encabezados, firmas ni nombres de parlamentarios.
4. `nombre_ley`, `historia`, `url_oficial` y `cobertura` iguales en todas las filas de la misma ley.
5. Si se usan artículos seleccionados, `cobertura` = `artículos seleccionados`; si no, `completa`.
6. Ejecutar `python pruebas/test_corpus.py` y corregir hasta que pase.

## 3. Preguntas de prueba

Completar el artículo esperado solo cuando el texto ya esté cargado y verificado.

| Norma | Pregunta | Artículo esperado |
|---|---|---|
| Estatuto Laboral Joven (`L21165`) | ¿Puedo trabajar 30 horas y estudiar? | por confirmar |
| Estatuto Laboral Joven (`L21165`) | ¿Qué derechos tengo si trabajo medio tiempo? | por confirmar |
| Estatuto Laboral Joven (`L21165`) | ¿Qué pasa si mi empleador no cumple la jornada pactada? | por confirmar |
| Estatuto Laboral Joven (`L21165`) | ¿Desde cuándo rige esta ley? | por confirmar |
| Estatuto Laboral Joven (`L21165`) | ¿Quién fiscaliza que se cumpla? | por confirmar |
| Prácticas (`CDT8`) | ¿Me tienen que pagar colación y movilización? | art. 8 |
| Prácticas (`CDT8`) | ¿Qué pasa si no me pagan la colación? | por confirmar |
| Prácticas (`CDT8`) | ¿Quién tiene que pagar la movilización? | por confirmar |
| Prácticas (`CDT8`) | ¿Puedo pedir la colación si hago práctica de medio día? | por confirmar |
| Prácticas (`CDT8`) | ¿Qué hago si el empleador me niega la colación? | por confirmar |
| Humedales (`L21202`) | ¿Qué pasa si construyen sobre un humedal urbano? | por confirmar |
| Humedales (`L21202`) | ¿Quién protege los humedales urbanos? | por confirmar |
| Humedales (`L21202`) | ¿Desde cuándo se aplica esta ley? | por confirmar |
| Humedales (`L21202`) | ¿Qué dice sobre las áreas verdes de la comuna? | por confirmar |
| Humedales (`L21202`) | ¿Puedo denunciar un daño a un humedal? | por confirmar |

Comprobar en cada consulta: que cada frase lleve `(art. N)`, que el artículo exista en la ley y que las frases sin cita se descarten.

## 4. Verificación final (checklist de Persona A)

- [ ] Las 3 normas están cargadas al final de `datos/b_leyes.csv`.
- [ ] `python pruebas/test_corpus.py` pasa.
- [ ] `python pruebas/test_variantes.py` sigue pasando (la primera ley sigue siendo L21100).
- [ ] `datos/b_diccionario.md` lista las 3 normas nuevas.
- [ ] Cada norma tiene al menos 5 preguntas con artículo esperado confirmado.
- [ ] Se guardó una muestra del CSV de registro para el mentor.
