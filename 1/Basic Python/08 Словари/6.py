arts_info = {
    'Звёздная ночь': 'Ван Гог Винсент',
    'Крик': 'Мунк Эдвард',
    'Неизвестная': 'Крамской Иван',
    'Итальянский полдень': 'Брюллов Карл',
    'Рожь': 'Шишкин Иван',
}
print(arts_info['Крик'])
print(arts_info.get('Рожь'))



nba_players = {
    'Джеймс Харден': [2191, 2818, 2335],
    'Леброн Джеймс': [2251, 1505, 1698],
    'Дэмиан Лиллард': [1962, 2067, 2009],
}
for player, score in nba_players.items():
    average = sum(score)/len(score)
    print(f'{player} {average}')




tracklist = [
    {
        'title': 'Stronger', # название трека
        'artist': 'Saimoo', # исполнитель
        'duration': 145, # продолжительность (в секундах)
        'genre': 'Deep House', # жанр
    },
    {
        'title': 'Alors On Danse',
        'artist': 'Stromae',
        'duration': 205,
        'genre': 'Hip-Hop',
    },
    {
        'title': 'Don\'t Be So Shy',
        'artist': 'Imany (Filatov & Karas Remix)',
        'duration': 190,
        'genre': 'Deep House',
    },
    {
        'title': 'Off My Mind',
        'artist': 'Matvey Emerson',
        'duration': 130,
        'genre': 'Deep House',
    },
    {
        'title': 'Now You\'re Gone',
        'artist': 'Basshunter',
        'duration': 154,
        'genre': 'Eurodance',
    },
    {
        'title': 'It Was A Good Day',
        'artist': 'Ice Cube',
        'duration': 260,
        'genre': 'Hip-Hop',
    },
    {
        'title': 'Diva',
        'artist': 'Beyonce',
        'duration': 200,
        'genre': 'Hip-Hop',
    }
]
hip_hop_duration = 0
for track in tracklist:
    if  track ['genre'] == 'Hip-Hop':
        hip_hop_duration += track['duration']


print(hip_hop_duration)





from json import dumps


tracklist = [
    {
        'title': 'Stronger', # название трека
        'artist': 'Saimoo', # исполнитель
        'duration': 145, # продолжительность (в секундах)
        'genre': 'Deep House', # жанр
    },
    {
        'title': 'Alors On Danse',
        'artist': 'Stromae',
        'duration': 205,
        'genre': 'Hip-Hop',
    },
    {
        'title': 'Don\'t Be So Shy',
        'artist': 'Imany (Filatov & Karas Remix)',
        'duration': 190,
        'genre': 'Deep House',
    },
    {
        'title': 'Off My Mind',
        'artist': 'Matvey Emerson',
        'duration': 130,
        'genre': 'Deep House',
    },
    {
        'title': 'Now You\'re Gone',
        'artist': 'Basshunter',
        'duration': 154,
        'genre': 'Eurodance',
    },
    {
        'title': 'It Was A Good Day',
        'artist': 'Ice Cube',
        'duration': 260,
        'genre': 'Hip-Hop',
    },
    {
        'title': 'Diva',
        'artist': 'Beyonce',
        'duration': 200,
        'genre': 'Hip-Hop',
    }
]


deep_house_tracklist = []
for track in tracklist:
    if track['genre'] == 'Deep House':
        deep_house_tracklist.append(track)
        
for track in deep_house_tracklist:
    print(dumps(track, indent=4))