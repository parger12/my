import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r'E:\courses\Data science\my\3\01 Exploratory data analysis\+ 02 First graphs and conclusions\2\visits.csv', sep = '\t') 

data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')


good_ids = too_fast_stat.query('too_fast < 0.5')

good_data = data.query('id in @good_ids.index')

good_data = data.query('id in @good_ids.index and 60 <= time_spent <= 1000')

good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc=('median'))

good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')

stat = data.pivot_table(index='name', values='time_spent')

stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=('count', 'first'))

id_name.columns = ['count', 'name']

station_stat_full = id_name.join(good_stations_stat, on='id')

good_stat2 = station_stat_full.query('count > 30').pivot_table(index='name', values='time_spent', aggfunc=('median', 'count'))

good_stat2.columns = ['stations', 'median_time']

final_stat = stat.join(good_stat2, on='name')

print(final_stat)

