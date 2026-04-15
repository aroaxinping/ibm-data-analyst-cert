# Modulo 3: Analyzing Data with Spreadsheets

**Semana:** 2-3
**Duracion estimada:** 3 horas

---

## De que va este modulo

Las funciones de analisis: logicas, de busqueda y estadisticas. Con estas
herramientas se pueden responder preguntas sobre los datos directamente
en Excel sin necesidad de exportar ni usar otra herramienta. Es el modulo
mas extenso en terminos de funciones.

---

## 1. Funciones logicas

Las funciones logicas permiten tomar decisiones dentro de una formula
segun si se cumple o no una condicion.

**SI:**
```
=SI(condicion, valor_si_verdadero, valor_si_falso)

=SI(A1>100, "Alto", "Bajo")
=SI(B2="", "Sin datos", B2)
=SI(C3>=0, C3, 0)    -> si es negativo, poner 0
```

**SI anidado:**
```
=SI(A1>100, "Alto",
    SI(A1>50, "Medio",
        "Bajo"))
```
Funciona pero es dificil de leer con mas de 2 niveles.

**SI.CONJUNTO (mejor que SI anidado):**
```
=SI.CONJUNTO(
    A1>100, "Alto",
    A1>50,  "Medio",
    A1>=0,  "Bajo",
    VERDADERO, "Negativo"
)
```
El ultimo par `VERDADERO, "valor"` actua como el "else" — captura
cualquier caso que no cumpla las condiciones anteriores.

**Y / O / NO:**
```
=Y(A1>0, B1<100)        TRUE solo si AMBAS son verdad
=O(A1="Madrid", A1="Barcelona")  TRUE si CUALQUIERA es verdad
=NO(A1="Cancelado")     invierte el resultado

=SI(Y(A1>0, B1="Activo"), "Valido", "No valido")
```

**IFERROR — manejar errores:**
```
=IFERROR(formula, valor_si_error)

=IFERROR(A1/B1, 0)              si da error, devuelve 0
=IFERROR(BUSCARV(...), "N/A")   si no encuentra, devuelve "N/A"
```
Muy util para evitar que los errores `#DIV/0!` o `#N/A` rompan el aspecto
de un informe.

---

## 2. Funciones de busqueda

Las funciones de busqueda conectan datos entre tablas distintas, como
un JOIN de SQL pero en Excel.

**BUSCARV (VLOOKUP):**
```
=BUSCARV(valor_buscado, tabla, num_columna, [coincidencia_exacta])

=BUSCARV(A2, $E$2:$G$100, 2, 0)
```

- `A2`: el valor que se busca
- `$E$2:$G$100`: la tabla donde buscar (bloqueada con $ para copiar)
- `2`: devuelve el valor de la 2a columna de la tabla
- `0`: coincidencia exacta (siempre usar 0 en analisis de datos)

**Limitaciones de BUSCARV:**
- Solo busca de izquierda a derecha — el valor buscado debe estar
  en la primera columna de la tabla
- Si se inserta una columna en la tabla, el numero de columna queda
  desactualizado
- Solo devuelve la primera coincidencia

**BUSCARH (HLOOKUP):**
```
=BUSCARH(valor_buscado, tabla, num_fila, [coincidencia_exacta])
```
Igual que BUSCARV pero busca horizontalmente (en filas en vez de columnas).

**INDICE + COINCIDIR (la alternativa potente):**
```
=INDICE(rango_resultado, COINCIDIR(valor, rango_busqueda, 0))

=INDICE($B$2:$B$100, COINCIDIR(A2, $A$2:$A$100, 0))
```

`COINCIDIR` devuelve la posicion (numero de fila) donde esta el valor.
`INDICE` devuelve el valor en esa posicion de otro rango.

Ventajas sobre BUSCARV:
- Puede buscar en cualquier direccion (no solo izquierda a derecha)
- No se rompe si se insertan columnas
- Mas flexible para construir busquedas complejas

**BUSCARX (Excel 365 / 2021):**
```
=BUSCARX(valor, rango_busqueda, rango_resultado, [si_no_encontrado])

=BUSCARX(A2, $E$2:$E$100, $G$2:$G$100, "No encontrado")
```
La version moderna que sustituye a BUSCARV y BUSCARH. Puede buscar en
cualquier direccion y tiene parametro de valor por defecto integrado.

---

## 3. Funciones estadisticas

Van mas alla de SUMA y PROMEDIO para analisis mas completos.

