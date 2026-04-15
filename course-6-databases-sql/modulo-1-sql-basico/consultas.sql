-- Modulo 1: SQL Basico — DDL y DML

-- ============================================================
-- CREAR TABLAS
-- ============================================================

CREATE TABLE departamentos (
    id_dept  INT PRIMARY KEY NOT NULL,
    nombre   VARCHAR(50) NOT NULL,
    ciudad   VARCHAR(50)
);

CREATE TABLE empleados (
    id           INT PRIMARY KEY NOT NULL,
    nombre       VARCHAR(50) NOT NULL,
    apellido     VARCHAR(50),
    id_dept      INT REFERENCES departamentos(id_dept),
    salario      DECIMAL(10, 2),
    fecha_alta   DATE
);

-- ============================================================
-- INSERTAR DATOS
-- ============================================================

INSERT INTO departamentos VALUES
    (1, 'IT', 'Barcelona'),
    (2, 'Marketing', 'Madrid'),
    (3, 'Finanzas', 'Barcelona'),
    (4, 'Datos', 'Barcelona');

INSERT INTO empleados VALUES
    (1, 'Ana', 'Garcia', 1, 38000.00, '2021-03-15'),
    (2, 'Luis', 'Martinez', 2, 32000.00, '2022-01-10'),
    (3, 'Marta', 'Lopez', 1, 42000.00, '2020-09-01'),
    (4, 'Carlos', 'Ruiz', 4, 45000.00, '2019-06-20'),
    (5, 'Sara', 'Gomez', 3, 36000.00, '2023-02-28'),
    (6, 'Pedro', 'Sanchez', 2, 29000.00, '2022-11-15');

-- ============================================================
-- SELECT BASICO
-- ============================================================

-- Todo
SELECT * FROM empleados;

-- Columnas especificas con alias
SELECT nombre, apellido, salario AS salario_anual
FROM empleados;

-- Valores distintos
SELECT DISTINCT id_dept FROM empleados;

-- Ordenar
SELECT nombre, salario
FROM empleados
ORDER BY salario DESC;

-- Limitar
SELECT * FROM empleados
FETCH FIRST 3 ROWS ONLY;

-- ============================================================
-- WHERE — FILTROS
-- ============================================================

-- Comparacion
SELECT * FROM empleados WHERE salario > 35000;

-- Entre dos valores
SELECT * FROM empleados
WHERE salario BETWEEN 30000 AND 40000;

-- Lista de valores
SELECT * FROM empleados
WHERE id_dept IN (1, 4);

-- Patron de texto
SELECT * FROM empleados
WHERE nombre LIKE 'A%';

-- Nulos
SELECT * FROM empleados
WHERE apellido IS NOT NULL;

-- Combinacion de condiciones
SELECT nombre, salario
FROM empleados
WHERE id_dept = 1 AND salario > 38000;

-- ============================================================
-- UPDATE Y DELETE
-- ============================================================

-- Actualizar salario
UPDATE empleados
SET salario = 40000.00
WHERE id = 1;

-- Actualizar departamento
UPDATE empleados
SET id_dept = 4
WHERE nombre = 'Ana';

-- Eliminar un registro
DELETE FROM empleados WHERE id = 6;
