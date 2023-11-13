#Calcular el valor absoluto de los elementos de un objeto Serie

import pandas as pd
datos = [-5, 3, 0, -7, -9, 21, 37, -2]

serie= pd.Series(datos)

print(f"Serie original \n{serie}")
print(f"Serie con valores Absolutos \n{serie.abs()}")