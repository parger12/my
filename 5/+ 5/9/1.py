import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r'E:\courses\Data science\my\5\5\4\train_data.csv')

features = df.drop(['last_price'], axis=1)
target = df['last_price']/1000000

features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345) # отделите 25% данных для валидационной выборки

model = RandomForestRegressor(max_depth=10, random_state=12345, n_estimators=40)
model.fit(features_train, target_train) 
predictions_valid = model.predict(features_valid) 

result = mean_squared_error(target_valid, predictions_valid) ** 0.5
print("RMSE наилучшей модели на валидационной выборке:", result)