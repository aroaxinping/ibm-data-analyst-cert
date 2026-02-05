# Modulo 1: Python Basics — Ejercicios

# Tipos y variables
nombre = "Ana"
edad = 28
precio = 19.99
activo = True

print(type(nombre))   # <class 'str'>
print(type(edad))     # <class 'int'>
print(type(precio))   # <class 'float'>
print(type(activo))   # <class 'bool'>

# Operaciones con strings
texto = "Python para Data Science"
print(len(texto))              # 24
print(texto.upper())
print(texto.split(" "))
print(texto[0:6])              # "Python"
print(f"Hola, {nombre}! Tienes {edad} años.")

# Operaciones numericas
print(10 // 3)   # 3 — division entera
print(10 % 3)    # 1 — modulo
print(2 ** 8)    # 256 — potencia

# Conversion de tipos
numero_str = "42"
numero_int = int(numero_str)
numero_float = float(numero_str)
de_vuelta_str = str(numero_int)

print(type(numero_int))   # <class 'int'>
