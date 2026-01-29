import pandas as pd
data = pd.read_csv(r'E:\courses\Data science\my\2\03 Changing data types\8\data_final.csv')
data_pivot = data.pivot_table (index=('category_name', 'subcategory_name'), columns='source', values='visits', aggfunc='sum')
data_pivot['ratio'] = data_pivot['organic']/ data_pivot['direct']
print ((data_pivot[data_pivot['direct']>1000].sort_values('ratio', ascending=False)).tail(10))
