import pandas as pd
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = pd.read_csv(r'E:\courses\Data science\my\6\3\travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)

target_pred_constant = pd.Series(0, index = target.index)
accuracy = accuracy_score(target, target_pred_constant)

print(accuracy)
