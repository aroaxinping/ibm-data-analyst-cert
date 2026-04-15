# Actividades — Modulo 2: Data Quality and Data Wrangling in Spreadsheets

---

## Actividad 1: Proyecto Montgomery — lo que se hizo en cada paso

Documentar el proceso real del final assignment con las tecnicas del modulo.

### Part 1: Data Cleaning

**Dataset de entrada:** CSV con el inventario de vehiculos del condado de Montgomery.

**Problemas identificados y solucion aplicada:**

| Problema | Donde | Tecnica usada |
|----------|-------|---------------|
| Filas vacias intercaladas | Todo el dataset | Seleccionar y eliminar manualmente |
| Filas duplicadas | Varias filas identicas | Datos > Quitar duplicados |
| Typo: `Rehabilltation` | Columna Department | Ctrl+H: reemplazar por `Rehabilitation` |
| Typo: `Recsue` | Columna Department | Ctrl+H: reemplazar por `Rescue` |
| Typo: `Servcies` | Columna Department | Ctrl+H: reemplazar por `Services` |
| Typo: `Enviromnental` | Columna Department | Ctrl+H: reemplazar por `Environmental` |
| Typo: `VehicleEquipment` | Columna Department | Ctrl+H: reemplazar por `Vehicle Equipment` |
| Dobles espacios en nombres | Columna Department | Ctrl+H: reemplazar `"  "` por `" "` |
| Columna Department partida en 2 | Columnas C y D | Flash Fill para unificar en una sola |

**Resultado:** 53 filas unicas, una sola columna Department, spelling corregido.

---

## Actividad 2: Identificar problemas en un dataset hipotetico

Dataset de empleados con problemas de calidad. Identificar cada problema
y la funcion o tecnica correcta para tratarlo.

| Columna | Valor de ejemplo | Problema | Solucion |
|---------|-----------------|----------|----------|
| nombre | "  ana garcia " | Espacios extra | `=ESPACIOS(A1)` |
| departamento | "it" / "IT" / "It" | Inconsistencia mayusculas | `=MAYUSC()` o `=NOMPROPIO()` para estandarizar |
| salario | "35.000€" | Numero almacenado como texto con simbolo | `=VALOR(SUSTITUIR(SUSTITUIR(A1,"€",""),".",""))` |
| fecha_alta | "1 enero 2023" | Fecha como texto | Datos > Texto en columnas > formato Fecha |
| email | (vacio) | Nulo en campo importante | Identificar con `=ESBLANCO()`, tratar segun politica |
| id_empleado | 1042, 1042 | Duplicado | Datos > Quitar duplicados |

---

## Actividad 3: Escribir las formulas de limpieza

Para cada transformacion, escribir la formula correcta:

| Transformacion | Formula |
|----------------|---------|
| Eliminar espacios de A1 | `=ESPACIOS(A1)` |
| Poner A1 en minusculas | `=MINUSC(A1)` |
| Extraer los primeros 3 caracteres de A1 | `=IZQUIERDA(A1, 3)` |
| Reemplazar "bcn" por "Barcelona" en A1 | `=SUSTITUIR(A1, "bcn", "Barcelona")` |
| Contar cuantas celdas de A:A estan vacias | `=CONTAR.BLANCO(A:A)` |
| Marcar si A1 tiene el mismo valor que alguna celda anterior (duplicado) | `=CONTAR.SI($A$1:A1,A1)>1` |
| Convertir el texto "42.5" de A1 a numero | `=VALOR(A1)` |
| Unir el nombre de A1 y apellido de B1 con espacio | `=CONCATENAR(A1," ",B1)` o `=A1&" "&B1` |

---

## Actividad 4: Reflexion sobre el proyecto Montgomery

Responder basandose en la experiencia real del final assignment.

**¿Cual fue el paso de limpieza mas tedioso y por que?**

Los typos en la columna Department — habia que encontrarlos primero
(inspeccion visual o filtro) y luego corregirlos uno a uno con Ctrl+H.
El dataset era pequeno (53 filas) pero en un dataset real de miles de
filas sin Flash Fill o formulas, seria inviable.

**¿Que pasaria si no se eliminaran los duplicados antes de crear la pivot table?**

La pivot table contaria el doble (o mas) esas filas duplicadas, inflando
los totales y produciendo conclusiones erroneas. Por ejemplo, si un
departamento tenia 5 vehiculos pero el registro aparecia duplicado,
la pivot mostraria 10.

**¿Por que es importante el orden: primero limpiar, despues analizar?**

Porque cualquier analisis sobre datos sucios produce resultados incorrectos.
En el caso de Montgomery: si no se corrige `Rehabilltation` antes de la
pivot, apareceria como un departamento separado de `Rehabilitation` con
sus propios totales, fragmentando incorrectamente los datos.
