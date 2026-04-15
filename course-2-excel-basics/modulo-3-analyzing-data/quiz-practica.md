# Quiz de Practica — Modulo 3: Analyzing Data with Spreadsheets

---

**1. La columna B tiene el tipo de cliente ("Premium", "Estandar", "Basico").
La columna C tiene el importe. ¿Que formula calcula el importe medio
solo para los clientes Premium?**

<details>
<summary>Respuesta</summary>

`=PROMEDIO.SI(B:B, "Premium", C:C)`

</details>

---

**2. Se quiere clasificar una nota (en A1) como: "Sobresaliente" si es >= 9,
"Notable" si es >= 7, "Aprobado" si es >= 5, y "Suspenso" si es menor.
¿Como se escribe con SI.CONJUNTO?**

<details>
<summary>Respuesta</summary>

```
=SI.CONJUNTO(
    A1>=9, "Sobresaliente",
    A1>=7, "Notable",
    A1>=5, "Aprobado",
    VERDADERO, "Suspenso"
)
```

El orden importa: SI.CONJUNTO evalua de arriba abajo y devuelve el
primer resultado que se cumple. Si se pusiera el Aprobado antes que
el Notable, un 8 devolveria "Aprobado" en vez de "Notable".

El ultimo par `VERDADERO, "Suspenso"` captura cualquier valor que
no haya cumplido ninguna condicion anterior.

</details>

---

**3. BUSCARV da `#N/A` para algunos valores. ¿Como se evita que
ese error aparezca en el informe, mostrando "Sin datos" en su lugar?**

<details>
<summary>Respuesta</summary>

Envolver el BUSCARV en IFERROR:

```
=IFERROR(BUSCARV(A2, $E$2:$G$100, 2, 0), "Sin datos")
```

Si el BUSCARV encuentra el valor, devuelve el resultado normal.
Si da cualquier error (incluido #N/A), devuelve "Sin datos".

</details>

---

**4. La tabla de referencia tiene el codigo de producto en la columna C
y el nombre en la columna A (el nombre esta a la izquierda del codigo).
¿Por que BUSCARV no funciona aqui y como se soluciona?**

<details>
<summary>Respuesta</summary>

BUSCARV solo busca de izquierda a derecha — el valor buscado debe estar
en la primera columna de la tabla, y el resultado debe estar a su derecha.
Si el resultado (nombre) esta a la izquierda del criterio (codigo), BUSCARV
no puede hacerlo.

Solucion con INDICE+COINCIDIR:
```
=INDICE($A$2:$A$100, COINCIDIR(codigo_buscado, $C$2:$C$100, 0))
```

COINCIDIR encuentra la fila donde esta el codigo, e INDICE devuelve
el nombre en esa misma fila de la columna A.

</details>

---

**5. ¿Que devuelve `=COEF.DE.CORREL(A1:A10, B1:B10)` si el resultado es -0.87?**

<details>
<summary>Respuesta</summary>

Una **correlacion negativa fuerte** entre las dos variables.

- El signo negativo indica que cuando una variable sube, la otra tiende
  a bajar (relacion inversa)
- El valor 0.87 (cercano a 1 en valor absoluto) indica que la relacion
  es bastante fuerte

Ejemplo real: mayor kilometraje del coche (A) suele correlacionarse con
menor precio de venta (B) — correlacion negativa.

</details>

---

**6. ¿Cual es la diferencia entre `=DESVEST(A1:A100)` y `=DESVESTP(A1:A100)`?
¿Cual usar en la mayoria de casos?**

<details>
<summary>Respuesta</summary>

- `DESVEST`: calcula la desviacion tipica **muestral** (divide entre n-1).
  Se usa cuando los datos son una muestra de una poblacion mayor.

- `DESVESTP`: calcula la desviacion tipica **poblacional** (divide entre n).
  Se usa cuando los datos son toda la poblacion completa.

En la practica casi siempre se usa `DESVEST`, porque raramente se tienen
todos los datos posibles del universo — casi siempre es una muestra.

</details>

---

**7. La funcion `=FILTRAR(A2:D100, C2:C100="Madrid")` se actualiza
automaticamente cuando cambian los datos. ¿En que se diferencia del
filtro manual (Datos > Filtro)?**

<details>
<summary>Respuesta</summary>

- El **filtro manual** oculta filas — los datos siguen ahi pero no se ven.
  Se pierde si alguien limpia los filtros. No es una formula.

- `FILTRAR()` crea un **rango dinamico nuevo** con solo las filas que
  cumplen la condicion. Es una formula, no modifica los datos originales,
  se puede colocar en otra hoja y se actualiza automaticamente.

La desventaja de FILTRAR: solo esta disponible en Excel 365/2021 y
Google Sheets, no en versiones antiguas de Excel.

</details>
