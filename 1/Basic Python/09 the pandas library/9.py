import pandas as pd
df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\music_log.csv')
rock = df[df['genre'] == 'rock']
rock_time = rock[['total play']]
rock_haters = rock_time[rock_time['total play'] <= 5]['total play'].count()

pop = df[df['genre'] == 'pop']
pop_time = pop[['total play']]
pop_haters = pop_time[pop_time['total play'] <= 5]['total play'].count()
print(f'Количество пропущенных треков жанра поп равно {pop_haters}')
print("Количество пропущенных треков жанра рок равно", rock_haters)
rock_skip = rock_haters/rock.shape[0]
pop_skip = pop_haters/ pop.shape[0]
print (f'Доля пропущенных композиций жанра рок равна:{rock_skip}')
print (f'Доля пропущенных композиций жанра поп равна:{pop_skip}')