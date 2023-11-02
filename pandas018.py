#obtener estadisticas basicas de un objeto series usando describe

import pandas as pd

datos=list(range(1,21))

print(datos)

serie= pd.Series(datos)

print(serie)
print(serie.describe())