**Estadisticas descriptivas:**
```
=MEDIANA(A1:A100)               valor central real
=MODA(A1:A100)                  valor mas frecuente
=MODA.UNO(A1:A100)              version actualizada de MODA
=DESVEST(A1:A100)               desviacion tipica muestral
=DESVESTP(A1:A100)              desviacion tipica poblacional
=VAR(A1:A100)                   varianza muestral
=PERCENTIL(A1:A100, 0.75)       percentil 75 (Q3)
=CUARTIL(A1:A100, 1)            Q1 (primer cuartil)
=CUARTIL(A1:A100, 3)            Q3 (tercer cuartil)
=COEF.DE.CORREL(A1:A100, B1:B100)   correlacion de Pearson
```

**Cuando usar DESVEST vs DESVESTP:**
- `DESVEST`: cuando los datos son una muestra de una poblacion mayor
  (lo mas comun en analisis de datos)
- `DESVESTP`: cuando los datos son TODA la poblacion (censos, etc.)
En la practica casi siempre se usa DESVEST.

**Funciones condicionales avanzadas:**
```
=PROMEDIO.SI(rango, criterio, rango_promedio)
=PROMEDIO.SI(B:B, "Madrid", C:C)    media de C donde B es "Madrid"

=SUMAR.SI.CONJUNTO(rango_suma, rango1, criterio1, rango2, criterio2)
=SUMAR.SI.CONJUNTO(C:C, B:B, "Madrid", D:D, ">100")
```

---

## 4. Filtros

Los filtros permiten ver subconjuntos de los datos sin modificarlos.

**Filtro basico:**
Datos > Filtro (o Ctrl+Shift+L). Aparece un desplegable en cada columna
con opciones para filtrar por valor, condicion de texto o condicion numerica.

**Filtros multiples:** se pueden combinar filtros en varias columnas
a la vez. Se aplican con logica AND (todas las condiciones deben cumplirse).

**Funcion FILTRAR (Excel 365 / Google Sheets):**
```
=FILTRAR(rango, condicion, [si_vacio])

=FILTRAR(A2:D100, C2:C100="Madrid", "Sin resultados")
```
Devuelve un rango dinamico con solo las filas que cumplen la condicion.
La ventaja sobre el filtro manual: es una formula, se actualiza automaticamente
y no modifica los datos originales.

---

## 5. Autosum y estadisticas rapidas

**AutoSum:** con Alt+= en una celda debajo o a la derecha de un rango,
Excel inserta automaticamente `=SUMA()` del rango adyacente.

Al desplegar el boton de AutoSum en la cinta, tambien permite insertar
rapidamente PROMEDIO, CONTAR, MAX y MIN.

Esto es exactamente lo que se hace en la Part 2 del proyecto de Montgomery
sobre la columna C (Equipment Count): seleccionar las celdas debajo del
rango y aplicar AutoSum para obtener SUM=1582, AVG=32.29, MIN=1, MAX=379, COUNT=49.

---

## Glosario del modulo

| Termino | Definicion |
|---------|------------|
| SI | Funcion que devuelve un valor u otro segun si se cumple una condicion |
| SI.CONJUNTO | Version mejorada de SI anidado que evalua multiples condiciones en orden |
| IFERROR | Captura cualquier error de una formula y devuelve un valor alternativo |
| BUSCARV | Busca un valor en la primera columna de una tabla y devuelve el de otra columna |
| BUSCARX | Version moderna de BUSCARV que permite buscar en cualquier direccion |
| COINCIDIR | Devuelve la posicion de un valor dentro de un rango |
| INDICE | Devuelve el valor de una celda en una posicion especifica de un rango |
| MEDIANA | Valor que divide la distribucion en dos mitades iguales |
| DESVEST | Desviacion tipica muestral — mide la dispersion de los datos |
| PERCENTIL | Valor por debajo del cual cae un porcentaje dado de los datos |
| COEF.DE.CORREL | Calcula el coeficiente de correlacion de Pearson entre dos rangos |

---

## Lo mas importante de este modulo

BUSCARV es la funcion que mas se usa en el trabajo real para conectar
tablas, pero tiene limitaciones importantes. Aprender INDICE+COINCIDIR
o BUSCARX desde el principio evita rehacer formulas cuando el dataset cambia.

La regla sobre errores: siempre envolver las busquedas en `IFERROR`
en informes que va a ver alguien. Un `#N/A` en medio de un dashboard
genera desconfianza aunque el resto del analisis sea correcto.
