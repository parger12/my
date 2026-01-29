
import pandas as pd
stock = pd.read_csv(r'E:\courses\Data science\my\2\04 Search for duplicates\3\stock_upd.csv')
stock['item_lowercase'] = stock['item'].str.lower()
apple = stock[stock['item_lowercase'] == 'смартфон apple iphone xr 64gb']['count'].sum()
samsung = stock[stock['item_lowercase'] == 'смартфон samsung galaxy a30 32gb']['count'].sum()
# print(apple)
# print(samsung)
stock['item_lowercase'] = stock['item_lowercase'].drop_duplicates()
stock = stock.dropna().reset_index(drop=True)
stock.loc[3, 'count'] = apple
stock.loc[1, 'count'] = samsung
print (stock)
