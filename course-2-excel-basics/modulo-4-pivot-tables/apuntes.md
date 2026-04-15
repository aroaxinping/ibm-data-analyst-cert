# Modulo 4: Pivot Tables

**Semana:** 3
**Duracion estimada:** 3 horas

---

## De que va este modulo

Las tablas dinamicas son la herramienta mas potente de Excel para el
analisis exploratorio rapido. Permiten resumir, agrupar y cruzar datos
de miles de filas en segundos, sin escribir una sola formula. Este modulo
es el que mas se usa en el trabajo real de un analista que trabaja con Excel.

---

## 1. Que es una tabla dinamica y para que sirve

Una tabla dinamica reorganiza y resume un dataset segun las dimensiones
y metricas que eliges. Es el equivalente de un GROUP BY de SQL hecho
con interfaz grafica.

**Cuándo usar una pivot table:**
- Resumir ventas por region, producto, mes, categoria...
- Contar registros por categoria
- Calcular medias, maximos o porcentajes por grupos
- Comparar dos dimensiones a la vez (filas x columnas)
- Explorar un dataset que no se conoce bien

**Lo que NO hace:** modificar los datos originales. La pivot es una vista
del dataset, no una copia. Si los datos originales cambian, hay que
actualizar la pivot (clic derecho > Actualizar).

---

## 2. Crear una tabla dinamica

**Pasos:**

1. Seleccionar cualquier celda dentro del dataset (Excel detecta el rango)
2. Insertar > Tabla dinamica
3. Confirmar el rango de datos
4. Elegir donde colocarla: nueva hoja (recomendado) o hoja existente
5. Se abre el panel de campos a la derecha

**Requisitos del dataset:**
- Cada columna debe tener un encabezado
- Sin filas o columnas completamente vacias dentro del rango
- Una fila = un registro (formato largo, no formato ancho)

**Recomendacion:** antes de crear la pivot, convertir el rango en tabla
(Ctrl+T). Las tablas se expanden automaticamente cuando se añaden filas
y la pivot las recoge al actualizar.

---

## 3. Las cuatro zonas del panel de campos

| Zona | Que hace | Ejemplo |
|------|----------|---------|
| **Filas** | Agrupa los datos por esta dimension — aparece como filas | Region, Producto, Mes |
| **Columnas** | Segunda dimension de agrupacion — aparece como columnas | Año, Tipo |
| **Valores** | La metrica que se calcula para cada combinacion | Suma de Ventas, Conteo |
| **Filtros** | Filtra todo el informe — aparece como desplegable arriba | Pais, Categoria |

**Arrastrar y soltar:** los campos se arrastran desde la lista de arriba
a las zonas de abajo. Se pueden mover, reorganizar y eliminar en cualquier momento.

---

## 4. Calculos en la zona Valores

Al poner un campo en Valores, por defecto:
- Si el campo es numerico: calcula la **suma**
- Si el campo es texto: calcula el **recuento**

Para cambiar el calculo: clic en el campo en la zona Valores >
Configuracion de campo de valor.

**Calculos disponibles:**
- Suma
- Recuento (COUNT — cuenta filas, incluye texto)
- Recuento de numeros (COUNT A — solo numeros)
- Media
- Maximo / Minimo
- Producto
- Desviacion tipica (muestral / poblacional)
- Varianza

**Mostrar valores como:**
Ademas del calculo en si, se puede cambiar como se muestra el valor.
Clic derecho sobre un valor > Mostrar valores como:

- % del total general
- % del total de fila
- % del total de columna
- Diferencia respecto a un valor base
- Diferencia % respecto a un valor base
- Total acumulado
- % del total acumulado
- Clasificacion de menor a mayor

Muy util para mostrar porcentajes sin escribir formulas adicionales.

---

## 5. Ordenar y filtrar dentro de la pivot

**Ordenar:** hacer clic en cualquier celda de valores y usar los botones
de orden ascendente/descendente de la cinta, o clic derecho > Ordenar.

**Filtrar por etiqueta:** el desplegable de fila o columna permite
seleccionar que valores mostrar. Util para centrarse en un subconjunto.

**Filtrar por valor:** mostrar solo las filas donde el valor supera
un umbral. Clic en desplegable > Filtros de valor.

**Top 10:** Filtros de valor > Los 10 primeros. Permite ver rapidamente
los N mayores o menores valores sin filtrar manualmente.

---

## 6. Agrupar datos

La pivot puede agrupar automaticamente fechas por mes, trimestre o año,
y numeros en rangos.

