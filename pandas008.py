#Cambiar el tipo de datos de un objeto Series

import pandas as pd

#cuando existen tipos de datos que no sean numeros lo suele tratar como un tipo de dato "objeto"
datos=pd.Series(['100','200','300','Python','400.20','508','Sublian'])
print(datos)

#cuando existen valores que no sean numericos por defecto se pasaran a NaN o Non a Numeric
datos= pd.to_numeric(datos, errors='coerce')
print(datos)