#Obtener las columnas de un determinado tipo de dato con select_dtypes

import pandas as pd

datos ={'real': [3.1415],
        'entero': [37],
        'fecha':[pd.Timestamp('20170121')],
        'cadena': 'Hola Mundo'}

df = pd.DataFrame(datos)

print(df.select_dtypes(include='int64'))

print(df.select_dtypes(include='float64'))

#con varios elementos
print(df.select_dtypes(include=['int64','float64']))