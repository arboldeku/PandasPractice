import pandas as pd
import os

ruta = "V:\\pandas\\"
excel = pd.read_excel(ruta + "Listados Excel.xlsx", sheet_name="Automocion", header=0)
print("Estructura del DataFrame...\n", excel.head())
fabric = ["mazda", "toyota", "honda", "nissan", "mitshubishi", "volkswagen"]
listado = excel[excel.fabricante.isin(fabric)]
print("\nCantidad de modelos por fabricante y carroceria...\n\n", 
      pd.crosstab(index=listado.fabricante, columns=listado.carroceria))
print("\nLa versión con pivot table es similar...\n", listado.pivot_table(index="fabricante", 
        columns="carroceria", aggfunc={"carroceria":len}, fill_value=0))
print("\n\nIncluimos totales...\n", pd.crosstab(index=listado.fabricante, columns=listado.puertas, 
        margins=True, margins_name="Suma Total"))
print("\nCalculamos el promedio del peso en vacio por fabricante y carroceria...\n",
      pd.crosstab(index=listado.fabricante, columns=listado.carroceria, 
                  values=listado.peso_vacio, aggfunc="mean", normalize="columns").round(2))

