import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv(r'E:\courses\Data science\my\6\2\travel_insurance.csv')

data_ohe = pd.get_dummies(data, drop_first=True)

target = data_ohe['Claim']
features = data_ohe.drop('Claim', axis=1)

features_train, features_valid, target_train, target_valid = train_test_split(features, target, test_size=0.25, random_state=12345) 

model = LogisticRegression(random_state=12345)

print("Обучено!")
