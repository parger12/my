import pandas as pd
metrica = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\9\metrica_data.csv')
age_avg = metrica['age'].mean()
print(age_avg)