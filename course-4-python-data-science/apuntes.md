# Apuntes — Course 4: Python for Data Science, AI & Development

**Duracion:** 25 horas
**Modulos:** 5

---

## Que cubre este curso

Python desde cero con enfoque en data science. El curso es mas amplio que
el equivalente del certificado de Google — cubre no solo pandas sino tambien
NumPy, APIs REST y web scraping con Beautiful Soup.

---

## Modulo 1: Python Basics

**Tipos de datos basicos:**

| Tipo | Ejemplo | Descripcion |
|------|---------|-------------|
| `int` | `42` | Entero |
| `float` | `3.14` | Decimal |
| `str` | `"hola"` | Cadena de texto |
| `bool` | `True` / `False` | Booleano |
| `NoneType` | `None` | Ausencia de valor |

**Variables:**
```python
nombre = "Ana"
edad = 28
precio = 19.99
activo = True
```

Python no requiere declarar el tipo — se infiere del valor asignado.

**Operadores:**

```python
# Aritmeticos
5 + 3    # 8
10 - 4   # 6
3 * 4    # 12
10 / 3   # 3.333... (division real)
10 // 3  # 3 (division entera)
10 % 3   # 1 (modulo / resto)
2 ** 3   # 8 (potencia)

# Comparacion
==  !=  >  <  >=  <=

# Logicos
and  or  not
```

**Strings:**
```python
s = "Python para Data Science"

len(s)           # 24 — longitud
s.upper()        # "PYTHON PARA DATA SCIENCE"
s.lower()        # "python para data science"
s.split(" ")     # ["Python", "para", "Data", "Science"]
s.replace("Python", "R")  # "R para Data Science"
s[0:6]           # "Python" — slicing
f"Hola, {nombre}"  # f-string — interpolacion

# Metodos utiles
s.strip()        # eliminar espacios al inicio y final
s.startswith("P")  # True
s.find("Data")   # 12 — posicion primera ocurrencia
```

**Input / output:**
```python
nombre = input("Como te llamas? ")
print(f"Hola, {nombre}")
print("Texto", variable, sep=" — ", end="\n")
```

---

## Modulo 2: Python Data Structures

**Listas:**
```python
lista = [1, 2, 3, "cuatro", True]

# Acceso
lista[0]     # 1
lista[-1]    # True (ultimo elemento)
lista[1:3]   # [2, 3] — slicing

# Modificar
lista.append(5)         # añadir al final
lista.insert(2, "X")   # insertar en posicion
lista.remove("cuatro") # eliminar por valor
lista.pop(0)           # eliminar por indice, devuelve el elemento
lista.sort()           # ordenar in-place (solo funciona si todos son del mismo tipo)
sorted(lista)          # devuelve nueva lista ordenada

# Utiles
len(lista)             # longitud
"cuatro" in lista      # True/False
lista.index("cuatro")  # posicion del elemento
```

**Tuplas:**
```python
tupla = (1, 2, 3)
# Igual que lista pero inmutable — no se puede modificar despues de crear
# Mas eficiente en memoria que la lista
# Uso tipico: coordenadas, registros que no deben cambiar
```

**Diccionarios:**
```python
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Barcelona"
}

# Acceso
persona["nombre"]         # "Ana"
persona.get("pais", "ES") # "ES" si "pais" no existe (evita KeyError)

# Modificar
persona["email"] = "ana@email.com"  # añadir / actualizar
del persona["ciudad"]               # eliminar

# Iterar
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

persona.keys()    # dict_keys con todas las claves
persona.values()  # dict_values con todos los valores
```

**Sets:**
```python
conjunto = {1, 2, 3, 3, 2}  # {1, 2, 3} — no hay duplicados
conjunto.add(4)
conjunto.remove(1)

# Operaciones de conjuntos
A | B   # union
A & B   # interseccion
A - B   # diferencia
A ^ B   # diferencia simetrica
```

**Comprensiones de lista:**
```python
cuadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
mayusculas = [s.upper() for s in ["ana", "luis", "marta"]]
```

---

## Modulo 3: Python Programming Fundamentals

