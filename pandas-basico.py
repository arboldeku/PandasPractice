import pandas as pd

listado = [30.47, 25.82, 8.15, 12.95, 44.34]
etiquetas = ["Artic 1", "Artic 2", "Artic 3", "Artic 4", "Artic 5"]
serie = pd.Series(listado, etiquetas)

capitales = {"Italia":"Roma", "Portugal":"Lisboa", "Polonia":"Varsovia"}
serieDict = pd.Series(capitales)
print(serie, "\nSerie a partir de diccionario:")
print(serieDict)
print("\nLos arrays multidimensionales no se reconocen como tales:")
multi = [[1, 2, 3], [4, 5, 6], [7, 8,9]]
serieMulti = pd.Series(multi)
print(serieMulti)

print("\n---Algunos atributos interesantes de las series pandas---\n")
print("Extensiones sobre una serie:\n", serie.array)
print("El valor del segundo articulo es:", serie.at["Artic 2"],
      "y del tercero: ", serie.iat[2])
print("Los elementos primero, tercero y cuarto de la serie son:\n"
      , serie.iloc[[True, False, True, True, False]])
print("La serie consta de", serie.size, "elementos. Dimensiones:",
      serie.ndim)

print("\n--Algunos metodos interesantes de las series pandas--\n")
enero = [-35.34, 82.75, 20.57, -22.42, 82.75]
febrero = [22.45, None, 45.95, 15.83, None]
precios = pd.Series(enero)
print("Serie Original:\n", precios)
print("Serie en valores absolutos:\n", precios.abs())
print("Serie incrementada un 2%:\n", precios.apply(lambda x:x*1.02))
print("Series sumadas:\n", precios.add(febrero))
print("Series sumadas, estableciendo en 0 los valores nulos:\n", precios.add(febrero, fill_value=0))
print("Añadiendo un prefijo en el eje:\n", precios.add_prefix("precio "))
print("Mostramos los 2 primeros valores:\n", precios.value_counts())
porcentajes = precios.value_counts(normalize=True)*100
print("Mostramos el recuento en porcentajes:\n", porcentajes.transform(lambda x:str(x)+"%"))
preciosFeb = pd.Series(febrero, etiquetas)
print("Esta es la serie original:\n", preciosFeb)
print("Eliminamos los valores no vàlidos:\n", preciosFeb.dropna())
print("Cambiamos dos valores y tambien los nulos por otros:\n", preciosFeb.replace({22.45: 300, 15.83: 20.95, None: 0}))
