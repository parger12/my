import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r'E:\courses\Data science\my\3\01 Exploratory data analysis\+ 02 First graphs and conclusions\2\visits.csv', sep = '\t') 


data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index')
good_data = good_data.query('60 <= time_spent <= 1000')
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')
stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat['good_time_spent'] = good_stat['time_spent']
id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])
id_name.columns = ['name', 'count']
station_stat_full = id_name.join(good_stations_stat)
good_stat2 = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
)
good_stat2.columns = ['median_time', 'stations']
final_stat = stat.join(good_stat2)

final_stat = final_stat.dropna(subset=['median_time'])

final_stat = final_stat.sort_values(by='median_time')

big_nets_stat = final_stat.query('stations > 10')

station_stat_full['group_name'] = station_stat_full['name'].where(station_stat_full['name'].isin(big_nets_stat.index), 'Другие')

stat_grouped = (station_stat_full.query('count > 30').pivot_table(index='group_name', values='time_spent', aggfunc=['median', 'count']))

stat_grouped.columns = ['time_spent', 'count']

stat_grouped.sort_values(by='time_spent', inplace=True)

good_data['group_name'] = good_data['name'].where(good_data['name'].isin(big_nets_stat.index), 'Другие')

for name, group_data in good_data.groupby('group_name'):
    group_data['time_spent'].plot(y='time_spent', title=name, kind='hist', bins = 50, grid=True)
    plt.show()