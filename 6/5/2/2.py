import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(r'E:\courses\Data science\my\6\5\flights.csv')

data_ohe = pd.get_dummies(data)
target = data_ohe['Arrival Delay']
features = data_ohe.drop(['Arrival Delay'], axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345
)

numeric = ['Day', 'Day Of Week', 'Origin Airport Delay Rate',
           'Destination Airport Delay Rate', 'Scheduled Time', 'Distance',
           'Scheduled Departure Hour', 'Scheduled Departure Minute']

scaler = StandardScaler()
scaler.fit(features_train[numeric])
features_train[numeric] = scaler.transform(features_train[numeric])
features_valid[numeric] = scaler.transform(features_valid[numeric])

print(features_train.shape)
print(features_valid.shape)
