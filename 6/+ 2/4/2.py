import pandas as pd

data = pd.read_csv(r'E:\courses\Data science\my\6\2\travel_insurance.csv')

data_ohe = pd.get_dummies(data, drop_first=True).astype(int)

print(data_ohe.head(3))