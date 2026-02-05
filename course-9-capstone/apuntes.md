# Apuntes — Course 9: IBM Data Analyst Capstone Project

**Duracion:** 13 horas
**Modulos:** 6

---

## Que cubre este curso

El capstone es el proyecto integrador del certificado. Se trabaja con datos
reales de la Stack Overflow Developer Survey para responder preguntas sobre
las tendencias tecnologicas del mercado. Cada modulo aplica habilidades de
un curso anterior.

---

## El problema de negocio

Una empresa de tecnologia quiere entender:
- Que lenguajes de programacion estan en mayor demanda actualmente
- Que bases de datos son las mas utilizadas y las mas deseadas
- Que plataformas y web frameworks tienen mayor adopcion
- Que perfil demografico tienen los desarrolladores del sector

Para responder estas preguntas se usa la Stack Overflow Developer Survey,
una encuesta anual con decenas de miles de respuestas de desarrolladores
de todo el mundo.

---

## Modulo 1: Collecting Data

**Fuentes de datos del capstone:**

1. **API de IBM:** dataset de la survey en formato JSON via API REST
2. **Web scraping:** lista de lenguajes mas populares desde una web de rankings
3. **Dataset descargable:** CSV completo de la Stack Overflow Survey

**Recopilar datos via API:**

```python
import requests
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.json"

respuesta = requests.get(url)
datos = respuesta.json()

df = pd.DataFrame(datos)
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
print(df.head())
```

**Web scraping de tecnologias:**

```python
from bs4 import BeautifulSoup
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, "html.parser")

tabla = soup.find("table")
df_lenguajes = pd.read_html(str(tabla))[0]
print(df_lenguajes.head())
```

---

## Modulo 2: Data Wrangling

**Columnas del dataset de la survey:**

Columnas clave:
- `LanguageHaveWorkedWith` — lenguajes con los que ha trabajado
- `LanguageWantToWorkWith` — lenguajes con los que quiere trabajar
- `DatabaseHaveWorkedWith` — bases de datos usadas
- `DatabaseWantToWorkWith` — bases de datos deseadas
- `PlatformHaveWorkedWith` — plataformas usadas
- `WebframeHaveWorkedWith` — frameworks web usados
- `Age`, `Gender`, `Country`, `EdLevel` — datos demograficos
- `YearsCodePro` — años de experiencia profesional
- `CompTotal` — compensacion total

**Limpiar datos:**

```python
# Ver dimension y nulos
print(df.shape)
print(df.isnull().sum().sort_values(ascending=False).head(20))

# Eliminar duplicados por respondente
df.drop_duplicates(subset=["ResponseId"], inplace=True)
print(f"Filas despues de eliminar duplicados: {len(df)}")

# Tratar nulos en columna de compensacion
df["CompTotal"].fillna(df["CompTotal"].median(), inplace=True)

# Estandarizar experiencia (algunos valores son strings: "Less than 1 year", "More than 50 years")
df["YearsCodePro"] = df["YearsCodePro"].replace({
    "Less than 1 year": 0,
    "More than 50 years": 50
})
df["YearsCodePro"] = pd.to_numeric(df["YearsCodePro"], errors="coerce")
df["YearsCodePro"].fillna(df["YearsCodePro"].median(), inplace=True)
```

**Expandir columnas multi-valor:**

Las columnas de lenguajes/bases de datos contienen valores separados por ";".
Para analizarlas hay que expandirlas:

```python
# Contar cuantos usan cada lenguaje
lenguajes_usados = (
    df["LanguageHaveWorkedWith"]
    .dropna()
    .str.split(";")
    .explode()
    .str.strip()
    .value_counts()
    .reset_index()
)
lenguajes_usados.columns = ["Lenguaje", "Conteo"]
print(lenguajes_usados.head(10))
```

---

## Modulo 3: Exploratory Data Analysis

**Distribucion de variables clave:**

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Compensacion
print("Compensacion:")
print(df["CompTotal"].describe())
print(f"Mediana: {df['CompTotal'].median():.0f}")

# Outliers en compensacion
Q1 = df["CompTotal"].quantile(0.25)
Q3 = df["CompTotal"].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df["CompTotal"] < Q1 - 1.5*IQR) | (df["CompTotal"] > Q3 + 1.5*IQR)]
print(f"Outliers: {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)")

# Top 10 lenguajes usados
top_lenguajes = lenguajes_usados.head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_lenguajes, x="Conteo", y="Lenguaje",
            palette="Blues_r", ax=ax)
ax.set_title("Top 10 lenguajes de programacion mas usados")
plt.tight_layout()
```

**Correlaciones:**

```python
correlaciones = df[["YearsCodePro", "CompTotal", "Age"]].corr()
sns.heatmap(correlaciones, annot=True, cmap="coolwarm")
```

**Analisis por grupos:**

```python
# Compensacion por nivel educativo
df.groupby("EdLevel")["CompTotal"].median().sort_values(ascending=False)

# Lenguajes mas deseados vs mas usados
deseados = df["LanguageWantToWorkWith"].dropna().str.split(";").explode().value_counts().head(10)
usados = df["LanguageHaveWorkedWith"].dropna().str.split(";").explode().value_counts().head(10)
```

---

## Modulo 4: SQL

Los datos se cargan en una base de datos SQLite para practicar el analisis
con SQL directamente.

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///survey.db")
df.to_sql("survey", engine, if_exists="replace", index=False)
```

