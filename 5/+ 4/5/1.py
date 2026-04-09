import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'E:\courses\Data science\my\5\+ 3\train_data.csv')
df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0

df_train, df_valid = train_test_split(df, test_size=0.25, random_state=12345)

features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class']

for depth in range(1,6):
    model = DecisionTreeClassifier(max_depth = depth, random_state = 12345)
    model.fit(features_train, target_train)
    predictions_valid = model.predict(features_valid)
    print("max_depth =", depth, ": ", end='')
    print(accuracy_score(target_valid, predictions_valid)) 

    
