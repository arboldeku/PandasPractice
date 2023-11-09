import pandas as pd
import os
import numpy as np

ruta = "V:\\pandas\\"
excel = pd.read_excel(ruta + "Listados Excel.xlsx", sheet_name="Primer Semestre", header=0, usecols="A:E")

print("Estructura del dataframe...\n", excel.head())
tabla = pd.pivot_table(excel, index="Mes", columns="Comercial", values=["Unidades", "Ventas"],
                       aggfunc={"Unidades": lambda x: "%.2f" % np.mean(x), "Ventas": lambda x: "%.2f €" % np.sum(x)})
print("\nMostramos el promedio de unidades y la suma de ventas por mes y comercial:\n\n", tabla)

esBalsera = excel.loc[:,"Comercial"]=="Balsera"
esRius = excel.loc[:,"Comercial"]=="Rius"
esMarzo = excel.loc[:,"Mes"]=="marzo"
esAbril = excel.loc[:,"Mes"]=="abril"
seleccion = excel.loc[(esRius | esBalsera) & (esMarzo | esAbril)]
print("\nMostramos los resultados solo para abril y marzo, y los comerciales Balsera y rius:\n\n", pd.pivot_table(seleccion, index="Mes", columns="Comercial",
                                                                                                                  values=["Unidades", "Ventas"],
                                                                                                                  aggfunc={"Unidades": lambda x: "%.2f" % np.mean(x),
                                                                                                                           "Ventas": lambda x: "%.2f €" % np.sum(x)}))