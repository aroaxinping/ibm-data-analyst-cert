# Quiz de Practica — Modulo 1: What is Data Analytics?

Preguntas del estilo de las que aparecen en los quizzes del curso.
Intentar responder antes de mirar la respuesta.

---

**1. Una empresa quiere saber cuantas unidades vendio por region el mes pasado.
¿Que tipo de analisis es?**

<details>
<summary>Respuesta</summary>

**Descriptivo.** Responde "que paso" con datos historicos. No busca causas
ni hace predicciones, solo describe el estado actual o pasado.

</details>

---

**2. Un modelo predice que las ventas del proximo trimestre bajaran un 15%
si no se cambia la estrategia de precios. ¿Que tipo de analisis es?**

<details>
<summary>Respuesta</summary>

**Predictivo.** Usa datos historicos y modelos estadisticos para anticipar
resultados futuros. El modelo no recomienda que hacer — solo predice.

</details>

---

**3. ¿Cual es la diferencia principal entre un analista de datos y un
cientifico de datos?**

<details>
<summary>Respuesta</summary>

El **analista de datos** trabaja con datos existentes para responder preguntas
concretas usando herramientas como Excel, SQL y Python basico. Su trabajo
es principalmente descriptivo y diagnostico.

El **cientifico de datos** construye modelos predictivos nuevos, trabaja con
algoritmos de machine learning y estadistica avanzada. Su trabajo incluye
crear sistemas que aprenden de los datos.

En la practica: el analista responde preguntas del pasado y presente; el
cientifico predice el futuro y automatiza la prediccion.

</details>

---

**4. Una empresa descubre que sus ventas online caen siempre los lunes.
Un analista investiga y encuentra que el servidor tiene picos de latencia
los lunes por la mañana. ¿Que tipo de analisis hizo el analista?**

<details>
<summary>Respuesta</summary>

**Diagnostico.** Identifico la causa de un patron conocido (caida de ventas).
El primer paso — detectar la caida — era descriptivo. Pero encontrar la razon
(latencia del servidor) es diagnostico.

</details>

---

**5. Verdadero o falso: el proceso de analisis de datos siempre sigue un
orden lineal de principio a fin.**

<details>
<summary>Respuesta</summary>

**Falso.** El proceso es iterativo. Es comun volver a etapas anteriores —
por ejemplo, si al analizar se detecta un problema de calidad en los datos,
hay que volver a la etapa de preparacion. Si la pregunta original estaba
mal planteada, hay que volver a definirla.

</details>

---

**6. ¿Cual de estos ejemplos corresponde a analisis prescriptivo?**

a) Las ventas cayeron un 20% en diciembre
b) La caida se debe a que un competidor bajo sus precios
c) Si reducimos el precio un 10%, recuperaremos el 60% de los clientes
d) Recomendamos reducir el precio un 10% para recuperar cuota de mercado

<details>
<summary>Respuesta</summary>

**d)** El prescriptivo va un paso mas alla del predictivo: no solo predice
lo que pasara (c), sino que **recomienda la accion concreta** a tomar.

- a) = descriptivo
- b) = diagnostico
- c) = predictivo
- d) = prescriptivo

</details>

---

**7. ¿Que hace un ingeniero de datos que no hace un analista de datos?**

<details>
<summary>Respuesta</summary>

El **ingeniero de datos** diseña, construye y mantiene la infraestructura
que permite que los datos fluyan desde las fuentes hasta donde se usan:
pipelines ETL, bases de datos, sistemas de almacenamiento en la nube, etc.

El **analista de datos** usa esa infraestructura para extraer y analizar datos,
pero no la construye. El analista es "consumidor" de la infraestructura que
el ingeniero crea.

</details>

---

**8. Una empresa usa datos de clientes para recomendar que accion tomar con
cada cuenta para maximizar la probabilidad de renovacion. ¿Que tipo de analisis es?**

<details>
<summary>Respuesta</summary>

**Prescriptivo.** El sistema no solo predice quien va a cancelar (predictivo),
sino que recomienda la accion especifica a realizar con cada cliente para
evitarlo. Es el tipo de analisis mas avanzado y suele requerir ML.

</details>

---

## Preguntas de reflexion (sin respuesta unica)

Estas no aparecen en el quiz oficial, pero ayudan a asentar los conceptos:

- En tu sector o en una empresa que conozcas, ¿que preguntas de negocio
  podrian responderse con analisis descriptivo? ¿Y con diagnostico?
- ¿Por que crees que la mayoria del trabajo real de un analista junior
  es descriptivo y diagnostico, y no predictivo?
- ¿Que riesgos tiene tomar decisiones basadas solo en intuicion sin datos?
  ¿Y basadas solo en datos sin contexto de negocio?
