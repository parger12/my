import pandas as pd
data = pd.read_csv(r'E:\courses\Data science\my\2\03 Changing data types\5\position.csv') 
data['timestamp'] = pd.to_datetime(data['timestamp'], format = '%Y-%m-%dT%H:%M:%S')
data['month'] = pd.DatetimeIndex(data['timestamp']).month
print(data)