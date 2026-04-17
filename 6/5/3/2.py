import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv(r'E:\courses\Data science\my\6\5\flights_preprocessed.csv')

target = data['Arrival Delay']
features = data.drop(['Arrival Delay'] , axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = LinearRegression()
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)
mse = mean_squared_error(target_valid, predicted_valid)

print("Linear Regression")
print("MSE =", mse)
print("RMSE =", mse ** 0.5)

predicted_valid = pd.Series(target_train.mean(), index=target_valid.index)
mse = mean_squared_error(target_valid, predicted_valid)

print("Mean")
print("MSE =", mse)
print("RMSE =", mse ** 0.5)