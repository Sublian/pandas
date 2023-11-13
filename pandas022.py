#Obtener el tamaño en bytes del espacio ocupado por los elementos de un objeto Series

import pandas as pd

datos = list(range(21))

serie = pd.Series(datos)

#funcion que nos retorna el tamaño en bytes
print("Total tamaño del registro Serie: ", serie.nbytes)
print("Tamaño por cada registro de la Serie: ", serie.nbytes/len(serie))