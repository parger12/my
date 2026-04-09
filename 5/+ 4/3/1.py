import pandas as pd
from sklearn.model_selection import train_test_split 

df = pd.read_csv(r'E:\courses\Data science\my\5\+ 3\train_data.csv')

df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0

df_train, df_valid = train_test_split(df, test_size= 0.25, random_state = 12345)


features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class']

print(features_train.shape)
print(target_train.shape)
print(features_valid.shape)
print(target_valid.shape)