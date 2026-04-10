import pandas as pd
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r'E:\courses\Data science\my\5\5\4\train_data.csv')

features = df.drop(['last_price'], axis=1)
target = df['last_price']/1000000

print(target.mean())