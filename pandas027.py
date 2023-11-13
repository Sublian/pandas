#Reemplazar los valores NaN (null) de una serie con un valor arbitrario

import pandas as pd
import numpy as np

datos=[1,3,7,9,11,21,37,'Python',0.5,-80, np.nan]

serie =pd.Series(datos)

serie=pd.to_numeric(serie, errors='coerce')
print(serie)

#cambiar valores NaN a 0
serie.fillna(0, inplace=True)
print(serie)