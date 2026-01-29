import pandas as pd
data = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\data1.csv')
rows = [True, False, True, False, False, False, True]
print (data.loc[rows])