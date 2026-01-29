import pandas as pd
df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\music_log.csv')
shape_table = df.shape
print(df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)
shape_table_updated = df.shape
if shape_table_updated < shape_table:
    print (f'Таблица уменьшилась, текущий размер:{shape_table_updated}')
else:
    print (f'Размер таблицы не изменился, текущий размер:{shape_table_updated}')
print(df['genre'].unique())
df['genre'] = df ['genre'].replace({
    'электроника':'electronic'
    })
genre_final_count = df[df['genre'] == 'электроника'].count()['genre']
print("Количество значений 'электроника' после замены:", genre_final_count)
