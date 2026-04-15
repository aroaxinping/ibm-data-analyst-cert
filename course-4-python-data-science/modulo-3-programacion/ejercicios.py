# Modulo 3: Python Programming Fundamentals — Ejercicios

# --- FUNCIONES ---
def calcular_imc(peso_kg, altura_m):
    """Calcula el Indice de Masa Corporal."""
    imc = peso_kg / (altura_m ** 2)
    return round(imc, 2)

def clasificar_imc(imc):
    """Clasifica el IMC segun la OMS."""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

imc = calcular_imc(70, 1.75)
print(f"IMC: {imc} — {clasificar_imc(imc)}")

# --- FUNCIONES CON *args Y **kwargs ---
def suma_total(*numeros):
    return sum(numeros)

def crear_registro(**campos):
    return campos

print(suma_total(1, 2, 3, 4, 5))
print(crear_registro(nombre="Ana", edad=28, ciudad="BCN"))

# --- LAMBDA ---
cuadrado = lambda x: x ** 2
personas = [{"nombre": "Ana", "edad": 28}, {"nombre": "Luis", "edad": 22}]
ordenados = sorted(personas, key=lambda p: p["edad"])
print(ordenados)

# --- MAP Y FILTER ---
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(cuadrados)
print(pares)

# --- EXCEPCIONES ---
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return None
    except TypeError:
        print("Los argumentos deben ser numericos")
        return None
    else:
        return resultado

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir("a", 2))
