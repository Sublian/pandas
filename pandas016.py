#obtener la desviacion estandar y el promedio de un conjunto de datos de una serie

import pandas as pd

datos=[2,3,4,5,8,9,10,0,6,12,11,20,21,15,16]

serie= pd.Series(datos)

print(serie)

print("desviacion estandar: ",serie.std())
print("promedio: ",serie.mean())
print("maximo: ",serie.max())
print("minimo: ",serie.min())