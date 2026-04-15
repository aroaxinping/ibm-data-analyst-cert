# Modulo 2: Data Quality and Data Wrangling in Spreadsheets

**Semana:** 1-2
**Duracion estimada:** 3 horas

---

## De que va este modulo

La limpieza de datos en Excel. Cubre como detectar y tratar los problemas
mas comunes que tiene cualquier dataset real: duplicados, valores vacios,
tipos de datos incorrectos, textos con espacios extra o inconsistencias
de formato. Este modulo es el mas practico del curso — es exactamente lo
que se hace en el proyecto final con el dataset de Montgomery.

---

## 1. Duplicados

Los duplicados son filas que representan el mismo registro mas de una vez.
Pueden ser errores de entrada, importaciones dobles o joins mal hechos.

**Eliminar duplicados automaticamente:**
Datos > Quitar duplicados > seleccionar las columnas que definen unicidad.

Si se seleccionan todas las columnas: solo elimina filas identicas en todo.
Si se selecciona solo "id_pedido": elimina filas con el mismo id aunque
el resto de columnas sea diferente.

**Marcar duplicados sin eliminar:**
```
=CONTAR.SI($A$1:A1, A1) > 1
```
Esta formula en una columna auxiliar devuelve TRUE en las filas duplicadas
(la segunda aparicion en adelante). Permite revisarlos antes de eliminar.

**Encontrar duplicados con formato condicional:**
Inicio > Formato condicional > Resaltar reglas de celdas > Valores duplicados.
Util para inspeccion visual rapida.

---

## 2. Valores vacios y nulos

**Localizar celdas vacias:**
Ctrl+G (Ir a) > Especial > Celdas en blanco.
Selecciona todas las celdas vacias del rango activo de golpe.

**Comprobar si una celda esta vacia:**
```
=ESBLANCO(A1)          devuelve TRUE si A1 esta vacia
=SI(ESBLANCO(A1), "Vacio", A1)
```

**Contar vacios:**
```
=CONTAR.BLANCO(A:A)    numero de celdas vacias en la columna
```

**Estrategias de tratamiento:**

| Situacion | Estrategia |
|-----------|-----------|
| Columna critica (id, fecha) con pocos nulos | Eliminar esas filas |
| Columna numerica con nulos moderados | Rellenar con la media o mediana |
| Columna categorica | Rellenar con la moda o crear categoria "Desconocido" |
| Nulos que tienen significado | Dejar como nulo y documentarlo |

**Rellenar vacios con el valor de arriba (fill down):**
Seleccionar la columna con vacios > Ctrl+G > Especial > Celdas en blanco >
escribir `=` y flecha arriba > confirmar con Ctrl+Enter.
Esto rellena cada celda vacia con el valor de la celda inmediatamente superior.

---

## 3. Tipos de datos incorrectos

El problema mas silencioso: numeros almacenados como texto, fechas con
formato incorrecto. Excel no avisa — simplemente no los suma o los ordena mal.

**Detectar numeros como texto:**
- Estan alineados a la izquierda (los numeros van a la derecha)
- Aparece un triangulo verde en la esquina superior izquierda de la celda
- `=SUMA()` sobre ese rango da 0

**Convertir texto a numero:**
```
=VALOR(A1)             convierte el texto "42" al numero 42
=A1*1                  truco rapido: multiplicar por 1 fuerza la conversion
```

O pegado especial: copiar una celda con el numero 1 > seleccionar las
celdas a convertir > Pegado especial > Multiplicar.

**Convertir numero a texto:**
```
=TEXTO(A1, "0")        numero a texto simple
=TEXTO(A1, "DD/MM/YYYY")   fecha a texto con formato
=A1&""                 truco rapido: concatenar con cadena vacia
```

**Fechas almacenadas como texto:**
```
=FECHANUMERO("15/03/2024")    convierte el texto a numero de fecha
```
Despues hay que aplicar formato de fecha a la celda resultado.

---

## 4. Limpieza de texto

**Espacios extra:**
```
=ESPACIOS(A1)
```
Elimina espacios al inicio, al final, y reduce multiples espacios internos
a uno solo. Es la primera funcion a aplicar en cualquier columna de texto.

