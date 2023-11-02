#obtener los elementos pares e impares de objeto Serie numerico

import pandas as pd

datos=list(range(1,21))
serie= pd.Series(datos)

serie_par=serie[serie%2==0]
serie_impar=serie[serie%2==1]
print("Serie par")
print(serie_par)
print("Serie impar")
print(serie_impar)