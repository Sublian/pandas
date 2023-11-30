# mostrar un reporte con la informacion basica de un objet DataFrame

import pandas as pd

lenguajes =['Python', 'Java', ' C#', 'JavaScript', 'C++', 'PHP']
agnio_creacion =[1990, 1995, 2013, 1995, 1985, 1995]
interpretado=[True, False, False,  True, False, True]
extension = ['py', 'java', 'cs', 'js', 'cpp', 'php']

indices =['a', 'b', 'c', 'd', 'e', 'f']

datos= {'lenguaje': lenguajes,
        'agnio_creacion': agnio_creacion,
        'interpretado': interpretado,
        'extension': extension
       } 

df = pd.DataFrame(data=datos, index=indices)
print(df)

print(df.info())