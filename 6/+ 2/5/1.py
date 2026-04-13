import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = pd.read_csv(r'E:\courses\Data science\my\6\2\travel_insurance.csv')

encoder = OrdinalEncoder()
data_ordinal = pd.DataFrame(encoder.fit_transform(data),
                            columns=data.columns)

print(data_ordinal.head())
