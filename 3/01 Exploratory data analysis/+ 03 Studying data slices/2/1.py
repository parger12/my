import pandas as pd

df = pd.DataFrame(
    {
        'From': [
            'Moscow',
            'Moscow',
            'St. Petersburg',
            'St. Petersburg',
            'St. Petersburg',
        ],
        'To': ['Rome', 'Rome', 'Rome', 'Barcelona', 'Barcelona'],
        'Is_Direct': [False, True, False, False, True],
        'Has_luggage': [True, False, False, True, False],
        'Price': [21032, 19250, 19368, 2268, 31425],
        'Date_From': [
            '20.07.19',
            '20.07.19',
            '04.07.2019',
            '03.07.2019',
            '05.07.2019',
        ],
        'Date_To': [
            '07.07.19',
            '07.07.19',
            '10.07.2019',
            '09.07.2019',
            '11.07.2019',
        ],
        'Airline': ['Belavia', 'S7', 'Finnair', 'Swiss', 'Rossiya'],
        'Travel_time_from': [995, 230, 605, 365, 255],
        'Travel_time_to': [350, 225, 720, 355, 250],
    }
)

max_price = df['Price'].max()
mask = df['Price'] * 1.5 < max_price


result = df[(df['Travel_time_from'] >= 365) | (df['Travel_time_to'] < 250)]


df['Date_To'] = pd.to_datetime(df['Date_To'], dayfirst=True)

result1 = df[(df['Is_Direct'] == False) & (df['Date_To'] < '2019-07-08')]

result2 = df[(~df['Is_Direct']) &(~df['Date_To'].isin(('09.07.2019', '10.07.2019', '11.07.2019')))]

print(result)


print(result1)



