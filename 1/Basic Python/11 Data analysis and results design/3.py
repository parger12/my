import pandas as pd
df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\music_log_upd.csv')
print(df.head(15))
print (df.columns)
na_number = df.isna().sum()
print(na_number)
duplicated_number = df.duplicated().sum()
print(duplicated_number)