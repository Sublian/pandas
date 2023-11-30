# obtener las primeras n filas de un objeto DataFrame

import pandas as pd
import numpy as np

nombre = ['Olivia', 'Daniela', 'Juan', 'German', 'Edward', 'Alex', 'Julio', 'Edgard', 'Angie', 'Irlesa']
puntaje = [11.5, 8, 15.55, np.nan, 8, 19, 13.56, np.nan, 8, 18]
intentos = [1,3,2,3,2,3,1,1,2,1]
califico= ['SI', 'NO', 'SI', 'NO', 'NO', 'SI', 'SI', 'NO', 'NO', 'SI']
indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

jugadores ={'nombre': nombre,
            'puntaje': puntaje,
            'intentos': intentos,
            'califico':califico}

df= pd.DataFrame(data= jugadores, index= indices)
print(df)

print('*'*15)
#imprime las primeras 3
print(df.iloc[:3])

print('*'*15)
#imprime las ultimas 3
print(df.iloc[-3:])