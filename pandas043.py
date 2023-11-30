# Guardar datos de un objeto Series  en un archivo Excel 

import pandas as pd


produccion = {'Enero': 1000, 'Febrero': 1100, 'Marzo': 900, 'Abril': 850, 'Mayo': 950, 'Junio': 1100, 'Julio': 1300, 'Agosto': 1050, 'Septiembre': 1650, 'Octubre': 1450}

serie = pd.Series(produccion)

serie.to_excel("produccion.xlsx")
"""
#en caso de convertir un dictionary  a excel
dct = {'ID': {0: 23, 1: 43, 2: 12, 
              3: 13, 4: 67, 5: 89, 
              6: 90, 7: 56, 8: 34}, 
      'Name': {0: 'Ram', 1: 'Deep', 
               2: 'Yash', 3: 'Aman', 
               4: 'Arjun', 5: 'Aditya', 
               6: 'Divya', 7: 'Chalsea', 
               8: 'Akash' }, 
      'Marks': {0: 89, 1: 97, 2: 45, 3: 78, 
                4: 56, 5: 76, 6: 100, 7: 87, 
                8: 81}, 
      'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C', 
                4: 'E', 5: 'C', 6: 'A', 7: 'B', 
                8: 'B'} 
    } 
  
# forming dataframe
data = pd.DataFrame(dct) 
  
# storing into the excel file
data.to_excel("output.xlsx")
"""