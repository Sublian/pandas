# Expecificar nombres de indices arbitrarios a un objetivo DataFrame

import pandas as pd

datos = {'x': [1,2,3,4,5],
         'y': [5,4,3,2,1],
         'z': [2,3,5,7,11]
         }

df = pd.DataFrame(datos)

print(df)

print('*'*15)
indices = ['a','b','c','d','e']

df = pd.DataFrame(data= datos, index=indices)
print(df)

print('*'*15)

print(df.loc['c'])
print(type(df.loc['c']))