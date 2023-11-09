import sqlite3 as sql
import pandas as pd
import os

ruta = "V:\\pandas\\"
conex = sql.connect(ruta + "pandas_venta_semestre.sqlite")

datos = pd.read_sql("SELECT * FROM ventas WHERE Mes='enero' and Ventas>9000", con=conex, index_col="id", parse_dates="Fecha")
print("DataFrame resultante de la lectura con sql:\n\n", datos)