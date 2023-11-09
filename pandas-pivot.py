import pandas as pd
alumnos = pd.DataFrame({"Alumno": ["Gonzalo", "Irene", "Oscar", "Gonzalo"], "Titulo": ["Master", "Superior", "Superior", "Master"],
                        "Creditos": [27, 24, 22, 20]})
print("Dataframe original:\n", alumnos)
#print("\nTabla dinamica (pivot):\n\n", alumnos.pivot(index="Alumno", columns="Titulo", values="Creditos"))
print("\nTabla dinamica (pivot_table):\n\n", alumnos.pivot_table(index="Alumno", columns="Titulo", values="Creditos",
                                                                 fill_value="", margins=True, aggfunc="sum"))