# Actividades — Modulo 4: Pivot Tables

---

## Actividad 1: Las tres pivot tables del proyecto Montgomery

Documentar la configuracion exacta de cada pivot del final assignment.

### Pivot Table 1 — Suma por Department (descendente)

| Zona | Campo |
|------|-------|
| Filas | Department |
| Columnas | (vacio) |
| Valores | Suma de Equipment Count |
| Filtros | (vacio) |

**Configuracion adicional:** ordenar Valores de mayor a menor
(clic derecho > Ordenar > De mayor a menor).

**Resultado:** Transportation aparece primero con el mayor numero
de unidades. Cada departamento en una fila con su total.

---

### Pivot Table 2 — Department > Equipment Class (jerarquia)

| Zona | Campo |
|------|-------|
| Filas | Department (primero), Equipment Class (segundo — subnivel) |
| Columnas | (vacio) |
| Valores | Suma de Equipment Count |
| Filtros | (vacio) |

**Configuracion adicional:** colapsar todos los departamentos
(clic en - de cada uno) y expandir solo Transportation para ver
su desglose por Equipment Class.

---

### Pivot Table 3 — Equipment Class > Department (jerarquia invertida)

| Zona | Campo |
|------|-------|
| Filas | Equipment Class (primero), Department (segundo — subnivel) |
| Columnas | (vacio) |
| Valores | Suma de Equipment Count |
| Filtros | (vacio) |

**Configuracion adicional:** colapsar todo y expandir solo CUV
para ver que departamentos tienen vehiculos de tipo CUV.

---

## Actividad 2: Disenar pivots para un caso de negocio

**Dataset:** ventas de una cadena de supermercados con columnas:
fecha, tienda, ciudad, region, categoria, producto, unidades, precio_unit, total.

Para cada pregunta de negocio, disenar la configuracion de la pivot:

**Pregunta A:** ¿Cuanto vendio cada region el ultimo mes?

| Zona | Campo |
|------|-------|
| Filas | Region |
| Valores | Suma de Total |
| Filtros | Fecha (filtrado al ultimo mes) |

---

**Pregunta B:** ¿Que categoria vende mas en cada tienda?

| Zona | Campo |
|------|-------|
| Filas | Tienda |
| Columnas | Categoria |
| Valores | Suma de Total |

---

**Pregunta C:** ¿Cuantos productos distintos se vendieron por ciudad?

| Zona | Campo |
|------|-------|
| Filas | Ciudad |
| Valores | Recuento de Producto (no suma — cuenta filas) |

---

**Pregunta D:** ¿Cual es el ticket medio por region y mes?

| Zona | Campo |
|------|-------|
| Filas | Region |
| Columnas | Fecha (agrupada por Mes) |
| Valores | Media de Total |

---

## Actividad 3: Interpretar los resultados de Montgomery

Basandose en las capturas del final assignment, responder:

**¿Que departamento tiene mas vehiculos y cuantos?**

Transportation — con 379 unidades (visible en la Pivot 1 como la primera
fila al ordenar de mayor a menor, y como el MAX de la columna C).

**¿Para que sirve la Pivot 2 (Department > Equipment Class)?**

Para ver no solo el total por departamento, sino como se distribuye
ese total entre los distintos tipos de equipo. Por ejemplo: Transportation
tiene 379 unidades en total, pero la Pivot 2 permite ver cuantas son
coches, camiones, maquinaria, etc.

**¿Por que es util hacer la Pivot 3 (Equipment Class > Department)?**

La logica es inversa: en vez de "que tipos de equipo tiene cada departamento",
responde "en que departamentos se usa cada tipo de equipo". Util si la
pregunta es "quienes tienen CUV" en vez de "que tiene Transportation".

**¿Que insight da el AutoSum de la columna C?**

- COUNT=49: hay 49 departamentos/categorias de equipo distintas
- SUM=1582: el inventario total es de 1582 unidades
- MAX=379: el departamento mayor tiene 379 unidades
- MIN=1: el mas pequeno tiene 1 sola unidad
- AVG=32.29: de media, cada departamento tiene 32 unidades — pero
  la diferencia entre 1 y 379 indica una distribucion muy desigual
