# Modulo 2: Python Data Structures — Ejercicios

# --- LISTAS ---
frutas = ["manzana", "pera", "naranja", "uva"]

frutas.append("melon")
frutas.insert(1, "kiwi")
frutas.remove("pera")

print(frutas)
print(frutas[0])    # primer elemento
print(frutas[-1])   # ultimo elemento
print(frutas[1:3])  # slicing

# Comprension de lista
cuadrados = [x**2 for x in range(1, 11)]
pares = [x for x in range(20) if x % 2 == 0]
print(cuadrados)
print(pares)

# --- DICCIONARIOS ---
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Barcelona"
}

persona["email"] = "ana@email.com"
print(persona.get("pais", "No especificado"))

for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# Comprension de diccionario
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(cuadrados_dict)

# --- SETS ---
colores_a = {"rojo", "azul", "verde"}
colores_b = {"azul", "amarillo", "verde"}

print(colores_a | colores_b)  # union
print(colores_a & colores_b)  # interseccion
print(colores_a - colores_b)  # diferencia

# --- TUPLAS ---
coordenadas = (41.3851, 2.1734)  # Barcelona
print(f"Lat: {coordenadas[0]}, Lon: {coordenadas[1]}")
# coordenadas[0] = 0  # TypeError: no se puede modificar
