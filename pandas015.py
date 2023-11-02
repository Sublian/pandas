# cambiar el orden del indice de un objeto Series

import pandas as pd

datos = [0,2,4,6,8,10]
indices = ['A', 'B', 'C', 'D', 'E', 'F']

serie = pd.Series(data= datos, index=indices)

print(serie)

#cambiando el orden a un orden a voluntad o dictaminado 
serie=serie.reindex(index=['F','A', 'C', 'E', 'B','D'])

print(serie)