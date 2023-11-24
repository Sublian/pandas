#Usar un grafico de barras para presentar la produccion de trigo en un pais X

import pandas as pd
import matplotlib.pyplot as plt

produccion = {2015: 1000, 2016: 1100, 2017: 900, 2018: 850, 2019: 950, 2020: 1100, 2021: 1300, 2022: 1050, 2023: 1650, 2024: 1450}
serie = pd.Series(produccion)

print(serie)
# Crear la gráfica
print(serie.plot(kind='bar'))
# Agregar un título a la gráfica
plt.title('Producción por año')
# Mostrar la gráfica
plt.show()

# Crear barras de error
errores = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

# Graficar con barras de error
plt.title('Producción por año/error')
plt.bar(serie.index, serie.values, yerr=errores, capsize=5)
plt.show()