**Agrupar fechas:**
Clic derecho sobre una fecha en la pivot > Agrupar > seleccionar
Meses, Trimestres, Anos...

**Agrupar numeros:**
Clic derecho > Agrupar > definir inicio, fin e intervalo.
Util para crear rangos de precio, rangos de edad, etc.

---

## 7. Tablas dinamicas jerarquicas

Se pueden poner varios campos en la zona Filas para crear una jerarquia:

```
Filas: Region > Ciudad > Tienda
```

Excel muestra primero las regiones, y se pueden expandir para ver las
ciudades, y dentro de cada ciudad las tiendas. Hacer clic en el icono
+ para expandir y - para colapsar.

Esto es exactamente lo que se hace en el proyecto de Montgomery:
- Pivot 2: Department > Equipment Class (Transportation expandido)
- Pivot 3: Equipment Class > Department (CUV expandido)

---

## 8. Segmentaciones de datos (Slicers)

Los slicers son botones visuales que filtran la tabla dinamica.
Son la alternativa visual a los filtros de la zona Filtros.

**Insertar un slicer:**
Clic dentro de la pivot > Analizar tabla dinamica > Insertar segmentacion de datos.

**Conectar un slicer a varias pivots:**
Si hay varias tablas dinamicas en el mismo libro, un slicer puede
controlarlas todas a la vez. Clic derecho en el slicer > Conexiones de informe.

**Por que usar slicers:**
- Mas intuitivos para usuarios no tecnicos
- Se puede ver rapidamente que filtro esta activo (los botones seleccionados
  se resaltan)
- Permiten hacer clic rapido para cambiar entre valores

---

## 9. Graficos dinamicos

Un grafico dinamico esta vinculado a una tabla dinamica y se actualiza
automaticamente cuando cambia el filtro o la configuracion de la pivot.

**Crear:** con la pivot seleccionada > Analizar > Grafico dinamico.
O insertar un grafico normal — si los datos origen son una pivot,
sera dinamico automaticamente.

**Lo que cambia respecto a un grafico normal:**
Tiene botones de filtro integrados en el propio grafico que permiten
filtrar sin tocar la pivot. Se pueden ocultar si el grafico es para
una presentacion.

---

## Lo que se aplica en el proyecto final (Montgomery Part 2)

**Formatear como tabla:**
Antes de la pivot se formatea el rango como tabla (`FleetTable`)
con Ctrl+T para que la pivot se actualice automaticamente si se
añaden datos.

**AutoSum en columna C:**
Seleccionar las celdas debajo del rango de Equipment Count y aplicar
AutoSum para obtener rapidamente SUM, AVG, MIN, MAX y COUNT.
Resultado real: SUM=1582, AVG=32.29, MIN=1, MAX=379, COUNT=49.

**Pivot 1:** Department en Filas, Equipment Count en Valores (Suma),
ordenada de forma descendente.

**Pivot 2:** Department en Filas, Equipment Class en Filas (subnivel),
Equipment Count en Valores. Expandir Transportation para ver el detalle.

**Pivot 3:** Equipment Class en Filas, Department en Filas (subnivel),
Equipment Count en Valores. Expandir CUV para ver el detalle.

---

## Glosario del modulo

| Termino | Definicion |
|---------|------------|
| Tabla dinamica | Herramienta de resumen interactivo que agrupa y calcula datos sin formulas |
| Campo | Cada columna del dataset original — se puede usar en cualquier zona de la pivot |
| Filas | Zona de la pivot donde se colocan las dimensiones de agrupacion en vertical |
| Columnas | Zona de la pivot donde se colocan las dimensiones de agrupacion en horizontal |
| Valores | Zona donde se define la metrica a calcular (suma, media, conteo...) |
| Slicer | Botones visuales para filtrar la tabla dinamica de forma interactiva |
| Grafico dinamico | Grafico vinculado a una tabla dinamica que se actualiza automaticamente |
| Drill-down | Expandir un nivel de la jerarquia para ver el detalle |
| Actualizar | Refrescar la pivot para que recoja cambios en los datos originales |

---

## Lo mas importante de este modulo

Las tablas dinamicas reemplazan horas de trabajo manual con minutos.
Cualquier analisis que se pueda expresar como "suma / conteo / media de X
agrupado por Y" se puede hacer con una pivot en segundos.

El error mas comun: olvidar actualizar la pivot despues de cambiar los
datos. La pivot no se actualiza sola — siempre hay que hacer clic derecho
> Actualizar, o configurar la actualizacion automatica al abrir el archivo.
