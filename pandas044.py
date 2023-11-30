# usar la funcion filter para extrare los elementos por su indice

import pandas as pd

produccion = {'Enero': 1000, 'Febrero': 1100, 'Marzo': 900, 'Abril': 850, 'Mayo': 950, 'Junio': 1100, 'Julio': 1300, 'Agosto': 1050, 'Septiembre': 1650, 'Octubre': 1450}

serie= pd.Series(produccion)

print(serie)

print(serie.filter(items= ["Enero", "Marzo", "Mayo", "Julio"]))

#expresiones regulares
print("*"*10)
print(serie.filter(regex="^M"))

#parecido
print("/"*10)
print(serie.filter(like="yo"))