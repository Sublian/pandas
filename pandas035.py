#Crear objeto DataFrame a partir de un objeto Series

import pandas as pd

datos = [2,3,7,9,12,5]

serie= pd.Series(datos)
print(serie)

df= serie.to_frame()
print(df)
print(type(df))
