# Usar operadores relacionales con metodos de la clase Series

import pandas as pd

datos1= list(range(10))
datos2= list(range(-5,15,2))

print(datos1)
print(datos2)

serie1= pd.Series(datos1)
serie2= pd.Series(datos2)

#less than // menor que
print(serie1.lt(serie2))

#less equals // menor e igual
print(serie1.le(serie2))

#equals //igual
print(serie1.eq(serie2))

#great than // mayor que
print(serie1==serie2)

#great equals // mayor e igual
print(serie1.gt(serie2))

print(serie1.ge(serie2))