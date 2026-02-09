import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'E:\courses\Data science\my\3\01 Exploratory data analysis\+ 02 First graphs and conclusions\2\visits.csv', sep = '\t') 

sample = data.query('id == "3c1e4c52"')

data['time_spent'].hist(bins=100, range = (0,1500))
plt.show()
sample['time_spent'].hist(bins=100, range = (0,1500))
plt.show()
