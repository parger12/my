import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'E:\courses\Data science\my\3\01 Exploratory data analysis\+ 02 First graphs and conclusions\2\visits.csv', sep = '\t') 

data['date_time'] = pd.to_datetime(data['date_time'], format = '%Y%m%dT%H%M%S')

data['local_time'] = data['date_time'] + pd.Timedelta(hours=3)

data['date_hour'] = data['date_time'].dt.round('H')

sample = data.query('id == "3c1e4c52"')

pivot = sample.pivot_table(index='date_hour', values='time_spent', aggfunc=('count'))

pivot.plot(grid=True, figsize = (12,5 ))
plt.show()