-- Modulo 4: SQL sobre los datos del capstone
-- Base de datos: survey.db (SQLite)
-- Ver modulo-5-python-sql/conexion_db.py para cargar el dataset en SQLite

-- ============================================================
-- EXPLORACION INICIAL
-- ============================================================

-- Numero total de respondentes
SELECT COUNT(*) AS total FROM survey;

-- Columnas del dataset (SQLite)
PRAGMA table_info(survey);

-- ============================================================
-- DEMOGRAFICOS
-- ============================================================

-- Top 10 paises por numero de respondentes
SELECT Country, COUNT(*) AS respondentes
FROM survey
WHERE Country IS NOT NULL
GROUP BY Country
ORDER BY respondentes DESC
LIMIT 10;

-- Distribucion por nivel educativo
SELECT EdLevel, COUNT(*) AS respondentes,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM survey), 1) AS porcentaje
FROM survey
WHERE EdLevel IS NOT NULL
GROUP BY EdLevel
ORDER BY respondentes DESC;

-- Experiencia media por pais (top 10 paises)
SELECT Country,
       COUNT(*) AS respondentes,
       AVG(CAST(YearsCodePro AS REAL)) AS experiencia_media
FROM survey
WHERE Country IS NOT NULL
  AND YearsCodePro NOT IN ('Less than 1 year', 'More than 50 years')
GROUP BY Country
HAVING COUNT(*) > 100
ORDER BY experiencia_media DESC
LIMIT 10;

-- ============================================================
-- COMPENSACION
-- ============================================================

-- Compensacion media y mediana por nivel educativo
SELECT EdLevel,
       COUNT(*) AS n,
       AVG(CompTotal) AS comp_media,
       MIN(CompTotal) AS comp_minima,
       MAX(CompTotal) AS comp_maxima
FROM survey
WHERE EdLevel IS NOT NULL
  AND CompTotal IS NOT NULL
  AND CompTotal > 0
  AND CompTotal < 500000  -- excluir valores extremos
GROUP BY EdLevel
ORDER BY comp_media DESC;

-- ============================================================
-- TECNOLOGIAS
-- ============================================================

-- Cuantos usan Python
SELECT COUNT(*) AS usan_python
FROM survey
WHERE LanguageHaveWorkedWith LIKE '%Python%';

-- Cuantos quieren aprender Rust
SELECT COUNT(*) AS quieren_rust
FROM survey
WHERE LanguageWantToWorkWith LIKE '%Rust%';

-- Cuantos usan Python Y quieren aprender Rust
SELECT COUNT(*) AS python_y_rust
FROM survey
WHERE LanguageHaveWorkedWith LIKE '%Python%'
  AND LanguageWantToWorkWith LIKE '%Rust%';

-- Cuantos usan JavaScript
SELECT COUNT(*) AS usan_js
FROM survey
WHERE LanguageHaveWorkedWith LIKE '%JavaScript%';

-- Bases de datos mas usadas (aproximacion con LIKE — no es perfecto)
-- La version completa requiere expandir la columna con Python
SELECT 'MySQL' AS database_nombre, COUNT(*) AS usuarios
FROM survey WHERE DatabaseHaveWorkedWith LIKE '%MySQL%'
UNION ALL
SELECT 'PostgreSQL', COUNT(*) FROM survey WHERE DatabaseHaveWorkedWith LIKE '%PostgreSQL%'
UNION ALL
SELECT 'SQLite', COUNT(*) FROM survey WHERE DatabaseHaveWorkedWith LIKE '%SQLite%'
UNION ALL
SELECT 'MongoDB', COUNT(*) FROM survey WHERE DatabaseHaveWorkedWith LIKE '%MongoDB%'
UNION ALL
SELECT 'Microsoft SQL Server', COUNT(*) FROM survey WHERE DatabaseHaveWorkedWith LIKE '%Microsoft SQL Server%'
UNION ALL
SELECT 'Redis', COUNT(*) FROM survey WHERE DatabaseHaveWorkedWith LIKE '%Redis%'
ORDER BY usuarios DESC;
