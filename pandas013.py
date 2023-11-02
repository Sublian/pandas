# Agregar datos a un objeto Series existente

import pandas as pd

datos =['Python', 'C#', 'Java', 'PHP','Kotlin']

serie = pd.Series(datos)

print(serie)

# se agregan mas elementos usando el agregado de listas
serie = serie.append(pd.Series(['Node','C++','Perl']))

print(serie)
