import pandas as pd
metrica = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\9\metrica_data.csv')
age_avg = metrica['age'].mean()
metrica ['age'] = metrica ['age'].fillna (value=32)
time_avg = metrica['time'].mean()
desktop_data = metrica.loc[metrica['device_type'] == 'desktop']
desktop_data_time_avg = desktop_data['time'].mean()
mobile_data = metrica[metrica['device_type'] == 'mobile']
print (mobile_data)