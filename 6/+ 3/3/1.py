import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'E:\courses\Data science\my\6\3\travel_insurance_preprocessed.csv')

class_frequency = data['Claim'].value_counts(normalize=True)
print(class_frequency)
class_frequency.plot(kind='bar')
plt.show()