#Obtener una columna de un objeto DataFrame como un objeto Series

import pandas as pd

datos={'A':[1,2,3,4,5], 'B':[9,8,7,6,5], 'C':[2,3,5,7,11]}

df=pd.DataFrame(data=datos)

print(df)
print(type(df))

#se puede usar iloc: para posiciones indexadas o loc: para indices en base a etiquetas
columna= df.iloc[:,1]
print(columna)