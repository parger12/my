import pandas as pd
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv (r'E:\courses\Data science\my\5\2\train_data.csv')
df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0
features = df[['total_area', 'rooms', 'ceiling_height', 'living_area',
               'studio', 'open_plan', 'kitchen_area', 'balcony',
                'airports_nearest', 'cityCenters_nearest']]
target = df['price_class']
model = DecisionTreeClassifier()
model.fit(features, target)
new_features = pd.DataFrame([
    [900, 12, 2.8, 409.7, 0, 0, 112, 0, 30706.0, 7877.0],
    [109, 2, 2.8, 32, 0, 0, 40.5, 0, 36421.0, 9176.0]
], columns=['total_area', 'rooms', 'ceiling_height', 'living_area',
            'studio', 'open_plan', 'kitchen_area', 'balcony',
            'airports_nearest', 'cityCenters_nearest'])

answers = model.predict(new_features)
from sklearn.tree import export_text

print(export_text(model, feature_names=list(features.columns)))



