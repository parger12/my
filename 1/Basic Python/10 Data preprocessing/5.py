import pandas as pd
df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\music_log.csv')
df['track'] = df['track'].fillna('unknown')
df['Artist'] = df['Artist'].fillna('unkown')
df = df.dropna(subset=['genre'])
print (df.head)