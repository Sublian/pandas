#Operaciones aritmeticas con metodos de las clases Serie; add, sustact, multiply y divide

import pandas as pd

serie1= pd.Series(list(range(1,21)))
print (serie1)

serie2= pd.Series(list(range(20,0,-1)))
print(serie2)

print("Suma \n" ,serie1.add(serie2))
print("Resta \n" ,serie1.subtract(serie2))
print("Multiplicacion \n" ,serie1.multiply(serie2))
print("Division \n" ,serie1.divide(serie2))