**Condicionales:**
```python
if edad >= 18:
    print("Mayor de edad")
elif edad >= 16:
    print("Casi")
else:
    print("Menor de edad")

# Expresion ternaria
estado = "activo" if activo else "inactivo"
```

**Bucles:**
```python
# for
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for elemento in lista:
    print(elemento)

for i, elemento in enumerate(lista):
    print(f"{i}: {elemento}")

for clave, valor in diccionario.items():
    print(f"{clave} = {valor}")

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Control de bucle
break     # salir del bucle
continue  # saltar a la siguiente iteracion
```

**Funciones:**
```python
def saludar(nombre, mensaje="Hola"):
    """Docstring: describe la funcion."""
    return f"{mensaje}, {nombre}!"

# Llamada
saludar("Ana")             # "Hola, Ana!"
saludar("Luis", "Buenos dias")

# *args y **kwargs
def suma(*numeros):
    return sum(numeros)

def crear_perfil(**datos):
    return datos

# Lambda (funcion anonima)
cuadrado = lambda x: x ** 2
ordenar_por_edad = sorted(personas, key=lambda p: p["edad"])
```

**Manejo de excepciones:**
```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Tipo o valor incorrecto")
else:
    print("Sin errores")
finally:
    print("Esto siempre se ejecuta")
```

**Ficheros:**
```python
# Leer
with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    lineas = f.readlines()

# Escribir
with open("resultado.txt", "w", encoding="utf-8") as f:
    f.write("Linea 1\n")

# CSV con pandas (mas comun en data science)
import pandas as pd
df = pd.read_csv("datos.csv")
df.to_csv("resultado.csv", index=False)
```

---

## Modulo 4: Working with Data in Python

**NumPy:**
```python
import numpy as np

# Arrays
arr = np.array([1, 2, 3, 4, 5])
matriz = np.array([[1, 2], [3, 4], [5, 6]])

# Crear arrays
np.zeros((3, 4))          # matriz 3x4 de ceros
np.ones((2, 3))           # matriz 2x3 de unos
np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)      # 5 valores entre 0 y 1

# Propiedades
arr.shape     # (5,)
arr.dtype     # dtype('int64')
arr.size      # 5

# Operaciones vectorizadas (mucho mas rapidas que bucles)
arr * 2              # [2, 4, 6, 8, 10]
arr + np.array([10, 20, 30, 40, 50])
np.sqrt(arr)

# Estadisticas
np.mean(arr)    # media
np.median(arr)  # mediana
np.std(arr)     # desviacion tipica
np.max(arr)     # maximo
np.min(arr)     # minimo

# Indexing y slicing (igual que listas pero mas potente)
arr[2]           # elemento en posicion 2
arr[1:4]         # elementos del 1 al 3
arr[arr > 3]     # elementos mayores que 3 (boolean indexing)
```

**pandas — lo esencial:**
```python
import pandas as pd

# Crear DataFrame
df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta"],
    "edad": [28, 34, 22],
    "ciudad": ["BCN", "MAD", "VAL"]
})

# Leer datos
df = pd.read_csv("datos.csv")
df = pd.read_excel("datos.xlsx")

# Explorar
df.head()          # primeras 5 filas
df.tail(3)         # ultimas 3 filas
df.info()          # tipos y valores no nulos
df.describe()      # estadisticas basicas
df.shape           # (filas, columnas)
df.columns         # nombres de columnas
df.dtypes          # tipo de cada columna

# Seleccion
df["nombre"]               # columna como Series
df[["nombre", "edad"]]     # varias columnas como DataFrame
df.iloc[0]                 # primera fila (por posicion)
df.loc[0, "nombre"]        # celda especifica (por etiqueta)
df[df["edad"] > 25]        # filtrar filas

# Limpieza
df.isnull().sum()               # contar nulos por columna
df.dropna()                     # eliminar filas con nulos
df.fillna(0)                    # rellenar nulos con 0
df.fillna(df["edad"].mean())    # rellenar con la media
df.drop_duplicates()            # eliminar duplicados
df["edad"] = df["edad"].astype(int)  # cambiar tipo

# Transformaciones
df["nueva_col"] = df["edad"] * 2
df.rename(columns={"nombre": "name"}, inplace=True)
df.sort_values("edad", ascending=False)
df.groupby("ciudad")["edad"].mean()

# Merge / join
pd.merge(df1, df2, on="id", how="left")
```

