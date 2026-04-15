-- Modulo 3: Funciones de Agregacion y Funciones de Ventana

-- ============================================================
-- FUNCIONES DE AGREGACION BASICAS
-- ============================================================

SELECT
    COUNT(*) AS total_empleados,
    COUNT(apellido) AS con_apellido,
    SUM(salario) AS masa_salarial,
    AVG(salario) AS salario_medio,
    MIN(salario) AS salario_minimo,
    MAX(salario) AS salario_maximo
FROM empleados;

-- ============================================================
-- GROUP BY
-- ============================================================

-- Estadisticas por departamento
SELECT id_dept,
       COUNT(*) AS empleados,
       AVG(salario) AS media,
       MAX(salario) AS maximo
FROM empleados
GROUP BY id_dept
ORDER BY media DESC;

-- ============================================================
-- HAVING — filtrar sobre grupos
-- ============================================================

-- Solo departamentos con mas de 1 empleado
SELECT id_dept, COUNT(*) AS empleados
FROM empleados
GROUP BY id_dept
HAVING COUNT(*) > 1;

-- Departamentos con salario medio mayor de 38000
SELECT id_dept, AVG(salario) AS media
FROM empleados
GROUP BY id_dept
HAVING AVG(salario) > 38000;

-- ============================================================
-- FUNCIONES DE VENTANA
-- ============================================================

-- ROW_NUMBER: ranking de salario dentro de cada departamento
SELECT
    nombre,
    id_dept,
    salario,
    ROW_NUMBER() OVER (
        PARTITION BY id_dept
        ORDER BY salario DESC
    ) AS ranking_en_dept
FROM empleados;

-- RANK: igual que ROW_NUMBER pero empates comparten numero
SELECT
    nombre,
    salario,
    RANK() OVER (ORDER BY salario DESC) AS ranking_global
FROM empleados;

-- Acumulado de masa salarial por fecha de alta
SELECT
    nombre,
    fecha_alta,
    salario,
    SUM(salario) OVER (
        ORDER BY fecha_alta
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS masa_salarial_acumulada
FROM empleados;

-- LAG: diferencia de salario respecto al empleado anterior (ordenado por fecha)
SELECT
    nombre,
    fecha_alta,
    salario,
    LAG(salario) OVER (ORDER BY fecha_alta) AS salario_anterior,
    salario - LAG(salario) OVER (ORDER BY fecha_alta) AS diferencia
FROM empleados;
