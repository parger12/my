import pandas as pd

data = pd.read_excel(r'E:\courses\Data science\my\2\04 Search for duplicates\2\stock.xlsx')
xiaomi = data[data['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum() 
huawei = data[data['item'] == 'Смартфон HUAWEI P30 lite'] ['count'].sum()
data = data.dropna().reset_index(drop=True)
data.loc[0, 'count'] = xiaomi
print (data)
