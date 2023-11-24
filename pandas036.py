#Convertir contenido Series en formato CSV (Comma Separated Values)

import pandas as pd

datos=["Python", "JavaScript", "PHP", "C++", "SQL"]

serie =pd.Series(datos)

#genera la conversion de formato
print(serie.to_csv())

#genera la conversion de formato sin indice
print(serie.to_csv(index=False))