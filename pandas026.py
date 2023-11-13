# Usar la funcion de agregacion agg de un objeto Serie

import pandas as pd

datos = [-8, 7, -6, 3, 21, 37,-40]

serie= pd.Series(datos)

print(f"Valor maximo de la serie: \n{serie.agg(max)}")
print(f"Valor minimo de la serie: \n{serie.agg(min)}")
print(f"Valores absolutos en la serie: \n{serie.agg(abs)}")

from math import sqrt

print(f"La raiz de cada elemento: \n{serie.agg(abs).agg(sqrt)}")

print(f"Representacion hex: \n{serie.agg(abs).agg(hex)}")

def cuadrado(x):
    return x*x

print(f"Valores cuadrados en la serie: \n{serie.agg(cuadrado)}")

print(f"Valores cubicos de la serie: \n{serie.agg(lambda x:x**3)}")

import numpy as np

print(f"Seno de los elementos en la serie: \n{serie.agg(np.sin)}")

print(f"Raiz Cubica de los elementos en la serie: \n{serie.agg(np.cbrt)}")

print(f"Suma de todos los elementos en la serie: \n{serie.agg(np.sum)}")