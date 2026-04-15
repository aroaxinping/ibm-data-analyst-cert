# Quiz de Practica — Modulo 4: Pivot Tables

---

**1. Se tiene un dataset de ventas con columnas: fecha, region, vendedor,
producto, cantidad, precio. Se quiere ver la suma de precio por region
y por producto (regiones en filas, productos en columnas).
¿Como se configura la pivot?**

<details>
<summary>Respuesta</summary>

- **Filas:** Region
- **Columnas:** Producto
- **Valores:** Suma de Precio

Resultado: una tabla donde cada fila es una region, cada columna es un
producto, y el valor de cada celda es la suma de precios para esa
combinacion region-producto.

</details>

---

**2. La pivot muestra "Recuento de Precio" en vez de "Suma de Precio".
¿Por que ocurre esto y como se cambia?**

<details>
<summary>Respuesta</summary>

Ocurre porque Excel detecta que la columna Precio tiene algun valor
de texto (un nulo, un "#N/A" o texto), y cuando hay texto en un campo
numerico, Excel usa Recuento por defecto en vez de Suma.

Para cambiarlo: clic en el campo en la zona Valores > Configuracion de
campo de valor > seleccionar Suma.

La causa raiz hay que corregirla en el dataset original: localizar
y eliminar los valores de texto en la columna de precio.

</details>

---

**3. Se quiere que la pivot muestre el porcentaje que representa cada
region sobre el total de ventas, en vez de el valor absoluto. ¿Como?**

<details>
<summary>Respuesta</summary>

Clic derecho sobre los valores de la pivot > Mostrar valores como >
% del total general.

O en la configuracion del campo de valor: zona Valores > campo > Mostrar
valores como > % del total general.

</details>

---

**4. La pivot tiene un slicer de "Año" con los valores 2022, 2023, 2024.
Se selecciona 2023. ¿Que ocurre con el grafico dinamico vinculado?**

<details>
<summary>Respuesta</summary>

El grafico dinamico se actualiza automaticamente mostrando solo los
datos de 2023. El slicer controla tanto la tabla dinamica como el grafico
vinculado a ella al mismo tiempo.

</details>

---

**5. Se añaden 200 filas nuevas al dataset original. ¿La pivot se
actualiza automaticamente?**

<details>
<summary>Respuesta</summary>

**No.** La pivot hay que actualizarla manualmente: clic derecho dentro
de la pivot > Actualizar. O en la cinta: Analizar tabla dinamica > Actualizar.

Si el dataset esta formateado como tabla (Ctrl+T), el rango se expande
automaticamente al añadir filas, pero la pivot sigue necesitando la
actualizacion manual para incorporar los nuevos datos.

Para actualizacion automatica: Analizar > Opciones > Datos > marcar
"Actualizar al abrir el archivo". Pero esto solo actualiza al abrir,
no en tiempo real.

</details>

---

**6. ¿En que se diferencia usar el campo "Region" en la zona Filtros
vs usarlo en la zona Filas?**

<details>
<summary>Respuesta</summary>

- **En Filas:** la pivot muestra una fila por cada region, con sus
  metricas correspondientes. Se pueden ver todas las regiones a la vez
  y compararlas directamente.

- **En Filtros:** la pivot muestra los datos de UNA region a la vez
  (la seleccionada en el desplegable). Es un filtro global que oculta
  el resto — util cuando solo se quiere analizar una region en particular.

</details>

---

**7. Verdadero o falso: una tabla dinamica modifica el dataset original.**

<details>
<summary>Respuesta</summary>

**Falso.** La tabla dinamica es una vista del dataset, no una copia
ni una modificacion. El dataset original queda intacto. Todos los calculos
de la pivot son temporales y se recalculan al actualizar.

Esto es una de las grandes ventajas: se puede experimentar con distintas
configuraciones sin riesgo de estropear los datos.

</details>
