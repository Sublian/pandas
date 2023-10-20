#Convertir un arreglo Numpy en un objeto Series

import pandas as pd
import numpy as np

arreglo= np.array([2,3,5,7,11,15,21])
print("Objeto Numpy:",arreglo)

serie=pd.Series(arreglo)
print("Objeto Serie:",serie)
