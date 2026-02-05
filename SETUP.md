# Setup

Instrucciones para replicar los entornos de cada curso.

---

## Python (cursos 4, 5, 7, 8)

```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy matplotlib seaborn scipy scikit-learn plotly jupyter
```

## SQL (curso 6)

Los ejercicios usan **IBM Db2 on Cloud** (capa gratuita) o **SQLite** localmente.

Para SQLite:
```bash
pip install ipython-sql sqlite3
```

Para conectar Db2 desde Jupyter:
```bash
pip install ibm_db ibm_db_sa sqlalchemy
```

## Excel / Cognos (cursos 2, 3)

- Excel: Microsoft 365 o Google Sheets (compatible para la mayoria de ejercicios)
- IBM Cognos Analytics: acceso via trial gratuito en IBM Cloud

## Jupyter

```bash
pip install jupyter
jupyter notebook
```

---

## Estructura de carpetas

Cada curso tiene su propia carpeta con:
- `README.md` — resumen del curso y contenido del repo
- `apuntes.md` — notas detalladas por modulo
- subcarpetas con ejercicios practicos cuando aplica
