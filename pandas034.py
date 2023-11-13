#obtener la representacion de diccionario de un objeto Series

import pandas as pd

capitales =["Caracas","Lima", "Paris","Moscú", "Berlin", "Bogota"]

paises=["Venezuela", "Perú", "Francia", "Rusia", "Alemania", "Colombia"]

serie= pd.Series(capitales, index=paises)
print(serie)

#transforma una Serie a Dict
print(serie.to_dict())