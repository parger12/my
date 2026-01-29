import pandas as pd
data = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\data1.csv')
rows = data['Статья'] == '+'
print (data.loc[rows])