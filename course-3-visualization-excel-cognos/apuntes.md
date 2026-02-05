# Apuntes — Course 3: Data Visualization and Dashboards with Excel and Cognos

**Duracion:** 13 horas
**Modulos:** 4

---

## Que cubre este curso

Crear visualizaciones que comuniquen hallazgos de forma clara. El curso cubre
los principios de visualizacion, los tipos de grafico y sus casos de uso,
y el diseño de dashboards en Excel y IBM Cognos Analytics.

---

## Modulo 1: Visualizing Data with Spreadsheets

**Por que importa la visualizacion:**
Los numeros en una tabla no comunican patrones de forma intuitiva. Una
visualizacion bien diseñada permite:
- Detectar tendencias y patrones rapidamente
- Comparar valores de forma eficiente
- Comunicar hallazgos a audiencias no tecnicas

**Tipos de grafico y cuando usarlos:**

| Grafico | Mejor para | Evitar cuando |
|---------|-----------|---------------|
| Barras (vertical / horizontal) | Comparar categorias | Hay mas de 10-12 categorias |
| Lineas | Evolucion temporal | Los datos no son continuos |
| Circular / dona | Proporciones de un total | Hay mas de 5-6 categorias |
| Dispersion (scatter) | Relacion entre dos variables numericas | Los datos tienen pocas observaciones |
| Histograma | Distribucion de una variable | Se quiere comparar categorias |
| Boxplot | Distribucion + outliers | Audiencia no tecnica |
| Mapas de calor | Matrices de correlacion, calendarios | — |
| Treemap | Proporciones jerarquicas | Datos sin jerarquia clara |

**Graficos de Excel mas usados en analisis:**

- **Barras agrupadas:** comparar varias series entre categorias
- **Barras apiladas:** mostrar composicion + total
- **Lineas:** series temporales
- **Combinado (barra + linea):** dos metricas con escalas diferentes en un grafico

**Configuracion de un grafico profesional en Excel:**
1. Titulo claro que describe el hallazgo (no solo el contenido)
2. Etiquetas de ejes con unidades
3. Eliminar gridlines innecesarias
4. Paleta de colores coherente y accesible
5. Leyenda solo si hay varias series
6. Sin efectos 3D (distorsionan la percepcion)

---

## Modulo 2: Creating Visualizations and Dashboards with Spreadsheets

**Spark lines:**
Minigraficos dentro de una celda. Ideales para mostrar tendencias rapidamente
en un informe tabular sin necesidad de un grafico completo. Insertar > Spark
lines > Linea / Columna / Perdidas y ganancias.

**Formato condicional como visualizacion:**
- Escalas de color: verde-amarillo-rojo para valores alto-medio-bajo
- Barras de datos: barra proporcional dentro de la celda
- Conjuntos de iconos: flechas, semaforos, estrellas

Util para tablas que ya tienen muchos datos y no se quiere añadir un grafico
adicional.

**Diseño de dashboards en Excel:**

Principios:
- **Una pantalla:** el dashboard debe caber en una pantalla sin scroll
- **Jerarquia visual:** lo mas importante, arriba a la izquierda y mas grande
- **Consistencia:** misma paleta, mismas fuentes, mismo estilo de grafico
- **Interactividad basica:** slicers para que el usuario filtre sin tocar datos
- **KPIs destacados:** los 3-5 numeros clave en grande, arriba del todo

Estructura tipica de un dashboard:
```
[KPI 1]   [KPI 2]   [KPI 3]
[Grafico principal (tendencia temporal)]
[Grafico secundario A] [Grafico secundario B]
[Tabla de detalle]
```

**Sheets de soporte:**
El dashboard solo tiene graficos. Los datos y calculos van en hojas ocultas
separadas. El usuario del dashboard no toca los datos crudos.

---

## Modulo 3: Creating Visualizations with Cognos Analytics

IBM Cognos Analytics es una plataforma de BI empresarial. La capa gratuita
permite explorar sus funcionalidades principales.

**Conceptos clave de Cognos:**

- **Fuente de datos:** conexion a un dataset (archivo, base de datos, API)
- **Modulo de datos:** vista limpia y preparada de los datos para reportes
- **Reporte:** documento estructurado con visualizaciones y tablas
- **Dashboard:** vista interactiva con filtros y graficos conectados
- **Story:** narrativa guiada con slides de datos

**Diferencia con Excel:**

| Aspecto | Excel | Cognos |
|---------|-------|--------|
| Volumen de datos | Limitado (millones de filas) | Grande (bases de datos enteras) |
| Colaboracion | Compartir archivo | Web, multiusuario en tiempo real |
| Actualizacion | Manual | Automatica con la fuente |
| Curva de aprendizaje | Baja | Media-alta |
| Permisos | Basicos | Granulares por rol |

