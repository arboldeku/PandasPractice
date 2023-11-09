import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import os

ruta = "V:\\pandas\\"
conex = sql.connect(ruta + "pandas_venta_semestre.sqlite")
grafico = pd.read_sql("SELECT SUM(Ventas) AS Totales, Comercial From ventas WHERE Mes='enero' AND Ventas>9000 GROUP BY Comercial", con=conex)
print("Los datos que emplea el grafico son:\n", grafico)
plt.bar(grafico.Comercial, grafico.Totales, color="cyan")
plt.title("Totales de ventas Enero (matplotlib)")
grafico.plot("Comercial", "Totales", kind="barh", color="red")
plt.title("Totales de ventas Enero (pandas)")
plt.show()