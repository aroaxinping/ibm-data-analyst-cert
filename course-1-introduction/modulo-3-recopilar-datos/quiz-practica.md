# Quiz de Practica — Modulo 3: Gathering and Wrangling Data

---

**1. Un dataset de ventas tiene la columna "fecha_pedido" con valores en
tres formatos distintos: "15/03/2024", "2024-03-15" y "15 marzo 2024".
¿Que dimension de calidad de datos esta fallando?**

<details>
<summary>Respuesta</summary>

**Consistencia.** Los datos representan lo mismo pero con formatos
diferentes, lo que los hace incoherentes entre si y dificiles de
ordenar o filtrar correctamente.

La solucion es estandarizar todos a un unico formato antes de analizar.

</details>

---

**2. Un dataset de clientes tiene la columna "ingresos_anuales" vacia
para el 65% de los registros. ¿Que dimension de calidad falla y que
opciones hay para tratarlo?**

<details>
<summary>Respuesta</summary>

**Completitud.** Falta una cantidad significativa de valores.

Opciones:
- Si el 65% de nulos hace la columna poco fiable, descartarla del analisis
- Rellenar con la mediana de los ingresos (no la media — suele haber sesgo)
- Crear una categoria "No informado" si la ausencia tiene significado propio
- Buscar la informacion en otra fuente y completarla

Con un 65% de nulos, rellenar con la mediana es arriesgado porque estariamos
inventando el 65% de los datos. Lo mas honesto es documentar esta limitacion.

</details>

---

**3. Al analizar un dataset de empleados, se encuentra un registro con
edad = 187. ¿Como se trataria este dato?**

<details>
<summary>Respuesta</summary>

Es un **outlier** que casi con certeza es un error de entrada (un campo
numerico que alguien rellenó mal).

Pasos correctos:
1. No eliminar directamente sin investigar
2. Buscar si hay forma de verificar el dato real (otra fuente, el registro original)
3. Si no es recuperable, tratarlo como nulo (NA) y aplicar la estrategia de nulos
4. Documentar que ese registro tenia un valor imposible

Nunca simplemente reemplazarlo por la media sin documentar — eso distorsiona
el dataset de forma silenciosa.

</details>

---

**4. ¿Por que es importante evaluar la calidad de los datos ANTES de
empezar el analisis, y no despues?**

<details>
<summary>Respuesta</summary>

Porque si los datos tienen problemas de calidad, las conclusiones del
analisis seran incorrectas aunque el proceso analitico sea tecnicamente
perfecto. "Basura dentro, basura fuera" (garbage in, garbage out).

Ademas, detectar problemas de calidad al final obliga a rehacer todo
el analisis. Detectarlos al principio ahorra ese retrabajo.

</details>

---

**5. Un analista tiene un dataset de precios de pisos con algunos valores
muy altos (penthouse en el centro de Madrid a 10 millones de euros).
¿Deberia eliminarlos como outliers?**

<details>
<summary>Respuesta</summary>

**No necesariamente.** Los outliers no son siempre errores. Un piso de
10 millones puede ser perfectamente real.

Antes de eliminarlos hay que preguntarse:
- ¿La pregunta de negocio incluye este tipo de propiedades?
  Si se analiza el mercado de vivienda habitual, puede tener sentido
  excluirlos y documentarlo.
- ¿Son errores o casos reales? Verificar contra otra fuente.

Si se excluyen, hay que documentarlo explicitamente: "el analisis excluye
propiedades con precio superior a X por considerarse fuera del segmento objetivo".

</details>

---

**6. ¿Cual es la diferencia entre eliminar un nulo e imputarlo?**

<details>
<summary>Respuesta</summary>

- **Eliminar:** se borra la fila o columna con el nulo. Se pierde informacion
  del resto del registro. Recomendable cuando el nulo esta en una columna
  critica y hay pocos nulos.

- **Imputar:** se reemplaza el nulo con un valor estimado (media, mediana,
  moda, o un modelo mas sofisticado). Se mantiene el registro pero se
  introduce un valor artificial. Hay que documentarlo.

Ninguna opcion es siempre la correcta — depende del porcentaje de nulos,
de la importancia de la columna y del uso que se hara del dato.

</details>

---

**7. ¿En que se diferencia Power Query de pandas para el wrangling?**

<details>
<summary>Respuesta</summary>

- **Power Query** (Excel): interfaz grafica, sin codigo, mas accesible.
  Bueno para transformaciones estandar en datasets pequenos o medianos.
  No es reproducible de forma automatica ni escalable facilmente.

- **pandas** (Python): basado en codigo, mas flexible y potente.
  Permite transformaciones complejas, es reproducible (el codigo queda
  documentado), automatizable y funciona con datasets grandes.

Para un analista, saber ambos es util: Power Query para trabajo rapido
en Excel, pandas para analisis mas serios o que se van a repetir.

</details>
