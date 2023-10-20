#Crear y visualizar un arreglo unidimensional como una estructura Series

import pandas as pd

datos = [2, 3, 5, 6, 7,10]
serie = pd.Series(datos)

#mostrar datos de la serie
print(serie)

#mostrar el tamaño de la serie
print(serie.size)

#muestra datos relevantes a la informacion contenida en serie
print(serie.describe())
