import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r'E:\courses\Data science\my\3\01 Exploratory data analysis\02 First graphs and conclusions\2\visits.csv', sep = '\t') 
name_stat = data.pivot_table (index = 'name', values = 'time_spent')

data['time_spent'].hist(bins=100, range=(0,1500))
