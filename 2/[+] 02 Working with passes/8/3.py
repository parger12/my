import pandas as pd
logs = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\8\logs1.csv')
logs ['email'] = logs ['email'].fillna(value='')
logs.loc[logs['source'] == 'None', 'source'] = 'email'
