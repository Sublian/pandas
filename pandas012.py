# Ordenar los valores de un objetivo Series con el metodo sort_values

import pandas as pd

datos =['1.1', 'Python', '0.5', 'Pandas', '2.8']

serie= pd.Series(datos)

print(serie)

#la ordenacion es en base a los valores numericos y luego los de tipo strings
serie=pd.Series(serie).sort_values()

print(serie)
