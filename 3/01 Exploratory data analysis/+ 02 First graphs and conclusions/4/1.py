import pandas as pd

data = pd.read_csv(r'E:\courses\Data science\my\3\01 Exploratory data analysis\02 First graphs and conclusions\2\visits.csv', sep = '\t') 
name_stat = data.pivot_table (index = 'name', values = 'time_spent')

print (name_stat)