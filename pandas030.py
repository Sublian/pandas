#Reemplazar por un valor arbitrario los valores de una serie que no satisfagan una condicion

import pandas as pd

datos = list(range(9))

serie=pd.Series(datos)

print(serie)

print(serie.where(serie>1))

print(serie.where(serie>1,-1))