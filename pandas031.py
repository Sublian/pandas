# Remover los valores que no cumplan con un objeto Series

import pandas as pd

datos = list(range(1,37,2))

serie = pd.Series(datos)

#muestra los elementos NaN
print(serie.where(serie>=7))

#elimina los elementos NaN
print(serie.where(serie>=7).dropna())