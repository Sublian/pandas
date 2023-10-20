#Convertir un Diccionario en un objeto Series

import pandas as pd

datos={'a': 10, 'b': 20, 'c': 30, 'd': 5}
serie= pd.Series(datos)
print(serie)