---

## Modulo 5: APIs and Data Collection

**Requests — consumir APIs REST:**
```python
import requests

# GET
respuesta = requests.get("https://api.example.com/data")
respuesta.status_code    # 200 si ok
datos = respuesta.json() # convertir respuesta a dict/lista

# GET con parametros
params = {"ciudad": "Barcelona", "limit": 10}
respuesta = requests.get(url, params=params)

# GET con autenticacion
headers = {"Authorization": "Bearer TOKEN"}
respuesta = requests.get(url, headers=headers)

# POST
payload = {"nombre": "Ana", "email": "ana@email.com"}
respuesta = requests.post(url, json=payload)

# Manejo de errores
if respuesta.status_code == 200:
    datos = respuesta.json()
else:
    print(f"Error: {respuesta.status_code}")
```

**Web scraping con Beautiful Soup:**
```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, "html.parser")

# Encontrar elementos
titulo = soup.find("h1").text
todos_parrafos = soup.find_all("p")
tabla = soup.find("table", {"class": "datos"})

# Extraer texto
for fila in tabla.find_all("tr"):
    celdas = [td.text.strip() for td in fila.find_all("td")]
    print(celdas)

# Nota: siempre revisar los terminos de uso del sitio antes de hacer scraping
```

---

## Esquema resumido del curso

```
COURSE 4: PYTHON
|
+-- Basico
|     Tipos, variables, operadores, strings
|
+-- Estructuras de datos
|     Listas, tuplas, diccionarios, sets, comprensiones
|
+-- Programacion
|     Funciones, bucles, condicionales, excepciones, ficheros
|
+-- Datos
|     NumPy (arrays, operaciones vectorizadas)
|     pandas (DataFrame, limpieza, agrupacion, merge)
|
+-- APIs y scraping
      requests (GET, POST, autenticacion)
      BeautifulSoup (parsing HTML)
```

---

## Glosario

| Termino | Definicion |
|---------|------------|
| Array | Estructura de datos de NumPy: lista de elementos del mismo tipo, optimizada para calculo vectorizado |
| DataFrame | Estructura tabular de pandas con filas y columnas etiquetadas |
| Series | Columna de un DataFrame — array unidimensional con etiquetas |
| Broadcasting | Mecanismo de NumPy para operar arrays de distintas formas sin copiarlos |
| Boolean indexing | Filtrar un array o DataFrame usando una mascara de True/False |
| API REST | Interfaz para comunicarse con un servicio web mediante HTTP |
| JSON | JavaScript Object Notation — formato de datos estandar para APIs |
| Web scraping | Extraccion automatica de datos de paginas web |
| Lambda | Funcion anonima de una sola expresion |
| Comprension de lista | Forma concisa de crear listas aplicando una expresion a cada elemento de un iterable |

---

## Errores comunes

- **Modificar una lista mientras se itera sobre ella:** produce comportamiento
  inesperado. Iterar sobre una copia: `for x in lista[:]`.
- **Confundir `.loc` y `.iloc`:** `.loc` usa etiquetas (nombres), `.iloc` usa
  posiciones numericas. En un DataFrame con indice numerico pueden dar el mismo
  resultado, pero no siempre.
- **Olvidar `inplace=True` en operaciones de pandas:** muchos metodos devuelven
  un nuevo DataFrame en vez de modificar el original. O usar `inplace=True` o
  reasignar: `df = df.dropna()`.
- **No manejar errores en llamadas a APIs:** si la API devuelve un codigo de
  error y se llama `.json()` sin comprobar el status, puede lanzar una excepcion.

---

## Conexion con otros cursos

- Este curso es la base tecnica para los cursos 7 (Data Analysis with Python)
  y 8 (Data Visualization with Python). Los conceptos de pandas y NumPy de
  este curso se amplian significativamente en el 7.
- Las APIs cubiertas en el modulo 5 son relevantes para el capstone (curso 9)
  donde se trabaja con datos reales que a menudo vienen de APIs.
- El curso 5 (Python Project) aplica inmediatamente lo aprendido aqui en
  un proyecto practico con datos financieros reales.
