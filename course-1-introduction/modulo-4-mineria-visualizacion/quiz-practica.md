# Quiz de Practica — Modulo 4: Mining & Visualizing Data and Communicating Results

---

**1. Una empresa observa que en los meses que vende mas helados tambien
hay mas ahogamientos en piscinas. ¿Que conclusion es correcta?**

a) Comer helados aumenta el riesgo de ahogarse
b) Hay correlacion pero no causalidad — el calor explica ambos
c) Hay causalidad — los helados causan ahogamientos
d) No hay ninguna relacion entre las dos variables

<details>
<summary>Respuesta</summary>

**b).** Hay correlacion (las dos variables suben juntas) pero la causa
de ambas es una tercera variable: el calor. En verano se venden mas
helados Y hay mas gente banandose. Ninguna de las dos causa la otra.

Este es el ejemplo clasico de **variable de confusion** (confounding variable).

</details>

---

**2. Un director de ventas pide un informe de los resultados del ultimo
trimestre. ¿Como deberia estructurarse la presentacion?**

<details>
<summary>Respuesta</summary>

Para un directivo:
1. Los 3-4 hallazgos principales primero (lo mas importante al inicio)
2. Comparativa con el trimestre anterior o con el objetivo
3. Una o dos recomendaciones concretas y accionables
4. Graficos simples — no tablas de datos crudos

Lo que hay que evitar: metodologia detallada, codigo, tablas con muchas
columnas, jerga estadistica. El CEO no necesita saber como se limpiaron
los datos — necesita saber que hacer con los resultados.

</details>

---

**3. Se quiere mostrar como han evolucionado los ingresos de una empresa
mes a mes durante los ultimos 2 anos. ¿Que tipo de grafico es el mas adecuado?**

<details>
<summary>Respuesta</summary>

**Grafico de lineas.** Es el tipo correcto para mostrar la evolucion de
una variable continua a lo largo del tiempo.

Las barras tambien funcionan para series temporales, pero las lineas
muestran mejor la tendencia y la continuidad.

</details>

---

**4. ¿Por que puede ser mejor usar la mediana que la media para describir
los salarios de una empresa?**

<details>
<summary>Respuesta</summary>

Porque los salarios suelen tener una distribucion asimetrica: la mayoria
de empleados gana sueldos normales, pero unos pocos directivos ganan
mucho mas. Esos valores altos "tiran" de la media hacia arriba, haciendo
que parezca que el sueldo tipico es mas alto de lo que realmente es.

La mediana no se ve afectada por los valores extremos — representa
el salario de la persona que esta exactamente en el medio de la distribucion.

Ejemplo: empresa con 10 empleados, 9 ganan 30.000€ y 1 gana 300.000€.
- Media: 57.000€ (no representa a nadie)
- Mediana: 30.000€ (representa a la mayoria)

</details>

---

**5. ¿Que tiene de malo este titulo de grafico: "Ventas 2023"?**

<details>
<summary>Respuesta</summary>

No comunica ningun hallazgo. Solo describe el contenido del grafico,
no lo que significa.

Un titulo mejor: "Las ventas crecieron un 18% respecto a 2022, impulsadas
por el segmento premium" — esto si dice algo accionable.

El titulo del grafico debe responder la pregunta: ¿que quiero que el
lector se lleve despues de ver este grafico?

</details>

---

**6. ¿Que tecnica de mineria de datos usaria para segmentar a los clientes
de un banco en grupos con comportamiento similar, sin categorias predefinidas?**

<details>
<summary>Respuesta</summary>

**Clustering.** Es la tecnica que agrupa registros similares sin necesitar
etiquetas o categorias previas. El algoritmo encuentra los grupos de forma
automatica basandose en las caracteristicas de los datos.

Si las categorias estuvieran definidas de antemano (por ejemplo, "cliente
de alto valor" vs "cliente de bajo valor") y hubiera datos etiquetados,
se usaria clasificacion.

</details>

---

**7. Un analista trunca el eje Y de un grafico de barras para que empiece
en 95 en vez de en 0, haciendo que una diferencia de 2 puntos parezca
enorme. ¿Que principio de visualizacion viola?**

<details>
<summary>Respuesta</summary>

Viola el principio de **integridad grafica**: el tamano visual debe ser
proporcional al dato real. Truncar el eje exagera las diferencias y puede
llevar a conclusiones incorrectas al lector.

En graficos de barras, el eje Y debe empezar en cero. En graficos de
lineas puede empezar en otro valor si se indica claramente, pero en barras
la altura de la barra representa la magnitud total, no la diferencia.

</details>

---

**8. Verdadero o falso: el objetivo de la visualizacion es mostrar todos
los datos disponibles para que el lector pueda sacar sus propias conclusiones.**

<details>
<summary>Respuesta</summary>

**Falso.** El objetivo de la visualizacion es comunicar un hallazgo
especifico de forma clara y eficiente. Mostrar todos los datos sin
un mensaje claro produce graficos sobrecargados que nadie entiende.

Cada grafico debe tener un unico mensaje. Si hay muchos hallazgos,
se hacen varios graficos enfocados, no uno con todo dentro.

</details>
