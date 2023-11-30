# Obtener los tipos de datos de las comunas de un DataFrame

import pandas as pd

datos ={'real': [3.1415],
        'entero': [37],
        'fecha':[pd.Timestamp('20170121')],
        'cadena': 'Hola Mundo'}

df =pd.DataFrame(datos)

print(df)
print(df.dtypes)