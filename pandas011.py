#Convertir un objeto Series con multiples listas en un unico objeto Series 

import pandas as pd

#conjunto de datos en formato de lista
datos = [['Colombia', 'Perú', 'Argentina'], ['Bolivia', 'Uruguay'],['Venezuela']]

#se cambia a una serie
serie = pd.Series(datos)

print(serie)

#aplanamos la serie
serie = serie.apply(pd.Series).stack().reset_index(drop=True)

print(serie)