# Contar los valores repetidos en una serie

import pandas as pd

datos=[5,3,5,5,3,7,18,19,21,37,18]

serie= pd.Series(datos)

print(serie.value_counts())