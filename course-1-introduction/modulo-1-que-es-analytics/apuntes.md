# Modulo 1: What is Data Analytics?

**Semana:** 1
**Duracion estimada:** 3 horas

---

## De que va este modulo

Primer modulo del certificado. Explica de cero que es el analisis de datos,
que hace exactamente un analista en su dia a dia, y como se diferencia de
otros roles (cientifico de datos, ingeniero de datos, analista de negocio).
No hay codigo. Todo conceptual — pero es la base de todo lo que viene.

---

## 1. Que es el analisis de datos

**Definicion oficial de IBM:**
El proceso de recopilar, limpiar, analizar e interpretar datos para sacar
conclusiones que apoyen decisiones de negocio.

Mas concretamente: se parte de una pregunta de negocio real ("¿por que
bajaron las ventas en marzo?"), se buscan y preparan los datos relevantes,
se analizan, y se comunican los hallazgos a quien tiene que tomar la decision.

El analisis de datos no es hacer graficos bonitos ni aprender herramientas.
Es un proceso que empieza con una pregunta y termina con una recomendacion.

---

## 2. Los cuatro tipos de analisis

Este es uno de los conceptos mas importantes del certificado — aparece en
el examen final y es la primera pregunta que hace cualquier reclutador.

| Tipo | Pregunta que responde | Herramientas tipicas | Dificultad |
|------|-----------------------|----------------------|------------|
| **Descriptivo** | ¿Que paso? | Excel, SQL, dashboards | Baja |
| **Diagnostico** | ¿Por que paso? | SQL, Python, drill-down | Media |
| **Predictivo** | ¿Que va a pasar? | Python, ML, estadistica | Alta |
| **Prescriptivo** | ¿Que deberia hacer? | ML, optimizacion, simulacion | Muy alta |

**Ejemplo con el mismo escenario (caida de ventas):**

- *Descriptivo:* las ventas cayeron un 18% en marzo respecto a febrero
- *Diagnostico:* la caida se concentro en el segmento premium y coincidio
  con la entrada de un competidor nuevo
- *Predictivo:* si el competidor mantiene la estrategia de precios, las ventas
  seguiran bajando un 8% trimestral durante los proximos 6 meses
- *Prescriptivo:* reducir el precio del producto premium un 12% recuperaria
  el 70% de los clientes perdidos con un impacto marginal en margen

**La mayoria del trabajo junior es descriptivo y diagnostico.** El predictivo
y prescriptivo requieren estadistica avanzada y ML — no es el objetivo del
certificado de analista, es el del cientifico de datos.

---

## 3. El rol del analista de datos

**Lo que hace un analista en un dia tipico:**

- Recibe una pregunta de negocio de un stakeholder
- Identifica que datos necesita y donde estan
- Extrae los datos (SQL, Excel, API)
- Los limpia y transforma hasta que esten listos para analizar
- Analiza: estadisticas, comparaciones, tendencias, segmentaciones
- Crea visualizaciones que comuniquen el hallazgo
- Presenta las conclusiones y recomendaciones

**Lo que NO hace (en general):**

- Construir modelos de machine learning — eso es el cientifico de datos
- Diseñar la infraestructura de datos — eso es el ingeniero de datos
- Tomar la decision final — eso es el stakeholder o el manager

---

## 4. Los roles del ecosistema de datos

Aqui es donde mucha gente se confunde. Los cuatro roles principales:

**Analista de datos (Data Analyst):**
- Responde preguntas con datos que ya existen
- Herramientas: Excel, SQL, Tableau, Python basico
- Perfil: mas orientado a negocio que a ingenieria

**Cientifico de datos (Data Scientist):**
- Construye modelos predictivos y trabaja con algoritmos de ML
- Herramientas: Python avanzado, R, TensorFlow, estadistica avanzada
- Perfil: mas matematico e informatico

**Ingeniero de datos (Data Engineer):**
- Construye y mantiene los pipelines y la infraestructura de datos
- Herramientas: Spark, Kafka, Airflow, bases de datos, cloud
- Perfil: mas ingeniero de software

**Analista de negocio (Business Analyst):**
- Traduce las necesidades de negocio en requerimientos para el equipo de datos
- Herramientas: Excel, PowerPoint, herramientas de BI
- Perfil: mas orientado a proceso y estrategia que a datos

**Regla rapida para distinguirlos:**
- "¿Que paso y por que?" → Analista de datos
- "¿Que va a pasar?" → Cientifico de datos
- "¿Como movemos los datos?" → Ingeniero de datos
- "¿Que necesita el negocio?" → Analista de negocio

---

## 5. El proceso de analisis de datos

IBM usa este framework de 6 pasos que aparece a lo largo de todo el
certificado:

```
1. DEFINIR        →  Que pregunta quiero responder
2. RECOPILAR      →  Donde estan los datos y como los consigo
3. PREPARAR       →  Limpiar, transformar, estandarizar
4. ANALIZAR       →  Estadisticas, correlaciones, segmentaciones
5. VISUALIZAR     →  Comunicar los hallazgos visualmente
6. COMUNICAR      →  Presentar conclusiones y recomendaciones
```

Cada uno de estos pasos corresponde a un bloque de cursos del certificado.

**Lo importante:** el proceso no es lineal. Se puede volver a pasos anteriores
— si al analizar se detecta que los datos tienen un problema de calidad, hay
que volver a "preparar". Si al visualizar se ve que la pregunta original estaba
mal planteada, hay que volver a "definir".

---

## 6. Por que los datos importan en las empresas

Tres casos de uso reales que el modulo usa como ejemplo:

**Netflix:**
El algoritmo de recomendacion se basa en analisis del historial de visualizacion
de millones de usuarios. Sin ese analisis, los usuarios pasarian mas tiempo
buscando y menos viendo — lo que se traduce en mas cancelaciones. Se estima
que el sistema de recomendaciones vale 1 billón de dolares anuales en retencion.

**Amazon:**
La funcion "los clientes que compraron esto tambien compraron..." es un modelo
de asociacion (reglas de asociacion / market basket analysis). Aumenta el ticket
medio y reduce el tiempo de decision de compra.

**Logistica (ejemplo generico):**
Un analista detecta que los retrasos en entregas se concentran en rutas
especificas y en dias con lluvia. La empresa reasigna recursos preventivamente
cuando el tiempo lo predice. Reduccion del 23% en retrasos.

El patron comun: **los datos convierten intuicion en evidencia**, y la evidencia
permite tomar decisiones mas baratas de equivocar.

---

## Glosario del modulo

| Termino | Definicion |
|---------|------------|
| Analisis de datos | Proceso de recopilar, limpiar, analizar e interpretar datos para apoyar decisiones |
| Analisis descriptivo | Tipo de analisis que responde "que paso" usando datos historicos |
| Analisis diagnostico | Tipo de analisis que responde "por que paso" identificando causas |
| Analisis predictivo | Uso de modelos estadisticos o ML para anticipar resultados futuros |
| Analisis prescriptivo | Recomendaciones sobre que accion tomar, basadas en analisis predictivo |
| Analista de datos | Profesional que extrae, limpia y analiza datos para responder preguntas de negocio |
| Cientifico de datos | Profesional que construye modelos de ML y trabaja con datos a escala |
| Ingeniero de datos | Profesional que diseña y mantiene la infraestructura de datos |
| Analista de negocio | Profesional que traduce necesidades de negocio en requerimientos de datos |
| Stakeholder | Persona o grupo con interes en los resultados del analisis |
| Toma de decisiones basada en datos | Usar evidencia factual en lugar de intuicion para guiar las decisiones |
| Pipeline de datos | Flujo automatizado que mueve datos desde la fuente hasta el destino |

---

## Lo mas importante de este modulo

Dos ideas que hay que tener claras antes de seguir:

1. **El analisis empieza con una pregunta, no con los datos.** Si no sabes que
   quieres responder, no sabes que datos buscar ni como interpretarlos.

2. **Los cuatro tipos de analisis son un espectro de complejidad.** El
   descriptivo es el punto de partida — el 80% del trabajo real es descriptivo
   y diagnostico. No hay que apresurarse a hacer ML si la pregunta se puede
   responder con un buen grafico de barras.
