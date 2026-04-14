import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = pd.read_csv(r'E:\courses\Data science\my\6\3\travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = DecisionTreeClassifier(random_state=12345)
model.fit(features_train, target_train)

predicted_valid = pd.Series(model.predict(features_valid))

class_frequency = predicted_valid.value_counts(normalize=True)

print(class_frequency)

class_frequency.plot(kind='bar')
plt.show()
