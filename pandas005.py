#Aplicar las operaciones logico/relacionales sobre objetos Series

import pandas as pd

serie1=pd.Series([1,2,3,4,5,6])
serie2=pd.Series([7,8,9,4,11,12])

print(serie1>serie2)
print(serie1<serie2)
print(serie1==serie2)