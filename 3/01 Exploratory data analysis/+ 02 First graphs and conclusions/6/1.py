import pandas as pd

data = pd.read_csv(r'E:\courses\Data science\my\3\01 Exploratory data analysis\02 First graphs and conclusions\2\visits.csv', sep = '\t') 
name_stat = data.pivot_table (index = 'name', values = 'time_spent')

total_visits = len(data)
total_stations = data['id'].unique().__len__()
total_days = 7
station_visits_per_day = total_visits/total_stations/total_days
print(data['name'].value_counts().head(10))