**Queries del capstone:**

```sql
-- Top 5 paises por numero de respondentes
SELECT Country, COUNT(*) AS respondentes
FROM survey
GROUP BY Country
ORDER BY respondentes DESC
LIMIT 5;

-- Compensacion media por nivel educativo
SELECT EdLevel,
       COUNT(*) AS respondentes,
       AVG(CompTotal) AS comp_media,
       MEDIAN(CompTotal) AS comp_mediana
FROM survey
GROUP BY EdLevel
ORDER BY comp_media DESC;

-- Desarrolladores que usan Python y quieren aprender Rust
SELECT COUNT(*) AS pythonistas_que_quieren_rust
FROM survey
WHERE LanguageHaveWorkedWith LIKE '%Python%'
  AND LanguageWantToWorkWith LIKE '%Rust%';

-- Bases de datos mas deseadas
SELECT db, COUNT(*) AS interesados
FROM (
    SELECT TRIM(value) AS db
    FROM survey, json_each('["' || REPLACE(DatabaseWantToWorkWith, ';', '","') || '"]')
    WHERE DatabaseWantToWorkWith IS NOT NULL
)
GROUP BY db
ORDER BY interesados DESC
LIMIT 10;
```

---

## Modulo 5: Data Visualization y Dashboard

**Dashboard en Cognos / IBM Analytics:**

El dashboard del capstone tiene tres pestañas:
- **Current Technology Usage:** lenguajes, bases de datos y plataformas actuales
- **Future Technology Trends:** lenguajes y bases de datos deseados
- **Demographics:** perfil de los respondentes (edad, pais, educacion, experiencia)

**Graficos del dashboard:**

```
CURRENT USAGE
- Barras: Top 10 lenguajes usados
- Barras: Top 10 bases de datos usadas
- Treemap: plataformas usadas

FUTURE TRENDS
- Barras: Top 10 lenguajes deseados
- Barras: Top 10 bases de datos deseadas
- Burbujas: frameworks mas deseados

DEMOGRAPHICS
- Mapa: distribucion de respondentes por pais
- Barras: distribucion por edad
- Circular: nivel educativo
- Barras: genero
```

---

## Modulo 6: Presentacion de Resultados

**Estructura del informe final:**

1. **Executive Summary:** 3-4 bullets con los hallazgos principales
2. **Metodologia:** fuentes de datos, proceso de limpieza, herramientas
3. **Hallazgos — Uso actual:**
   - Top lenguajes: JavaScript, Python, SQL, TypeScript, Java
   - Top bases de datos: MySQL, PostgreSQL, SQLite, MongoDB
   - Top plataformas: Linux, AWS, Docker
4. **Hallazgos — Tendencias futuras:**
   - Lenguajes en alza: Rust, Kotlin, Go
   - Bases de datos en alza: PostgreSQL, Redis, MongoDB
5. **Hallazgos — Perfil demografico:**
   - Distribucion de edad, pais, experiencia
   - Brecha de genero en el sector
6. **Limitaciones:** sesgo de la muestra (los que responden a SO survey
   no representan a todos los desarrolladores del mundo)
7. **Recomendaciones:** basadas en los hallazgos

**Principios de storytelling con datos:**

- Empezar con el hallazgo mas importante, no con la metodologia
- Usar visualizaciones que el publico entienda sin explicacion
- Comparar siempre respecto a algo: año anterior, benchmark, media
- Ser explicito sobre las limitaciones — genera credibilidad
- Terminar con una recomendacion concreta y accionable

---

## Esquema del proyecto completo

```
CAPSTONE: STACK OVERFLOW DEVELOPER SURVEY
|
+-- Modulo 1: Recopilacion
|     API REST + web scraping + CSV
|
+-- Modulo 2: Wrangling
|     Nulos, duplicados, columnas multi-valor, tipos
|
+-- Modulo 3: EDA
|     Distribuciones, outliers, correlaciones, agrupaciones
|
+-- Modulo 4: SQL
|     Queries sobre SQLite: top listas, comparaciones, segmentaciones
|
+-- Modulo 5: Visualizacion
|     Dashboard en Cognos: 3 pestañas, 9 graficos
|
+-- Modulo 6: Presentacion
      Informe estructurado con hallazgos y recomendaciones
```

---

## Hallazgos principales

_(completar al terminar el curso — aqui se pondran los resultados reales)_

**Lenguajes mas usados actualmente:**
1.
2.
3.

**Lenguajes mas deseados (tendencia futura):**
1.
2.
3.

**Bases de datos mas deseadas:**
1.
2.
3.

---

## Conexion con todos los cursos anteriores

Este capstone integra todo el certificado:

| Modulo | Habilidad aplicada | Curso de origen |
|--------|--------------------|-----------------|
| 1 | API REST + web scraping | Curso 4 (Python) |
| 2 | Wrangling con pandas | Cursos 4 y 7 |
| 3 | EDA y estadistica | Curso 7 |
| 4 | SQL sobre datos reales | Curso 6 |
| 5 | Dashboard en Cognos | Cursos 3 y 8 |
| 6 | Storytelling y presentacion | Curso 1 (comunicar resultados) |
