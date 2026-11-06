# Fuentes de las 3 normas de la demo · Variante B

Estado: **pendiente de carga**. Los textos deben copiarse desde la BCN (Ley Chile) antes de agregarlos a `datos/b_leyes.csv`. Ninguna de las filas de esta tabla está verificada todavía.

## 1. Normas a verificar

| id_ley | Norma a verificar | Qué confirmar antes de cargar | Enlace BCN | Estado |
|---|---|---|---|---|
| `L21165` | Ley 21.165 · Establece una jornada parcial alternativa para estudiantes trabajadores | Verificada con el PDF oficial de BCN (publicada 26-07-2019). Cargada: 14 filas (intro y letras a-h del art. 40 bis E del Código del Trabajo, arts. 2 a 4 de la ley y transitorios). | https://bcn.cl/3l7ev | cargada |
| `L21202` | Humedales urbanos | Número de ley (propuesta: 21.202) y artículos que regulan la protección. | por completar | pendiente |
| `CDT8` | Código del Trabajo, art. 8 (prácticas, colación y movilización) | Que el art. 8 contiene la obligación que se quiere explicar. No existe una ley autónoma "de pago de prácticas". | https://www.bcn.cl/leychile/navegar?idNorma=207436 | pendiente |

Nota: el título "Estatuto Laboral Joven" del brief no corresponde a la Ley 21.165, que se llama "Establece una jornada parcial alternativa para estudiantes trabajadores". La Ley 21.133 aparece en resultados de búsqueda como norma sobre trabajadores independientes; no la uses sin verificarla en BCN.

Las referencias "art. N" de la ley usan el número de la fila: `40 bis E a` … `40 bis E h` para las letras del art. 40 bis E del Código del Trabajo, `2`, `3`, `4` para los artículos de la ley y `transitorio primero` / `transitorio segundo`.

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
| Jornada parcial (`L21165`) | ¿Qué entiende la ley por estudiante trabajador? | `40 bis E a` |
| Jornada parcial (`L21165`) | ¿Qué pasa si dejo de cumplir los requisitos de edad o estudios? | `40 bis E c` |
| Jornada parcial (`L21165`) | ¿Cuántas horas puedo trabajar al día? | `40 bis E d` |
| Jornada parcial (`L21165`) | ¿Un accidente en el trayecto entre el colegio o la universidad y el trabajo es accidente laboral? | `40 bis E d` |
| Jornada parcial (`L21165`) | ¿Tengo permiso para rendir exámenes? | `40 bis E e` |
| Jornada parcial (`L21165`) | ¿Qué puedo pactar en vacaciones académicas? | `40 bis E f` |
| Jornada parcial (`L21165`) | ¿Qué pasa si soy carga familiar? | `40 bis E g` |
| Jornada parcial (`L21165`) | ¿Qué empresas no pueden pactar esta jornada? | `40 bis E h` |
| Jornada parcial (`L21165`) | ¿Desde cuándo rige la ley? | `transitorio primero` |
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

- [x] Ley 21.165 cargada al final de `datos/b_leyes.csv` (14 filas).
- [ ] Ley 21.202 (humedales) y art. 8 del Código del Trabajo cargados.
- [ ] `python pruebas/test_corpus.py` pasa.
- [ ] `python pruebas/test_variantes.py` sigue pasando (la primera ley sigue siendo L21100).
- [ ] `datos/b_diccionario.md` lista las 3 normas nuevas.
- [ ] Cada norma tiene al menos 5 preguntas con artículo esperado confirmado.
- [ ] Se guardó una muestra del CSV de registro para el mentor.
