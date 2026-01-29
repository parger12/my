import pandas as pd
df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\music_log.csv')
genre_fight = df[['genre', 'Artist']]
print(genre_fight)


genre_pop = df[df['genre' ] == 'pop']['genre'].count ()

print (genre_pop)

genre_rock = df[df['genre'] == 'rock']['genre'].count()
print (f'Число прослушанных треков в жанре рок равно ...{genre_rock}')

if genre_pop > genre_rock:
    print(f'Поп-музыку слушают больше.')
else:
    print(f'Рок слушают больше.')