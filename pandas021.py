# comprobar si una serie contiene valores Nan usando un enfoque de alto rendimiento

import pandas as pd

datos = ['20','30', 'Python', "40", 100]

serie = pd.Series(datos)

print(serie)

#esta funcion transforma los elementos presentes a tipo numerico, 
# reconoce los numeros en string y los transforma a numerico, 
# en caso de no poder coincidir se convierten en NaN
serie = pd.to_numeric(serie, errors='coerce')

print(serie)

print(f"Existen valores NaN en la serie: {serie.hasnans}")