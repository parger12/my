import pandas as pd

data = pd.read_csv(r'E:\courses\Data science\my\6\2\travel_insurance.csv')

print(pd.get_dummies(data['Gender'], dummy_na=True).head())
