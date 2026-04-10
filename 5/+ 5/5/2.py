import pandas as pd
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r'E:\courses\Data science\my\5\5\4\train_data.csv')

features = df.drop(['last_price'], axis=1)
target = df['last_price'] / 1000000

mean_price = target.mean()
predictions = [mean_price] * len(target)
mse = mean_squared_error(target, predictions)
mse = mse ** 0.5

print("MSE:", mse)