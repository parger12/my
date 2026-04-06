import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(r'E:\courses\Data science\my\5\3\train_data.csv')

df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0

features = df.drop(['last_price', 'price_class'], axis=1)
target = df['price_class']

best_model = None
best_result = 0

for depth in range(1, 6):
    model = DecisionTreeClassifier(random_state=12345, max_depth=depth)
    model.fit(features, target)
    predictions = model.predict(features)
    result = accuracy_score(target, predictions) 
    if result > best_result:
        best_model = model
        best_result = result
        
print("Accuracy лучшей модели:", best_result)