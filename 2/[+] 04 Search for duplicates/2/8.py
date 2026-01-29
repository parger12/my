
import pandas as pd
stock = pd.read_excel(r'E:\courses\Data science\my\2\04 Search for duplicates\2\stock.xlsx')
xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()
# print(xiaomi)
# print(huawei)
stock['item'] = stock['item'].drop_duplicates()
stock = stock.dropna().reset_index(drop=True)
stock.loc[0, 'count'] = xiaomi
stock.loc[3, 'count'] = huawei
print(stock)