**Tipos de widget en Cognos Dashboard:**
- KPI card
- Grafico de barras / lineas / circular
- Tabla de referencias cruzadas (crosstab)
- Mapa
- Filtros de panel

**Flujo tipico en Cognos:**
1. Conectar fuente de datos (CSV, DB2, etc.)
2. Crear modulo de datos (limpiar, renombrar, crear calculos)
3. Crear dashboard o reporte
4. Añadir widgets y configurar visualizaciones
5. Publicar y compartir

---

## Modulo 4: Final Assignment — Creating Dashboards

El proyecto final del curso consiste en crear un dashboard con datos reales
usando tanto Excel como Cognos.

**Dataset:** datos de automoviles del mercado americano (fuel economy, etc.)

**Requisitos del dashboard:**

En Excel:
- Grafico de barras: promedio de CO2 por fabricante
- Grafico de lineas: evolucion del consumo por año
- Tabla dinamica con slicer por tipo de combustible

En Cognos:
- KPI: promedio de MPG de la seleccion actual
- Grafico de dispersion: potencia vs consumo
- Mapa: distribucion geografica de ventas (si aplica)
- Filtro por año y fabricante

**Notas del proceso:**
_(completar al hacer el proyecto)_

---

## Principios de visualizacion de datos

**Los cinco principios de Edward Tufte adaptados:**

1. **Integridad grafica:** el tamaño visual debe ser proporcional al dato.
   No truncar ejes para exagerar diferencias.
2. **Maxima densidad de informacion:** cada pixel debe aportar. Eliminar
   elementos decorativos que no añaden informacion (chart junk).
3. **Contexto:** los datos solos no significan nada. Siempre comparar
   con un benchmark: año anterior, objetivo, media del sector.
4. **Claridad del mensaje:** el grafico debe comunicar un hallazgo concreto,
   no mostrar datos "por si alguien los necesita".
5. **Accesibilidad:** paletas accesibles para daltonismo. Nunca usar rojo/verde
   como unica distincion.

**Colores:**
- Usar una paleta de 2-3 colores maximo
- El color mas llamativo para el dato mas importante
- Escala secuencial (claro a oscuro) para magnitudes
- Escala divergente (rojo-blanco-azul) para desviaciones respecto a un punto medio
- Gris para elementos de contexto que no son el foco

---

## Esquema resumido del curso

```
COURSE 3: VISUALIZATION
|
+-- Tipos de grafico y casos de uso
|     Barras, lineas, circular, scatter, histograma, treemap
|
+-- Excel avanzado para visualizacion
|     Spark lines, formato condicional, dashboards con slicers
|
+-- IBM Cognos Analytics
|     Fuentes de datos, modulos, dashboards interactivos
|
+-- Principios de diseño
      Integridad grafica, densidad, contexto, claridad, accesibilidad
```

---

## Glosario

| Termino | Definicion |
|---------|------------|
| Dashboard | Vista consolidada de metricas clave en una sola pantalla |
| KPI | Key Performance Indicator — metrica que mide el rendimiento respecto a un objetivo |
| Spark line | Minigrafico dentro de una celda de hoja de calculo |
| Formato condicional | Formato visual aplicado automaticamente segun el valor de la celda |
| Chart junk | Elementos visuales decorativos que no añaden informacion al grafico |
| Escala divergente | Paleta de colores con un punto neutral en el centro y colores opuestos en los extremos |
| Cognos | Plataforma de BI de IBM para crear reportes y dashboards empresariales |
| Crosstab | Tabla de referencias cruzadas que muestra valores por dos dimensiones |

---

## Errores comunes

- **Graficos circulares con demasiadas categorias:** con mas de 5-6 sectores
  es imposible comparar. Usar barras horizontales en su lugar.
- **Ejes truncados para dramatizar:** empezar el eje Y en un valor diferente
  de cero exagera las diferencias visualmente. Solo justificado en casos
  muy concretos con buena documentacion.
- **Colores sin significado:** usar paletas de arcoiris por estetica. Los
  colores deben comunicar algo (mayor = mas oscuro, alerta = rojo).
- **Dashboard con demasiados elementos:** añadir todos los graficos posibles.
  Un buen dashboard tiene 5-7 elementos maximos, cada uno con un proposito claro.

---

## Conexion con otros cursos

- Los tipos de grafico vistos aqui se implementan en Python con matplotlib,
  seaborn y plotly en el curso 8. El criterio de eleccion del grafico es
  el mismo, cambia la herramienta.
- Los principios de dashboard (KPIs arriba, jerarquia visual, slicers)
  aplican igual en Cognos, Tableau, Power BI o cualquier herramienta de BI.
- Los datos de automoville del proyecto final son un buen ejemplo de dataset
  que volvera a aparecer en el curso 7 (Data Analysis with Python).
