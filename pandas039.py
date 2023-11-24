# calcular el producto punto entre dos Series

import pandas as pd

serie1 =pd.Series([2,3,5,7])
serie2 =pd.Series([1,2,2,3])

print(serie1,serie2)

print("El producto punto o escalar nos da: ",serie1.dot(serie2))