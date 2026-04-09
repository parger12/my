import pandas as pd
from joblib import dump
from sklearn.linear_model import LogisticRegression 

df_train = pd.read_csv(r'E:\courses\Data science\my\5\+ 3\train_data.csv')
df_train.loc[df_train['last_price'] > 5650000, 'price_class'] = 1
df_train.loc[df_train['last_price'] <= 5650000, 'price_class'] = 0

features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']

model = LogisticRegression(max_iter=50000, random_state=12345)
model.fit(features_train, target_train)

print(dump(model, 'model_9_1.joblib'))
print(model)
