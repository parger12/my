import pandas as pd
logs = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\8\logs1.csv')
logs ['email'] = logs ['email'].fillna(value='')
logs.loc[logs['source'] == 'None', 'source'] = 'email'
logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})
logs_grouped['conversion'] = logs_grouped['purchase']['sum'] / logs_grouped['purchase']['count']
logs.loc[logs['source'] == 'undef', 'source'] = 'other' 
logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})
logs_grouped['conversion'] = logs_grouped['purchase']['sum'] / logs_grouped['purchase']['count']
print(logs_grouped)