# extraer los datos de un objeto Series como un objeto NumPy

import pandas as pd

datos = list(range(20))

serie =pd.Series(datos)
print(serie, type(serie))

arreglo=serie.values
print(arreglo, type(arreglo))