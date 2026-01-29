import pandas as pd
purchases = pd.read_csv (r'E:\courses\Data science\my\2\02 Working with passes\2\returned.csv')
purchases ['total'] = purchases['first'] + purchases ['repeated']
purchases['repeated_share'] = purchases['repeated']/purchases['total']
print (purchases)
