# Quiz de Practica — Modulo 1: Introduction to Spreadsheets

---

**1. La celda C3 contiene `=A3+B3`. Se copia esa formula a D5.
¿Que formula aparece en D5?**

<details>
<summary>Respuesta</summary>

`=B5+C5`

Al copiar de C3 a D5, la referencia se desplaza una columna a la derecha
(de C a D) y dos filas hacia abajo (de 3 a 5). Como las referencias son
relativas, se ajustan en la misma proporcion.

</details>

---

**2. Se quiere calcular el precio con IVA para una lista de productos.
El IVA (21%) esta en la celda F1. La formula en C2 es `=B2*F1`.
Al copiar a C3, C4... el resultado es incorrecto. ¿Por que y como se arregla?**

<details>
<summary>Respuesta</summary>

Porque `F1` es una referencia relativa. Al copiar C2 a C3, la formula
pasa a ser `=B3*F2`, y F2 probablemente esta vacia. El IVA desaparece.

La correccion: bloquear la referencia al IVA con `$`.
Formula correcta en C2: `=B2*$F$1`

Al copiar, `B2` se ajusta (B3, B4...) pero `$F$1` se mantiene siempre.

</details>

---

**3. ¿Cual es la diferencia entre `=CONTAR(A:A)` y `=CONTARA(A:A)`?**

<details>
<summary>Respuesta</summary>

- `=CONTAR(A:A)` cuenta solo las celdas que contienen **numeros**.
- `=CONTARA(A:A)` cuenta todas las celdas que **no estan vacias**,
  independientemente del tipo de dato (texto, numeros, fechas, booleanos).

Si la columna A tiene nombres de clientes (texto), `CONTAR` devuelve 0
y `CONTARA` devuelve el numero de nombres.

</details>

---

**4. Una columna tiene 500 filas de datos. Se quiere contar cuantas
corresponden a la region "Norte". ¿Que formula usar?**

<details>
<summary>Respuesta</summary>

`=CONTAR.SI(A2:A501, "Norte")`

O usando toda la columna: `=CONTAR.SI(A:A, "Norte")`

</details>

---

**5. Una celda muestra el error `#REF!`. ¿Que ha pasado probablemente?**

<details>
<summary>Respuesta</summary>

La celda que referenciaba la formula ya no existe. Lo mas comun: se elimino
una columna o fila que formaba parte del rango de la formula.

Por ejemplo: la formula `=A1+C1` en la celda D1. Si se elimina la columna C,
la formula pasa a ser `=A1+#REF!` porque ya no existe la columna referenciada.

</details>

---

**6. ¿Que referencia mixta usaria para que al copiar una formula hacia abajo
la columna se quede fija en A pero la fila pueda cambiar?**

<details>
<summary>Respuesta</summary>

`$A1` — el `$` delante de la letra bloquea la columna (A siempre),
pero el numero de fila sin `$` se ajusta al copiar hacia abajo.

Util por ejemplo en tablas donde las columnas tienen un significado fijo
pero se quiere aplicar la misma formula a cada fila.

</details>

---

**7. Verdadero o falso: `=SUMA(A1:A10)` y `=A1+A2+A3+A4+A5+A6+A7+A8+A9+A10`
producen siempre el mismo resultado.**

<details>
<summary>Respuesta</summary>

**Verdadero**, en terminos de resultado matematico son equivalentes.

Pero `SUMA` es mucho mejor en la practica:
- Mas concisa y legible
- Si se insertan filas dentro del rango, SUMA las incluye automaticamente
- La version con + no se actualiza si se insertan filas en medio

</details>
