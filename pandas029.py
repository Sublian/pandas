# consigamos el ultimo y primer elemento de un objeto Series

import pandas as pd

datos=list(range(1,101))
serie=pd.Series(datos)

print(serie)

print(f"Primeros 5 elementos: \n{serie.head()}")
print(f"Ultimos 10 elementos: \n{serie.tail(10)}")