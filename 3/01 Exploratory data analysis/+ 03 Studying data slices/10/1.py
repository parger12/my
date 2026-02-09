import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'E:\courses\Data science\my\3\01 Exploratory data analysis\+ 02 First graphs and conclusions\2\visits.csv', sep = '\t') 

data['too_fast'] = data['time_spent'] < 60

too_fast_stat = data.pivot_table(index='id', values='too_fast')

data['too_slow'] = data['time_spent'] > 1000

too_slow_stat = data.pivot_table(index='id', values='too_slow')

too_slow_stat.hist(bins=30)
plt.show()
