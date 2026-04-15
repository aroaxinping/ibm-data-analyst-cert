# Practica Excel — Course 2

Ejercicios practicos del curso. Los archivos .xlsx no se suben al repo
(ver .gitignore), pero aqui se documentan las formulas usadas y los
hallazgos de cada ejercicio.

---

## Ejercicio 1: Limpieza de un dataset de ventas

**Dataset:** archivo de ventas con duplicados, campos vacios y fechas mal formateadas.

**Pasos aplicados:**
1. Eliminar duplicados: Datos > Quitar duplicados por columna `Order ID`
2. Rellenar `Region` vacia: filtrar en blanco, rellenar con valor mas frecuente
3. Convertir columna `Revenue` de texto a numero: `=VALOR(ESPACIOS(A2))`
4. Estandarizar `Date`: `=TEXTO(FECHANUMERO(A2), "DD/MM/YYYY")`

## Ejercicio 2: BUSCARV y tabla de categorias

**Objetivo:** añadir columna de categoria de producto buscando en tabla auxiliar.

```
=BUSCARV(B2, $H$2:$I$50, 2, 0)
```

Donde `B2` es el codigo de producto y la tabla `H2:I50` contiene la relacion
codigo -> categoria.

## Ejercicio 3: Tabla dinamica de ventas por region y categoria

**Configuracion:**
- Filas: Region
- Columnas: Categoria
- Valores: Suma de Revenue
- Filtros: Año

---

## Final Assignment — Montgomery Fleet Equipment Inventory

Entrega final del curso: limpieza de datos + pivot tables.
Ver [`final-assignment-montgomery-fleet/`](final-assignment-montgomery-fleet/)
para los archivos START/END, el detalle de cada tarea y las capturas
antes/despues.
