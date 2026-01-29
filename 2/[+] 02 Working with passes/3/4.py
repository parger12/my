import pandas as pd
logs = pd.read_csv (r'E:\courses\Data science\my\2\02 Working with passes\3\logs.csv')
unique_emails = logs['email'].unique()
unique_user = logs ['user_id'].unique()
print (logs['source'].unique())