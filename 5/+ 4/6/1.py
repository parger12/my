import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'E:\courses\Data science\my\5\+ 3\train_data.csv')
df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0

df_train, df_valid = train_test_split(df, test_size = 0.25, random_state=12345) 

features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class']

best_model = None
best_result = 0
for est in range(1, 11):
    model = RandomForestClassifier(random_state=12345, n_estimators= est )
    model.fit(features_train, target_train)
    result = model.score(features_valid, target_valid)
    if result > best_result:
        best_model = model
        best_result = result

print("Accuracy наилучшей модели на валидационной выборке:", best_result)
