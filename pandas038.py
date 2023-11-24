#Encontrar los elementos que estan dentro de un rango

import pandas as pd
import numpy as np

datos = [7,2,3,5,0,np.nan,21,37,42,23]

serie= pd.Series(datos)

print(serie.between(5,21))

#equivalencia
print((5<= serie) & (serie <=21))

print(serie.between(5,21, inclusive= False))
#cambio, inclusive= False esta obsoleto ahora se usan "neither": para ninguno o "both": para ambos como argumento opcional
#neither -> no incluye los limites o extremos
#both    -> si incluye los limites o  extremos
print(serie.between(5,21, "neither"))
print(serie.between(5,21, "both"))

#tambien se puede evaluar caracteres

nombres =["Luis", "Dayana", "Fabiana", "Javier","Ana"]
serie_nombre = pd.Series(nombres)

print(serie_nombre.between("Ana", "Fabiana"))