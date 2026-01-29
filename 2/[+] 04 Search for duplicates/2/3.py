import pandas as pd

data = pd.read_excel(r'E:\courses\Data science\my\2\04 Search for duplicates\2\stock.xlsx')

xiaomi = data[data['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum() 
print (xiaomi)