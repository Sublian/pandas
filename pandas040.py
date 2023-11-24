#Remover valores duplicados de un objeto Series usando la funcion o metodo drop_duplicates

import pandas as pd

datos =["Python", "C#", "Python", "C++", "Java", "Python", "Assembler", "JavaScript","PHP", "Java"]

serie= pd.Series(datos, name="lenguajes")

print(serie)

#elimina todos los duplicados
print(serie.drop_duplicates())

#elimina  duplicados, pero mantiene el ultimo que aparece
print(serie.drop_duplicates(keep="last"))