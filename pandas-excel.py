import pandas as pd
import os

ruta = "v:\\"  #os.getcwd() + "\\Documents\\"
excel = pd.read_excel(ruta + "Listados Excel.xlsx", sheet_name="Primer Semestre", header=0, usecols="A:E")

excel.info()

print("\nLectura realizada. 2 primeras ventas:")
print(excel.head(2))
print("\n2 últimas ventas:")
print(excel.tail(2))
print("\nLas ventas sólo del comercial Valsera:")
print(excel[excel["Comercial"]=="Balsera"])

print("\nMostramos la suma de ventas agrupadas por comercial y mes:")
print(excel[["Comercial", "Ventas", "Mes"]].groupby(["Comercial", "Mes"], sort=False).sum())

writer= pd.ExcelWriter(ruta + "Listados Excel.xlsx", mode="a", engine="openpyxl")
nombre = ""
while nombre != "salir":
    nombre = input("\nIndique el comercial ('salir' para finalizar):\n")
    seleccion = excel[excel["Comercial"]==nombre]
    if seleccion.size == 0:
        if nombre != "salir":
            print("Este comercial no se ha encontrado")
    else:
        grupo = seleccion[["Comercial", "Mes", "Ventas"]].groupby(["Comercial", "Mes"], sort=False)
        totalesComercial = pd.concat([grupo.sum(), grupo.max(), grupo.min()], axis=1, keys=["Suma", "Maximo", "Minimo"])
        print(totalesComercial)
        totalesComercial.to_excel(writer, "Totales " + nombre, startrow=2, startcol=3)
writer.save()
