# Actividades — Modulo 1: Introduction to Spreadsheets

---

## Actividad 1: Identificar el tipo de referencia necesaria

Para cada situacion, decidir si la referencia debe ser relativa, absoluta o mixta.

| Situacion | Tipo de referencia | Por que |
|-----------|--------------------|---------|
| Formula que suma las ventas de cada fila, y se va a copiar hacia abajo | Relativa | Cada fila debe sumar sus propios valores |
| Referencia al tipo de cambio EUR/USD en F1, usada en 500 formulas | Absoluta ($F$1) | El tipo de cambio es el mismo para todas las filas |
| Tabla de multiplicacion: columna fija, fila variable | Mixta ($A1 o A$1) | Una dimension se fija, la otra se ajusta |
| Nombre de la hoja en un encabezado | No aplica formula | Es texto estatico |
| Porcentaje de descuento en E2, aplicado a cada fila de precios | Absoluta ($E$2) | El descuento es igual para todas las filas |

---

## Actividad 2: Interpretar errores

Para cada error, identificar la causa probable y la solucion.

| Error | Causa probable | Solucion |
|-------|---------------|----------|
| `#DIV/0!` en una columna de "precio por unidad" | La columna de unidades tiene ceros o celdas vacias | Usar `=SI(B2=0, "", A2/B2)` para evitar la division entre cero |
| `#VALOR!` al sumar una columna numerica | Alguna celda de la columna tiene texto en vez de numero | Localizar y limpiar los valores de texto; usar `VALOR()` si es necesario |
| `#N/A` en un BUSCARV | El valor buscado no existe en la tabla | Verificar ortografia, espacios extra, o usar `IFERROR` para mostrar un valor alternativo |
| `#NOMBRE?` en `=SUMB(A1:A10)` | Nombre de funcion mal escrito ("SUMB" no existe) | Corregir a `=SUMA(A1:A10)` |
| `#REF!` despues de reorganizar columnas | Se elimino o movio una columna que formaba parte de la formula | Revisar y actualizar las referencias de la formula |

---

## Actividad 3: Formulas de conteo y suma

Dado este dataset hipotetico de pedidos:

| id_pedido | region | producto | cantidad | precio_unit |
|-----------|--------|----------|----------|-------------|
| 1001 | Norte | Laptop | 2 | 899 |
| 1002 | Sur | Raton | 5 | 29 |
| 1003 | Norte | Monitor | 1 | 349 |
| 1004 | Este | Laptop | 3 | 899 |
| 1005 | Sur | Teclado | 4 | 59 |
| 1006 | Norte | Raton | 10 | 29 |

Escribir la formula para cada pregunta (asumiendo que los datos estan en A1:E7 con encabezados en fila 1):

| Pregunta | Formula |
|----------|---------|
| Total de pedidos | `=CONTARA(A2:A7)` o `=CONTAR(A2:A7)` |
| Suma total de cantidad | `=SUMA(D2:D7)` → 25 |
| Pedidos de la region Norte | `=CONTAR.SI(B2:B7,"Norte")` → 3 |
| Total de cantidad vendida en el Norte | `=SUMAR.SI(B2:B7,"Norte",D2:D7)` → 13 |
| Precio unitario maximo | `=MAX(E2:E7)` → 899 |
| Precio unitario minimo | `=MIN(E2:E7)` → 29 |
| Media de precio unitario | `=PROMEDIO(E2:E7)` → 377.3 |

---

## Actividad 4: Atajo de referencia absoluta

Practica con F4.

Al escribir una formula, hacer clic dentro de una referencia y pulsar F4
alterna entre los cuatro tipos:

```
A1    ->  $A$1  ->  A$1  ->  $A1  ->  A1  (vuelve a empezar)
```

Ejercicio: escribir `=A1*B1` en la celda C1, poner el cursor sobre `B1`
y pulsar F4 tres veces. Anotar que referencia aparece en cada pulsacion.

- F4 primera vez: `$B$1` (absoluta completa)
- F4 segunda vez: `B$1` (fila fija)
- F4 tercera vez: `$B1` (columna fija)
- F4 cuarta vez: `B1` (relativa, vuelve al inicio)
