import pandas as pd
transactions = pd.read_excel(r'E:\courses\Data science\my\2\03 Changing data types\4\ids.xlsx') 
transactions ['id'] = pd.to_numeric(transactions['id'], errors='coerce')
print (transactions.tail())