# Modulo 3: Gathering and Wrangling Data

**Semana:** 2
**Duracion estimada:** 2.5 horas

---

## De que va este modulo

Explica como se consiguen los datos y como se preparan para que sean
analizables. El proceso de limpieza y transformacion (wrangling) es
el que mas tiempo ocupa en el trabajo real de un analista — los estudios
del sector lo estiman en el 60-80% del tiempo total del proyecto.

---

## 1. El proceso de recopilacion de datos

Antes de tocar ninguna herramienta, hay que tener clara la pregunta.
La pregunta define que datos hacen falta, y eso define donde buscarlos.

**Los pasos:**

1. **Definir la pregunta** — sin pregunta clara no se sabe que buscar
2. **Identificar las fuentes** — internas, externas, APIs, datasets publicos
3. **Evaluar la calidad** — antes de invertir tiempo, ¿estos datos sirven?
4. **Recopilar** — descargar, consultar con SQL, llamar a la API, scraping
5. **Limpiar y transformar** — wrangling hasta que este listo para analizar

---

## 2. Calidad de los datos

No todos los datos que se encuentran son utiles. Evaluar la calidad antes
de usarlos ahorra mucho tiempo y evita conclusiones erroneas.

**Las seis dimensiones de calidad de IBM:**

| Dimension | Pregunta clave | Ejemplo de problema |
|-----------|----------------|---------------------|
| **Exactitud** | ¿Refleja la realidad? | Un precio negativo, una edad de 200 anos |
| **Completitud** | ¿Faltan valores importantes? | La mitad de los registros sin codigo postal |
| **Consistencia** | ¿Es coherente entre fuentes? | "Madrid" en una tabla y "madrid" en otra |
| **Oportunidad** | ¿Esta actualizado? | Datos de clientes de hace 3 anos |
| **Credibilidad** | ¿La fuente es fiable? | Un dataset sin autor ni metodologia |
| **Relevancia** | ¿Es pertinente para la pregunta? | Datos de temperatura para analizar ventas de ropa (pueden ser utiles, pero hay que justificarlo) |

**Como evaluar la calidad rapidamente:**

- Ver cuantos valores nulos tiene cada columna
- Comprobar si los rangos de los valores tienen sentido (edad maxima, precios negativos...)
- Buscar duplicados
- Verificar que los formatos son consistentes (fechas, monedas, textos en mayusculas/minusculas)
- Contrastar con otra fuente si es posible

---

## 3. Wrangling: limpiar y transformar datos

El wrangling es el trabajo de convertir datos en bruto en datos utilizables.
No es glamuroso, pero es donde se gana o se pierde la calidad del analisis.

**Problemas comunes y como tratarlos:**

**Valores nulos:**
Opciones segun el caso:
- Eliminar la fila si el nulo es en una columna critica y no son muchos
- Rellenar con la media o mediana (variables numericas)
- Rellenar con la moda (variables categoricas)
- Crear una categoria "Desconocido" si el nulo tiene significado propio
- Dejar el nulo si la herramienta de analisis lo gestiona bien

**Duplicados:**
Identificar si el duplicado es un error (dos registros del mismo pedido)
o es intencionado (el mismo cliente aparece en dos tablas por razones
legales). Eliminar solo los duplicados que son errores.

**Tipos de datos incorrectos:**
La columna "precio" tiene valores como "25.99€" en vez de 25.99.
Hay que limpiar el texto y convertir al tipo numerico correcto.

**Formatos inconsistentes:**
- Fechas: "01/03/2024", "2024-03-01", "1 de marzo de 2024" — todo lo mismo
- Textos: "barcelona", "BARCELONA", "Barcelona" — estandarizar
- Monedas: mezcla de euros y dolares sin indicacion — aclarar o convertir

**Outliers:**
Valores extremos que pueden ser errores de entrada o casos reales excepcionales.
Antes de eliminarlos, investigar: un salario de 1.000.000€ puede ser un error
o puede ser el CEO. No eliminar sin entender.

---

## 4. Herramientas de wrangling

**Excel / Power Query:**
Para datasets pequenos o medianos sin codigo. Power Query tiene interfaz
grafica para transformaciones comunes: quitar duplicados, cambiar tipos,
dividir columnas, filtrar filas.

**Python — pandas:**
El estandar del sector para datasets de tamano medio. Permite hacer
cualquier transformacion con codigo reproducible y documentado.
Es lo que se aprende en profundidad en los cursos 4 y 7.

**SQL:**
Para limpiar datos directamente en la base de datos antes de extraerlos.
Eficiente cuando los datos ya estan en SQL y la transformacion es sencilla.

**OpenRefine:**
Herramienta gratuita especializada en limpieza de datos. Especialmente
buena para detectar y corregir inconsistencias en texto (variantes del
mismo valor, errores tipograficos...).

---

## 5. Transformaciones habituales

Mas alla de limpiar, a veces hay que transformar los datos para que
sean comparables o analizables:

**Normalizacion:**
Escalar los valores de una variable a un rango comun (tipicamente 0-1)
para poder comparar variables que tienen unidades distintas.

**Agregacion:**
Resumir datos de nivel granular a un nivel mayor.
Ejemplo: de ventas por ticket individual a ventas totales por dia y tienda.

**Deduplicacion:**
Identificar y eliminar registros que representan la misma entidad.

**Pivoting:**
Rotar los datos de formato largo (una fila por observacion) a formato
ancho (una columna por categoria) o viceversa.

**Encoding de variables categoricas:**
Convertir categorias en numeros para que los modelos matematicos puedan
usarlas. Ejemplo: "gasolina" = 1, "diesel" = 2, "electrico" = 3.

---

## Glosario del modulo

| Termino | Definicion |
|---------|------------|
| Wrangling | Proceso de limpiar, transformar y preparar datos en bruto para el analisis |
| Valor nulo | Ausencia de un valor en un campo de datos |
| Duplicado | Registro que aparece mas de una vez representando la misma entidad |
| Outlier | Valor que se aleja significativamente del resto de la distribucion |
| Normalizacion | Escalar valores a un rango comun para poder comparar variables distintas |
| Imputacion | Reemplazar un valor nulo con un valor estimado (media, mediana, moda) |
| Encoding | Convertir una variable categorica en representacion numerica |
| Agregacion | Resumir datos de un nivel granular a un nivel mas alto (suma, media, conteo) |
| Power Query | Herramienta de Excel para transformar datos sin escribir formulas |
| OpenRefine | Herramienta gratuita especializada en deteccion y correccion de inconsistencias en datos |

---

## Lo mas importante de este modulo

El wrangling ocupa la mayor parte del tiempo real de un analista.
No es el trabajo mas visible ni el mas reconocido, pero un analisis
construido sobre datos mal limpiados produce conclusiones equivocadas
aunque el analisis tecnico sea perfecto.

La regla de oro: **entender el dato antes de transformarlo**. Antes de
eliminar un outlier o rellenar un nulo, hay que preguntarse por que existe
ese valor. Puede ser un error, pero tambien puede ser el hallazgo mas
importante del analisis.
