#Eliminar valores NaN de una serie con el metodo dropna

import pandas as pd
import numpy as np

datos= [3.14, 'Python', 21, '37', np.nan, '0.5', '.9']

serie=pd.Series(datos)
serie= pd.to_numeric(serie, errors= 'coerce')

print("Serie con valores NaN")
print(serie)

serie =serie.dropna()
print("Serie sin valores NaN")
print(serie)
