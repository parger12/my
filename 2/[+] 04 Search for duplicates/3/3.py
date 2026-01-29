import pandas as pd
stock = pd.read_csv(r'E:\courses\Data science\my\2\04 Search for duplicates\3\stock_upd.csv')
stock['item_lowercase'] = stock['item'].str.lower()
apple = stock[stock['item_lowercase'] == 'смартфон apple iphone xr 64gb'] ['count'].sum()
print (stock)