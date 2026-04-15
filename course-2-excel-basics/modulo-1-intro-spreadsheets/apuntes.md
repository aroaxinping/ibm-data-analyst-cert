# Modulo 1: Introduction to Spreadsheets

**Semana:** 1
**Duracion estimada:** 2.5 horas

---

## De que va este modulo

Punto de partida del curso. Explica la estructura de una hoja de calculo,
los tipos de datos que puede contener cada celda, como funcionan las
referencias y las formulas basicas de agregacion. Sin este modulo, todo
lo que viene despues no tiene base.

---

## 1. Estructura de una hoja de calculo

**Los elementos basicos:**

- **Celda:** la unidad minima. Se identifica por letra de columna + numero
  de fila. A1 es la primera celda, B3 es la columna B fila 3.
- **Rango:** un grupo de celdas contiguas. A1:A10 es una columna de 10
  celdas. B2:D5 es un bloque de 3 columnas y 4 filas.
- **Hoja:** cada pestana dentro del archivo. Un archivo puede tener varias
  hojas con datos distintos o relacionados.
- **Libro:** el archivo completo (.xlsx en Excel, .ods en LibreOffice).

**Tipos de datos que puede contener una celda:**

| Tipo | Ejemplo | Como Excel lo reconoce |
|------|---------|----------------------|
| Numero | 42, 3.14, -5 | Alineado a la derecha |
| Texto | "Barcelona", "Laptop" | Alineado a la izquierda |
| Fecha / hora | 15/03/2024, 14:30 | Numero con formato especial |
| Booleano | TRUE, FALSE | Resultado de una comparacion |
| Formula | =A1+B1, =SUMA(A:A) | Empieza siempre con = |
| Error | #DIV/0!, #VALOR!, #REF! | Cuando algo falla |

**Tipos de error comunes:**

| Error | Causa |
|-------|-------|
| `#DIV/0!` | Division entre cero o entre una celda vacia |
| `#VALOR!` | Tipo de dato incorrecto (sumar texto con numero) |
| `#REF!` | La celda referenciada ya no existe (se elimino la columna) |
| `#NOMBRE?` | Nombre de funcion mal escrito |
| `#N/A` | BUSCARV no encontro el valor buscado |
| `#NUM!` | Operacion matematica imposible (raiz de negativo) |

---

## 2. Referencias: relativas, absolutas y mixtas

Este es uno de los conceptos mas importantes de Excel y el que mas
confusion genera al principio.

**Referencia relativa (`A1`):**
Cuando se copia la formula, la referencia se ajusta automaticamente
segun la posicion relativa de la celda de destino.

```
Celda C1: =A1+B1
Al copiar a C2: =A2+B2  (se ajusta automaticamente)
Al copiar a D1: =B1+C1  (se ajusta en columna)
```

**Referencia absoluta (`$A$1`):**
El simbolo `$` bloquea la referencia. Al copiar la formula, la referencia
no cambia nunca.

```
Celda C1: =A1*$E$1   (E1 contiene el IVA, por ejemplo)
Al copiar a C2: =A2*$E$1  (A1 se ajusta, $E$1 no cambia)
Al copiar a C3: =A3*$E$1
```

**Referencia mixta:**
Bloquea solo la fila o solo la columna.

```
$A1  ->  columna A fija, fila se ajusta
A$1  ->  fila 1 fija, columna se ajusta
```

**Regla practica:**
Usar `$` cuando la formula va a copiarse y hay una celda que debe
quedarse fija (tablas de parametros, tipos de cambio, tasas fijas...).
Si no se bloquea, la referencia se desplaza y la formula da resultados
incorrectos sin dar ningun error visible.

---

## 3. Formulas de agregacion basicas

Las formulas mas usadas en el analisis diario:

```
=SUMA(A1:A10)          suma todos los valores del rango
=PROMEDIO(B2:B20)      media aritmetica
=MAX(C1:C100)          valor maximo del rango
=MIN(C1:C100)          valor minimo del rango
=CONTAR(A:A)           cuenta celdas que contienen numeros
=CONTARA(A:A)          cuenta celdas que NO estan vacias (cualquier tipo)
=CONTAR.BLANCO(A:A)    cuenta celdas vacias
=CONTAR.SI(A:A,"SI")   cuenta celdas que cumplen una condicion
=SUMAR.SI(A:A,">100",B:B)  suma B donde A es mayor de 100
```

**CONTAR vs CONTARA:**
- `CONTAR` cuenta solo numeros
- `CONTARA` cuenta cualquier celda no vacia (texto, numeros, booleanos)
- Util para detectar cuantas filas tienen datos vs cuantas estan vacias

**CONTAR.SI con distintos criterios:**

```
=CONTAR.SI(A:A, "Madrid")       exactamente "Madrid"
=CONTAR.SI(A:A, ">100")         mayor de 100
=CONTAR.SI(A:A, "<>")           no vacio (cualquier valor)
=CONTAR.SI(A:A, "M*")           empieza por M
=CONTAR.SI(A:A, "*centro*")     contiene "centro"
```

---

## 4. Formatos y atajos utiles

**Atajos de teclado que ahorran tiempo:**

| Atajo | Accion |
|-------|--------|
| `Ctrl + Z` | Deshacer |
| `Ctrl + C / V` | Copiar / pegar |
| `Ctrl + Shift + L` | Activar / desactivar filtros |
| `Ctrl + T` | Convertir rango en tabla |
| `Ctrl + G` | Ir a (para saltar a celdas especiales) |
| `F2` | Editar la celda seleccionada |
| `F4` | Alternar entre referencias relativa / absoluta / mixta |
| `Ctrl + Flecha` | Saltar al ultimo dato de una columna o fila |
| `Ctrl + Mayus + Fin` | Seleccionar hasta el ultimo dato del libro |
| `Alt + =` | Insertar SUMA automatica |

**Formato de celdas:**
- Numero de decimales: Ctrl+1 > Numero
- Formato de fecha: Ctrl+1 > Fecha > elegir formato
- Formato de moneda: Ctrl+1 > Moneda
- Porcentaje: boton % en la barra o Ctrl+Mayus+%

---

## Glosario del modulo

| Termino | Definicion |
|---------|------------|
| Celda | Unidad basica de la hoja de calculo, identificada por columna y fila |
| Rango | Conjunto de celdas contiguas expresado como A1:B10 |
| Referencia relativa | Referencia que se ajusta automaticamente al copiar la formula |
| Referencia absoluta | Referencia bloqueada con $ que no cambia al copiar |
| Formula | Expresion que empieza con = y realiza un calculo |
| SUMA | Funcion que suma todos los valores de un rango |
| CONTARA | Funcion que cuenta todas las celdas no vacias de un rango |
| CONTAR.SI | Funcion que cuenta las celdas que cumplen una condicion especifica |
| #N/A | Error que indica que BUSCARV u otra funcion de busqueda no encontro el valor |
| #REF! | Error que indica que la celda referenciada ya no existe |

---

## Lo mas importante de este modulo

Las referencias absolutas y relativas son la base de todo lo que se
construye en Excel. Si no se entiende cuando usar `$` y cuando no,
las formulas se rompen silenciosamente al copiarlas y los resultados
son incorrectos sin ningun aviso de error.

La regla: si la formula se va a copiar y hay una celda que debe
quedarse fija (un parametro, una tasa, una tabla de referencia),
bloquear esa celda con `$`.
