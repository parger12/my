import pandas as pd
data = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\4\logs.csv')
visits = data.groupby('source')['user_id'].count()
visits2 = data['source'].value_counts()
purchase = data.groupby('source')['purchase'].sum()
print(purchase)