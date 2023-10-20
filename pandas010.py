#Extraer una fila de un DataFrame como un objeto Series

import pandas as pd

datos={'A':[1,2,3,4,5], 'B':[9,8,7,6,5], 'C':[2,3,5,7,11]}

df= pd.DataFrame(data=datos)
print(df)

fila= df.iloc[2,:]
print(fila)
print(type(fila))