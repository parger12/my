import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# обучающая выборка находится в файле train_data.csv
df = pd.read_csv(r'E:\courses\Data science\my\5\3\train_data.csv')

df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0

features = df.drop(['last_price', 'price_class'], axis=1)
target = df['price_class']

model = DecisionTreeClassifier(random_state=12345)

model.fit(features, target)

test_df = pd.read_csv(r'E:\courses\Data science\my\5\3\test_data.csv')

test_df = test_df.drop('Unnamed: 0', axis=1)



test_df.loc[test_df['last_price'] > 5650000, 'price_class'] = 1
test_df.loc[test_df['last_price'] <= 5650000, 'price_class'] = 0

test_features = test_df.drop(['last_price', 'price_class'], axis=1)
test_target = test_df['price_class']

test_predictions = model.predict(test_features)

def error_count(answers, predictions):
    counter = 0
    for i in range(len(answers)):
        if answers.iloc[i] != predictions[i]:
            counter += 1
    return counter
            


print("Ошибок:", error_count(test_target, test_predictions))

