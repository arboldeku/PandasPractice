import sqlite3 as sql
import pandas as pd
import os

ruta = "V:\\pandas\\"
conex = sql.connect(ruta + "pandas_venta_semestre.sqlite")
datos = pd.read_excel(ruta + "Listados Excel.xlsx", sheet_name="Primer Semestre", header =0, usecols="A:E")
print("Obtencion de un DataFrame a partir de Excel realizado...")
datos.to_sql("ventas", con=conex, if_exists="replace", index_label="id")
print("Escritura del DataFrame a la tabla 'ventas' realizado...")

cursor = conex.cursor()
campos = cursor.execute("pragma table_info('ventas')")
print("\nLos campos de la tabla 'ventas' son:")
print("Orden".ljust(6), "Campo".ljust(12), "Tipo".ljust(12), 
      "Admite Null".ljust(12), "Por defecto".ljust(12), "Es clave primaria")
for campo in campos:
    print("{0}".format(campo[0]).ljust(6),
          "{0}".format(campo[1]).ljust(12),
          "{0}".format(campo[2]).ljust(12),
          "{0}".format(campo[3]).ljust(12),
          "{0}".format("Si" if campo [3]==1 else "No").ljust(12),
          "{0}".format(campo[4]).ljust(12),
          "Si" if campo[5]==1 else "No")