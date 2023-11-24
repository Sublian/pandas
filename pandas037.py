#Aplicar una funcion sobre los elementos de un objeto Series

import pandas as pd

serie=pd.Series([22,18,17], index=["Pitalito", "Isnos", "San Agustin"])

print(serie)
#via funcion
def cuadrado(x):
    return x* x

print(serie.apply(cuadrado))

#usando lambda
print(serie.apply(lambda x: x*x))

def adicionar_temperatura(x, delta):
    return x+delta

print(serie.apply(adicionar_temperatura, args=(7,))) 
