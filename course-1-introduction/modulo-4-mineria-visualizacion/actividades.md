# Actividades — Modulo 4: Mining & Visualizing Data and Communicating Results

---

## Actividad 1: Elegir el grafico correcto

Para cada situacion, elegir el tipo de grafico mas adecuado y justificar.

| Situacion | Grafico elegido | Justificacion |
|-----------|----------------|---------------|
| Mostrar la evolucion del numero de usuarios activos mes a mes durante 2 anos | Lineas | Serie temporal continua — las lineas muestran la tendencia |
| Comparar el numero de ventas de 8 productos distintos en un mes | Barras horizontales | Comparacion entre categorias; horizontal porque los nombres de producto son largos |
| Ver si existe relacion entre el presupuesto de marketing y las ventas | Scatter (dispersion) | Relacion entre dos variables numericas |
| Mostrar que porcentaje del presupuesto total va a cada departamento (5 departamentos) | Barras horizontales o circular | Circular si hay pocas categorias y se quiere mostrar la proporcion; barras si se quiere comparar valores exactos |
| Ver la distribucion de edades de los clientes | Histograma | Distribucion de una variable numerica continua |
| Comparar el rango de salarios entre departamentos, con outliers | Boxplot | Muestra mediana, cuartiles y outliers de forma compacta |
| Mostrar la intensidad de la correlacion entre 10 variables | Heatmap | Matriz de correlacion — el color indica la fuerza y direccion |

---

## Actividad 2: Detectar problemas en visualizaciones

Para cada descripcion de grafico, identificar el problema y proponer la correccion.

**Caso A:** Grafico de barras comparando las ventas de dos productos.
El producto A tiene 1.020 unidades y el B tiene 1.000. El eje Y empieza en 990.
Las barras hacen que parezca que A vende el doble que B.

*Problema:* Eje Y truncado — distorsiona la percepcion de la diferencia.
*Correccion:* Empezar el eje Y en 0. La diferencia real (2%) se veria
como lo que es: pequena.

---

**Caso B:** Grafico circular con 12 categorias de producto, todas con
colores distintos. Es casi imposible distinguir unas de otras.

*Problema:* Demasiadas categorias para un circular — imposible de leer.
*Correccion:* Usar barras horizontales, que permiten leer los valores
exactos y comparar categorias facilmente. O agrupar las categorias menores
en "Otros".

---

**Caso C:** Titulo del grafico: "Distribucion de clientes por segmento
de edad Q3 2024".

*Problema:* Describe el contenido pero no comunica ningun hallazgo.
*Correccion posible:* "El segmento 25-34 anos representa el 42% de los
clientes, el doble que cualquier otro grupo de edad" — esto si dice algo.

---

**Caso D:** Un grafico de lineas con 15 series distintas, todas en colores
diferentes. La leyenda ocupa mas espacio que el grafico.

*Problema:* Demasiadas series — el grafico no comunica nada claro.
*Correccion:* Destacar las 2-3 series relevantes para el mensaje y poner
el resto en gris como contexto. O dividir en varios graficos mas pequenos.

---

## Actividad 3: Adaptar el mensaje al publico

El mismo hallazgo, tres audiencias distintas. Reescribir para cada una.

**Hallazgo:** el modelo de clustering identifico 4 segmentos de clientes.
El segmento 3 (clientes con alto ticket medio y baja frecuencia de compra)
tiene una tasa de churn del 34%, significativamente mayor que la media del 12%.
Se identifico que este segmento no tiene activado el programa de fidelizacion.

---

**Para el CEO:**

Las ventas de los clientes de alto valor estan en riesgo: el 34% abandona
cada ano, frente al 12% de media. La causa identificada: no estan en el
programa de fidelizacion. Recomendacion: inscribirlos proactivamente en el
programa. Impacto estimado: reducir el churn de este segmento al 15% supondria
retener X euros en ingresos anuales.

---

**Para el responsable de marketing:**

El segmento de clientes con ticket alto y compra poco frecuente tiene
un churn del 34% (media: 12%). Analisis de la causa: el 89% de este segmento
no tiene activado el programa de puntos. Propuesta: campana de activacion
del programa de fidelizacion especificamente para este segmento, con
comunicacion personalizada.

---

**Para el equipo de datos:**

El modelo K-Means con k=4 identifico 4 clusters. El cluster 3 (n=1.240,
ticket medio 180€, frecuencia media 1.2 compras/mes) presenta churn_rate=0.34
vs media global de 0.12. Feature importance: la variable loyalty_program_active
aparece como el predictor mas relevante del churn en este segmento (SHAP
value promedio 0.28). Proximos pasos: validar con el equipo de negocio,
definir la metrica de exito de la intervencion y disenar el A/B test.

---

## Actividad 4: EDA basico a mano

**Dataset:** 7 empleados con sus salarios anuales (en miles de euros).
Valores: 28, 32, 35, 38, 40, 45, 180

Calcular:
- Media: (28+32+35+38+40+45+180) / 7 = **398 / 7 = 56.9k€**
- Mediana (valor central): 28, 32, 35, **38**, 40, 45, 180 = **38k€**
- Rango: 180 - 28 = **152k€**

Interpretar:
- La media (56.9k€) esta muy por encima de lo que gana la mayoria
  porque el valor de 180k€ la "tira" hacia arriba.
- La mediana (38k€) representa mejor el salario tipico de la empresa.
- El valor de 180k€ es un outlier — probablemente el CEO o un directivo.
  No es un error, pero hay que saber que existe cuando se calcula la media.

**Conclusion:** en distribuciones con outliers o asimetria, la mediana
es mas representativa que la media.
