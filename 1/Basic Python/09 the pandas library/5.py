import pandas as pd

df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\music_log.csv')
shape_table = df.shape
observations_table = shape_table[0]
observations_info_table = 67963
print (df.info)
print (observations_info_table)
print (f'Размер таблицы: {shape_table}')
print (f'Количество наблюдений:{observations_table}')   

if observations_info_table == observations_table:
    print(f'Решение верно, количество наблюдений равно',  {observations_table})
else:
    print('Решение неверно, проверьте ещё раз!')