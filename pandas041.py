#Verificar con equals() si dos series contienen los mismo elementos

import pandas as pd

datos1 = [1,2,3,4,5]
datos2 = [1,2,3,4,5]

serie1=pd.Series(datos1)
serie2=pd.Series(datos2)

print(f"La serie1 es igual a la serie2: {serie1.equals(serie2)}")

datos3 = [6,8,9,10,0]
serie3=pd.Series(datos3)
print(f"La serie1 es igual a la serie3: {serie1.equals(serie3)}")

datos4 = [5,4,3,2,1]
serie4=pd.Series(datos4)
print(f"La serie1 es igual a la serie4: {serie1.equals(serie4)}")

