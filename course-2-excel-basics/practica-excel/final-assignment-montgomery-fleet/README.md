# Final Assignment — Montgomery Fleet Equipment Inventory

Entrega final del Course 2 (Excel Basics for Data Analysis).

## Archivos

- `Montgomery_Fleet_Equipment_Inventory_FA_PART_1_START.csv` — origen
- `Montgomery_Fleet_Equipment_Inventory_FA_PART_1_END.xlsx` — limpieza
- `Montgomery_Fleet_Equipment_Inventory_FA_PART_2_START.xlsx` — origen
- `Montgomery_Fleet_Equipment_Inventory_FA_PART_2_END.xlsx` — tabla + pivots

## Capturas

### Part 1 — antes y despues

**Antes** (CSV crudo con filas vacias, typos, departments partidos en 2 columnas, duplicados):

![Part 1 before](./screenshots/part1_before.png)

**Despues** (limpio, deduplicado, columna Department unificada):

![Part 1 after](./screenshots/part1_after.png)

### Part 2 — antes y despues

**Antes** (datos planos, sin tabla ni pivots):

![Part 2 before](./screenshots/part2_before.png)

**Despues** (formateado como tabla + AutoSum):

![Part 2 after](./screenshots/part2_after_table.png)

**Pivot Table 1** — suma por Department (desc):

![Pivot Table 1](./screenshots/pivot1.png)

**Pivot Table 2** — Department > Equipment Class (Transportation expandido):

![Pivot Table 2](./screenshots/pivot2.png)

**Pivot Table 3** — Equipment Class > Department (CUV expandido):

![Pivot Table 3](./screenshots/pivot3.png)

## Part 1 — Data cleaning

- CSV convertido a XLSX, anchos de columna ajustados.
- Filas vacias eliminadas, duplicados eliminados (53 filas unicas).
- Spelling: `Rehabilltation`, `Recsue`, `Servcies`, `Enviromnental`,
  `VehicleEquipment` corregidos.
- Dobles espacios eliminados (find & replace).
- Columnas Department unificadas en una sola (flash fill).

## Part 2 — Pivot tables

- Datos formateados como tabla (`FleetTable`).
- AutoSum columna C:
  - SUM = 1582
  - AVERAGE ≈ 32.29
  - MIN = 1
  - MAX = 379
  - COUNT = 49
- `Pivot Table 1`: Department → suma de Equipment Count, orden descendente.
- `Pivot Table 2`: Department > Equipment Class, colapsado excepto Transportation.
- `Pivot Table 3`: Equipment Class > Department, colapsado excepto CUV.
