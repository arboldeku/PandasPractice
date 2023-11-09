import pandas as pd
import os 

ruta = "V:\\pandas\\" #os.getcwd() + "\\"
lista = pd.read_csv(ruta + "Facturacion.csv", sep=";", keep_default_na=False,
                    parse_dates={"FECHA":["DD", "MM", "YY"]}, index_col="FECHA")
print("\nListado en CSV:\n", lista)
listaRedu = pd.read_csv(ruta + "Facturacion.csv", sep=";", usecols=[0,1,5], nrows=3)
print("\nSólo 3 columnas y 3 primeras filas:\n", listaRedu)

print("Creamos un archivo CSV nuevo")
listaRedu.to_csv(ruta + "Facturacion-Ejemplo.csv", sep=";", index=False)
print("Despues añadimos los mismos datos sin eliminarlo...")
listaRedu.to_csv(ruta + "Facturacion-Ejemplo.csv", sep=";", index=False, header=False, mode="a")
print("Creamos un archivo zip con el archivo csv...")
listaRedu.to_csv(ruta + "Facturacion-comprimido.zip", sep=";", index=False, 
                 compression=dict(method='zip', archive_name="Factur.csv"))