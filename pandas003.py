#convertir un objeto Series a una Lista en python

import pandas as pd

datos =[2,3,5,7,9,10]
serie = pd.Series(datos)

print(datos)
print("Variable Datos: ",type(datos))
print(serie)
print("Variable Serie: ",type(serie))

#convertimos la Serie en Lista
lista= serie.tolist()
print(lista)
print("Variable Lista: ",type(lista))