import pandas as pd
df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\music_log.csv')
df = df.rename (columns={
    '  user_id': 'user_id', 
    'total play': 'total_play', 
    'Artist': 'artist'
    })
print(df.columns)