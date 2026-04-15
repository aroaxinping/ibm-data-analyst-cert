# Actividades — Modulo 3: Analyzing Data with Spreadsheets

---

## Actividad 1: Escribir las formulas

Para cada pregunta, escribir la formula correcta. Asumir que los datos
de ventas estan en A:E con encabezados: id, region, producto, cantidad, precio.

| Pregunta | Formula |
|----------|---------|
| Suma de cantidad vendida en la region Sur | `=SUMAR.SI(B:B,"Sur",D:D)` |
| Numero de pedidos de Laptop | `=CONTAR.SI(C:C,"Laptop")` |
| Precio medio de productos con precio mayor de 100 | `=PROMEDIO.SI(E:E,">100")` |
| Suma de cantidad donde region es Norte Y producto es Monitor | `=SUMAR.SI.CONJUNTO(D:D,B:B,"Norte",C:C,"Monitor")` |
| Clasificar el precio: "Caro" si >500, "Medio" si >100, "Barato" si no | `=SI.CONJUNTO(E2>500,"Caro",E2>100,"Medio",VERDADERO,"Barato")` |
| BUSCARV para traer el nombre del producto desde tabla en G:H | `=BUSCARV(C2,$G$2:$H$50,2,0)` |
| Lo mismo pero sin error si no encuentra | `=IFERROR(BUSCARV(C2,$G$2:$H$50,2,0),"No encontrado")` |
| Correlacion entre cantidad vendida y precio | `=COEF.DE.CORREL(D2:D100,E2:E100)` |

---

## Actividad 2: Diagnosticar errores de formula

Para cada situacion, identificar por que no funciona y como arreglarlo.

**Caso A:**
Formula: `=BUSCARV(A2, E2:G100, 2, 0)` — da #N/A para la mayoria de valores.
Los datos de busqueda (columna A) tienen espacios extra al final.

*Causa:* espacios invisibles hacen que "Madrid " != "Madrid".
*Solucion:* `=BUSCARV(ESPACIOS(A2), $E$2:$G$100, 2, 0)`

---

**Caso B:**
Formula: `=SI(A1>100, "Alto", SI(A1>50, "Medio", SI(A1>0, "Bajo", "Negativo")))`
Funciona pero al insertar una columna en la tabla, el BUSCARV interno falla.

*Causa:* las referencias no estan bloqueadas con $.
*Solucion:* Bloquear el rango de la tabla con $ y revisar si hay BUSCARV
dentro de los SI que tampoco esten bloqueados.

---

**Caso C:**
`=PROMEDIO.SI(B:B, "norte", C:C)` devuelve 0 aunque hay registros con "Norte".

*Causa:* PROMEDIO.SI distingue mayusculas en algunos casos; el criterio
"norte" no coincide con "Norte".
*Solucion:* usar `=PROMEDIO.SI(B:B,"Norte",C:C)` con la misma capitalizacion
que tienen los datos, o estandarizar primero los datos con `=NOMPROPIO()`.

---

## Actividad 3: INDICE + COINCIDIR vs BUSCARV

Dado este layout de tabla donde el resultado esta a la izquierda del criterio:

```
Columna A: Nombre producto
Columna B: Descripcion
Columna C: Codigo producto  <- criterio de busqueda
```

Se quiere buscar el nombre (A) dado el codigo (C).

**Con BUSCARV:** no es posible directamente porque A esta a la izquierda de C.

**Con INDICE + COINCIDIR:**
```
=INDICE($A$2:$A$100, COINCIDIR(codigo_buscado, $C$2:$C$100, 0))
```

Explicacion paso a paso:
1. `COINCIDIR(codigo, $C$2:$C$100, 0)` devuelve el numero de fila donde
   esta ese codigo dentro del rango C2:C100. Por ejemplo: fila 5.
2. `INDICE($A$2:$A$100, 5)` devuelve el valor de la celda A que esta
   en la posicion 5 del rango A2:A100, que es el nombre del producto.

---

## Actividad 4: Aplicar estadisticas al dataset de Montgomery

Con el dataset limpio de la Part 1 del final assignment:

| Estadistica | Resultado real | Formula usada |
|-------------|---------------|---------------|
| Suma de Equipment Count | 1582 | `=SUMA(C2:C50)` o AutoSum |
| Media de Equipment Count | 32.29 | `=PROMEDIO(C2:C50)` o AutoSum |
| Minimo de Equipment Count | 1 | `=MIN(C2:C50)` o AutoSum |
| Maximo de Equipment Count | 379 | `=MAX(C2:C50)` o AutoSum |
| Numero de filas con datos | 49 | `=CONTAR(C2:C50)` o AutoSum |

El departamento con 379 unidades es el que domina el inventario —
visible directamente en la pivot table ordenada de forma descendente.
