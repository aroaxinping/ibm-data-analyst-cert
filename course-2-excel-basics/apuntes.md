# Apuntes — Course 2: Excel Basics for Data Analysis

**Duracion:** 11 horas
**Modulos:** 4

---

## Que cubre este curso

Excel y Google Sheets como herramientas de analisis de datos. No es un curso
de Excel en general — esta enfocado en las funciones que realmente usa un
analista: limpiar datos, calcular metricas, filtrar y resumir con tablas
dinamicas.

---

## Modulo 1: Introduction to Spreadsheets

**Estructura basica:**
- **Celda:** unidad basica. Referenciada por columna + fila (A1, B3, C10)
- **Rango:** grupo de celdas (A1:A10, B2:D5)
- **Hoja:** cada pestana de un archivo
- **Libro:** el archivo completo (.xlsx)

**Tipos de datos en una celda:**
- Texto (string)
- Numero (entero o decimal)
- Fecha / hora
- Booleano (TRUE/FALSE)
- Formula (empieza con `=`)

**Referencias:**

| Tipo | Ejemplo | Comportamiento al copiar |
|------|---------|--------------------------|
| Relativa | `A1` | Se ajusta automaticamente |
| Absoluta | `$A$1` | No cambia nunca |
| Mixta columna | `$A1` | Columna fija, fila se ajusta |
| Mixta fila | `A$1` | Fila fija, columna se ajusta |

Usar `$` con criterio: si una formula referencia un parametro fijo (tasa,
porcentaje), usar referencia absoluta para poder copiar sin errores.

**Formulas basicas:**

```
=SUMA(A1:A10)           -> suma el rango
=PROMEDIO(B2:B20)       -> media aritmetica
=MAX(C1:C100)           -> valor maximo
=MIN(C1:C100)           -> valor minimo
=CONTAR(A:A)            -> cuenta celdas con numeros
=CONTARA(A:A)           -> cuenta celdas no vacias
=CONTAR.SI(A:A,"SI")    -> cuenta celdas que cumplen condicion
```

---

## Modulo 2: Data Quality and Data Wrangling in Spreadsheets

Limpieza de datos directamente en Excel / Sheets.

**Detectar y tratar problemas comunes:**

**Duplicados:**
- Excel: Datos > Quitar duplicados
- Formula para marcar duplicados: `=CONTAR.SI($A$1:A1, A1) > 1`

**Valores nulos / vacios:**
- Localizar: Ctrl+G (Ir a) > Especial > Celdas en blanco
- Tratar: rellenar con valor anterior, con media, o eliminar fila segun el caso

**Tipos de datos incorrectos:**
- Texto que deberia ser numero: multiplicar por 1 (`=A1*1`) o usar `VALOR()`
- Numero que deberia ser texto: concatenar con "" (`=A1&""`)
- Fechas como texto: `=FECHANUMERO()` o formato personalizado

**Espacios extra:**
- `=ESPACIOS(A1)` — elimina espacios al principio, al final y dobles internos

**Mayusculas/minusculas:**
- `=MAYUSC(A1)` — todo mayusculas
- `=MINUSC(A1)` — todo minusculas
- `=NOMPROPIO(A1)` — primera letra de cada palabra en mayuscula

**Funciones de texto utiles:**

```
=IZQUIERDA(A1, 3)          -> primeros 3 caracteres
=DERECHA(A1, 4)             -> ultimos 4 caracteres
=EXTRAE(A1, 2, 5)           -> 5 caracteres desde posicion 2
=LARGO(A1)                  -> numero de caracteres
=ENCONTRAR("-", A1)         -> posicion del caracter buscado
=SUSTITUIR(A1, "viejo", "nuevo")  -> reemplazar texto
=CONCATENAR(A1, " ", B1)   -> unir textos
```

---

## Modulo 3: Analyzing Data with Spreadsheets

Funciones de analisis y busqueda.

**Funciones logicas:**

```
=SI(condicion, valor_si_verdadero, valor_si_falso)
=SI(A1>100, "Alto", "Bajo")

=Y(condicion1, condicion2)     -> ambas deben ser verdad
=O(condicion1, condicion2)     -> basta con que una sea verdad
=NO(condicion)                 -> invierte el resultado

=SI.CONJUNTO(
  A1>100, "Alto",
  A1>50, "Medio",
  A1<=50, "Bajo"
)
```

**Funciones de busqueda:**

```
=BUSCARV(valor, rango_tabla, num_columna, [exacto])
=BUSCARV(A2, $E$2:$F$100, 2, 0)
```

- Busca `A2` en la primera columna del rango `E2:F100`
- Devuelve el valor de la columna 2 del rango
- El `0` al final significa coincidencia exacta
- Limitacion: solo busca hacia la derecha

```
=BUSCARH(valor, rango_tabla, num_fila, [exacto])
```

- Igual que BUSCARV pero busca horizontalmente

```
=INDICE(rango, num_fila, num_columna)
=COINCIDIR(valor, rango, tipo)

=INDICE($B$2:$B$100, COINCIDIR(A2, $A$2:$A$100, 0))
```

Combinacion INDICE+COINCIDIR: mas flexible que BUSCARV, puede buscar en
cualquier direccion y no se rompe si se insertan columnas.

**Funciones estadisticas:**

