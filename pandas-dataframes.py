import pandas as pd
import numpy as np

columnas = ["Nombre", "Edad", "Genero", "Saldo"]
listado = np.array([["Carmen", 21, "M", 1743], ["Pedro", 32, "H", 9264], ["Maria", 28, "M", 8362], ["Julio", 24, "H", 2537]])

datos = pd.DataFrame(listado, columns=columnas)
print("Formamos un DataFrame con un array de Numpy:")
print(datos)

LocalizaHombres = datos.loc[:, "Genero"] == "H"
print("Los hombres localizados son los True de estas filas:\n", LocalizaHombres)
print("Con ello podemos obtener sus datos:")
print(datos.loc[LocalizaHombres])

print("Los tipos de datos en principio son todos object:\n", datos.dtypes)
datos = datos.astype({"Edad": "int32", "Saldo": "float64"})
print("Establecemos los numeros como numericos para hacer las operaciones aritmeticas:\n", datos.dtypes)
print("Por ejemplo, mostramos las personas mayores de 25 años")
print(datos.loc[datos["Edad"]>=25])
print("\nPodemos establecer un agrupamiento y realizar un calculo,", "por ejemplo el maximo por generos:\n")
print(datos.groupby("Genero").max())
print("\nSi el agrupamiento incluye una operacion con el grupo, solo veremos", "los valores numericos, por ejemplo los promedios:\n")
print(datos.groupby("Genero").median())
