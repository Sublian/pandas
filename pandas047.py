# obtener los nombres de las filas y las columnas de un DataFrame

import pandas as pd

datos = {'x': [1,2,3,4,5],
         'y': [5,4,3,2,1],
         'z': [2,3,5,7,11]
         }

df = pd.DataFrame(datos)

#indices
print(df.index)

#columnas
print(df.columns)

indices = ['a','b','c','d','e']
df = pd.DataFrame(data=datos, index=indices)
print(df)

#indices
print(df.index)