# Quiz de Practica — Modulo 2: Data Quality and Data Wrangling in Spreadsheets

---

**1. Una columna de precios suma 0 con `=SUMA()` aunque visualmente
tiene numeros. ¿Cual es el problema y como se soluciona?**

<details>
<summary>Respuesta</summary>

Los numeros estan almacenados como **texto**. Excel no los reconoce como
valores numericos y no los suma.

Senales que lo confirman: estan alineados a la izquierda (los numeros
van a la derecha), puede haber un triangulo verde en la esquina de cada celda.

Soluciones:
- `=VALOR(A1)` en una columna auxiliar para convertirlos
- Seleccionar las celdas > Datos > Texto en columnas > Finalizar (fuerza
  la conversion sin cambiar nada)
- Multiplicar por 1: `=A1*1`

</details>

---

**2. Se tiene una lista de 1.000 nombres de ciudad con espacios extra
antes y despues. ¿Que formula elimina esos espacios?**

<details>
<summary>Respuesta</summary>

`=ESPACIOS(A1)` aplicada en una columna auxiliar, luego copiar y pegar
como valores sobre la columna original (Ctrl+C > Pegado especial > Valores).

`ESPACIOS` elimina espacios al inicio, al final y reduce multiples espacios
internos a uno solo.

</details>

---

**3. El dataset tiene la columna "id_cliente" con estos valores:
1001, 1002, 1001, 1003, 1002. ¿Que formula en una columna auxiliar
marcaria los duplicados?**

<details>
<summary>Respuesta</summary>

```
=CONTAR.SI($A$1:A1, A1) > 1
```

Colocada en B1 y arrastrada hacia abajo. Devuelve:
- B1: FALSE (1001 aparece por primera vez)
- B2: FALSE (1002 primera vez)
- B3: TRUE (1001 ya aparecio antes)
- B4: FALSE (1003 primera vez)
- B5: TRUE (1002 ya aparecio)

La clave es `$A$1:A1` — el inicio del rango esta bloqueado pero el final
se expande al copiar, comparando cada valor contra todos los anteriores.

</details>

---

**4. Una columna de fechas tiene valores como "15 de marzo de 2024" (texto).
¿Como convertirlos a fecha real de Excel?**

<details>
<summary>Respuesta</summary>

Si el formato es consistente, `=FECHANUMERO(A1)` puede funcionar,
aunque depende de la configuracion regional de Excel.

La forma mas fiable: Datos > Texto en columnas > Siguiente > Siguiente >
seleccionar "Fecha" como formato de columna > Finalizar.

Despues hay que aplicar formato de fecha a las celdas resultado.

</details>

---

**5. En el proyecto de Montgomery, los departamentos "Transportation" y
"Transportation " (con espacio al final) se tratan como departamentos
distintos en la tabla dinamica. ¿Como se arregla?**

<details>
<summary>Respuesta</summary>

Con `=ESPACIOS()` sobre la columna de departamentos para eliminar el
espacio extra. Tambien se puede usar Ctrl+H (Buscar y reemplazar) para
reemplazar "Transportation " (con espacio) por "Transportation" (sin espacio),
pero es menos robusto si hay mas variantes ocultas.

La raiz del problema: un espacio invisible al final hace que Excel trate
valores identicos como distintos en cualquier funcion de agrupacion o busqueda.

</details>

---

**6. ¿Que hace exactamente Flash Fill y cuando es util?**

<details>
<summary>Respuesta</summary>

Flash Fill detecta el patron de lo que el usuario esta escribiendo en una
columna y completa automaticamente el resto de filas siguiendo ese patron.

Se activa: empezar a escribir en la primera celda de una columna nueva,
y Excel sugiere el relleno automatico. Confirmar con Enter o activar desde
Datos > Relleno rapido.

Util para:
- Unir dos columnas en una (nombre + apellido -> nombre completo)
- Separar una columna en dos (email -> extraer el dominio)
- Reformatear texto (numeros de telefono, codigos...)

En el proyecto de Montgomery se usa para unificar las dos columnas
de Department en una sola.

</details>

---

**7. ¿Que diferencia hay entre Buscar y reemplazar (Ctrl+H) y la
funcion `=SUSTITUIR()`?**

<details>
<summary>Respuesta</summary>

- **Ctrl+H** modifica los datos originales directamente, de forma permanente.
  Es rapido cuando se sabe exactamente lo que hay que cambiar.
  No es reversible (excepto con Ctrl+Z inmediatamente).

- **`=SUSTITUIR()`** crea una formula en una nueva columna con el texto
  modificado, sin tocar el original. Es no destructivo y permite ver
  el antes y despues. Requiere luego copiar y pegar como valores si se
  quiere reemplazar el original.

Para correcciones masivas en produccion, `SUSTITUIR` en columna auxiliar
es mas seguro. Para correcciones puntuales rapidas, Ctrl+H.

</details>
