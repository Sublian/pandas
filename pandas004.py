#Aplicar las operaciones aritmeticas basicas sobre objetos Series

import pandas as pd

serie1=pd.Series([1,2,3,4,5,6])
serie2=pd.Series([7,8,9,10,11,12])

#sumatoria
print(serie1+serie2)

#resta
print(serie1-serie2)

#multiplicacion
print(serie1*serie2)

#division
print(serie1/serie2)