```
=MEDIANA(A1:A100)
=MODA(A1:A100)
=DESVEST(A1:A100)            -> desviacion tipica muestral
=DESVESTP(A1:A100)           -> desviacion tipica poblacional
=VAR(A1:A100)                -> varianza muestral
=PERCENTIL(A1:A100, 0.75)    -> percentil 75
=CUARTIL(A1:A100, 1)         -> primer cuartil (Q1)
=COEF.DE.CORREL(A1:A100, B1:B100)  -> correlacion de Pearson
```

**Filtros:**
- Filtro basico: Datos > Filtro (desplegable en cada columna)
- Filtro avanzado: permite condiciones mas complejas y copiar resultados
- `=FILTRAR(rango, condicion)` — funcion dinamica (Excel 365 / Sheets)

---

## Modulo 4: Pivot Tables

Las tablas dinamicas son la herramienta mas potente de Excel para el analisis
exploratorio rapido.

**Como crear una tabla dinamica:**

1. Seleccionar el dataset (con encabezados)
2. Insertar > Tabla dinamica
3. Elegir donde colocarla (nueva hoja recomendado)
4. Arrastrar campos a las zonas: Filas, Columnas, Valores, Filtros

**Las cuatro zonas:**

| Zona | Para que |
|------|----------|
| Filas | Agrupa los datos por esta dimension (aparece como filas) |
| Columnas | Segunda dimension de agrupacion (aparece como columnas) |
| Valores | Metrica a calcular (suma, media, conteo...) |
| Filtros | Filtra todo el informe por este campo |

**Calculos disponibles en Valores:**
- Suma (por defecto para numeros)
- Recuento (por defecto para texto)
- Media
- Max / Min
- Producto
- Desviacion tipica

**Mostrar valores como:**
- % del total general
- % del total de fila
- % del total de columna
- Diferencia respecto a...
- Acumulado

**Segmentaciones de datos (Slicers):**
Botones visuales que filtran la tabla dinamica. Se insertan desde
Analizar > Insertar segmentacion de datos. Especialmente utiles cuando
el informe lo ve alguien que no sabe de Excel.

**Graficos dinamicos:**
Un grafico vinculado a una tabla dinamica que se actualiza automaticamente.
Misma logica que el grafico normal pero conectado a la tabla.

---

## Esquema resumido del curso

```
COURSE 2: EXCEL BASICS
|
+-- Estructura de la hoja de calculo
|     Referencias relativas vs absolutas
|
+-- Limpieza de datos
|     Duplicados, nulos, tipos incorrectos, texto extra
|     Funciones: ESPACIOS, SUSTITUIR, IZQUIERDA, LARGO
|
+-- Analisis con formulas
|     Logicas: SI, Y, O, SI.CONJUNTO
|     Busqueda: BUSCARV, INDICE+COINCIDIR
|     Estadisticas: MEDIANA, DESVEST, PERCENTIL, COEF.DE.CORREL
|
+-- Tablas dinamicas
      Filas, Columnas, Valores, Filtros
      Slicers, graficos dinamicos
```

---

## Glosario

| Termino | Definicion |
|---------|------------|
| Celda | Unidad basica de una hoja de calculo, identificada por columna y fila |
| Rango | Conjunto de celdas contiguas referenciadas como A1:B10 |
| Referencia absoluta | Referencia que no cambia al copiar la formula ($A$1) |
| BUSCARV | Funcion que busca un valor en la primera columna de una tabla y devuelve un valor de otra columna |
| INDICE+COINCIDIR | Alternativa mas flexible a BUSCARV que permite buscar en cualquier direccion |
| Tabla dinamica | Herramienta para resumir, agrupar y analizar datos sin escribir formulas |
| Slicer | Elemento visual que filtra una tabla o grafico dinamico |
| Outlier | Valor extremo que se aleja significativamente de la mayoria |
| Imputacion | Proceso de rellenar valores faltantes con un valor estimado |

---

## Errores comunes

- **Usar BUSCARV cuando hay columnas a la izquierda del valor de busqueda:**
  BUSCARV solo busca de izquierda a derecha. Si la columna con el resultado
  esta a la izquierda del criterio, usar INDICE+COINCIDIR.
- **No bloquear referencias absolutas en formulas que se van a copiar:**
  Si una formula referencia una tabla de parametros y no se bloquea con $,
  la referencia se desplaza al copiar y produce errores silenciosos.
- **Olvidar actualizar la tabla dinamica:** los datos pueden cambiar pero
  la tabla no se actualiza sola. Clic derecho > Actualizar, o configurar
  actualizacion automatica al abrir.
- **Mezclar tipos de datos en una columna:** tener numeros y texto en la
  misma columna rompe las funciones de suma y busqueda. Siempre un tipo
  por columna.

---

## Conexion con otros cursos

- Las operaciones de limpieza de datos de este curso (tratar nulos,
  duplicados, tipos incorrectos) se hacen con pandas en Python en el curso 7.
  Misma logica, distinta herramienta.
- Las funciones estadisticas (media, mediana, desviacion tipica, correlacion)
  reaparecen en los cursos 7 y 8 implementadas con NumPy y pandas.
- Las tablas dinamicas tienen su equivalente en Python: `df.groupby()` y
  `df.pivot_table()` en pandas.
- El concepto de filtrar y segmentar datos es la base de las queries SQL del
  curso 6 (WHERE, GROUP BY, HAVING).