Esto es exactamente lo que se hace en el proyecto de Montgomery con los
nombres de departamentos que tienen dobles espacios.

**Mayusculas y minusculas:**
```
=MAYUSC(A1)         todo en mayusculas: "BARCELONA"
=MINUSC(A1)         todo en minusculas: "barcelona"
=NOMPROPIO(A1)      primera letra de cada palabra: "Barcelona Norte"
```

**Funciones de extraccion de texto:**
```
=IZQUIERDA(A1, 3)           primeros 3 caracteres
=DERECHA(A1, 4)             ultimos 4 caracteres
=EXTRAE(A1, 2, 5)           5 caracteres empezando en posicion 2
=LARGO(A1)                  numero total de caracteres
=ENCONTRAR("@", A1)         posicion del caracter buscado (distingue may/min)
=HALLAR("@", A1)            igual pero sin distinguir mayusculas
```

**Reemplazar texto:**
```
=SUSTITUIR(A1, "  ", " ")   sustituye dobles espacios por uno simple
=SUSTITUIR(A1, "Recsue", "Rescue")   corregir un typo especifico
```

**Buscar y reemplazar masivo:**
Ctrl+H > escribir el texto a buscar y el reemplazo > Reemplazar todos.
Mas rapido que formulas cuando se sabe exactamente lo que hay que cambiar.
Esto se usa en el proyecto de Montgomery para corregir los typos en masa.

**Flash Fill:**
Excel detecta el patron de lo que se esta escribiendo y completa el resto
automaticamente. Util para separar o unir columnas sin formulas.

En Montgomery: las dos columnas de Department se unifican en una sola
usando Flash Fill — se escribe el primer valor combinado en una columna
nueva y Excel completa el resto.

---

## 5. Formato condicional para detectar problemas

El formato condicional no limpia datos, pero ayuda a localizarlos visualmente
antes de limpiarlos.

**Resaltar duplicados:**
Inicio > Formato condicional > Resaltar reglas de celdas > Valores duplicados

**Resaltar celdas vacias:**
Inicio > Formato condicional > Nueva regla > Dar formato solo a celdas que
contengan > Valor de celda: en blanco

**Escala de colores para detectar outliers:**
Inicio > Formato condicional > Escalas de color
Los valores mas altos apareceran en un color y los mas bajos en otro,
haciendo facil identificar extremos.

---

## Lo que se aplica en el proyecto final (Montgomery)

El dataset de Montgomery Fleet Equipment Inventory tiene exactamente los
problemas de este modulo:

- Filas vacias intercaladas entre los datos
- Duplicados exactos
- Typos en nombres de departamentos (`Rehabilltation`, `Recsue`, `Servcies`,
  `Enviromnental`, `VehicleEquipment`)
- Dobles espacios en los nombres
- La columna Department partida en dos columnas que hay que unificar

Las herramientas usadas: eliminar filas vacias manualmente, Datos > Quitar
duplicados, Ctrl+H para los typos, Flash Fill para unificar la columna.

---

## Glosario del modulo

| Termino | Definicion |
|---------|------------|
| Duplicado | Fila que representa el mismo registro mas de una vez |
| ESBLANCO | Funcion que devuelve TRUE si la celda esta vacia |
| CONTAR.BLANCO | Funcion que cuenta el numero de celdas vacias en un rango |
| ESPACIOS | Funcion que elimina espacios extra al inicio, final y dobles internos |
| SUSTITUIR | Funcion que reemplaza un texto por otro dentro de una cadena |
| VALOR | Funcion que convierte un texto que parece numero en numero real |
| NOMPROPIO | Funcion que pone en mayuscula la primera letra de cada palabra |
| Flash Fill | Funcion de Excel que detecta patrones y completa datos automaticamente |
| Formato condicional | Formato visual aplicado automaticamente segun el valor de la celda |

---

## Lo mas importante de este modulo

`=ESPACIOS()` es la primera funcion a aplicar a cualquier columna de texto
antes de hacer cualquier busqueda o comparacion. Un espacio invisible al final
de un nombre hace que dos valores identicos no se reconozcan como iguales,
rompiendo los BUSCARV y los CONTAR.SI de forma silenciosa.
