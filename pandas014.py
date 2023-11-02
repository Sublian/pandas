# crear un objeto Series a partir de un filtro aplicado a otro objeto Series utilizando expresiones booleanas

import pandas as pd

datos = [0,1,2,3,4,5,6,7,8,9]

serie = pd.Series(datos)

print(serie)

FILTER = 6

serie_nueva =serie[serie<FILTER]

print(serie_nueva)