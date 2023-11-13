#representacion JSON de un objeto Series

import pandas as pd

serie =pd.Series(range(6))

print(serie)

#transforma el objeto a formato JSON
print(serie.to_json())