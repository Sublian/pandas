#calcular minimo y maximo de un objeto Series

import pandas as pd

datos=[2,3,4,5,8,9,10,1,6,12,11,20,21,15,16, 2,3,6,7,1,22]

serie=pd.Series(datos)

print(serie)

print("maximo: ",serie.max())
print("minimo: ",serie.min())