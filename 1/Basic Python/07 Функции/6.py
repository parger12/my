def filter_by_year(data, year=1990):
    filter_by = []
    for movie in data:
        if movie[2]>year:
            filter_by.append(movie)
    return filter_by

def print_movie_table (data):
    for movie in data:
        for elem in movie:
            print(f'{elem:<45}', end=' ')
        print ()


movies_table = [
    ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111],
    ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730],
    ['Тёмный рыцарь', 'США', 2008, 'фантастика, боевик, триллер', 152, 8.499],
    ['Список Шиндлера', 'США', 1993, 'драма', 195, 8.818],
    ['Властелин колец: Возвращение Короля', 'Новая Зеландия', 2003, 'фэнтези, приключения, драма', 201, 8.625],
    ['Криминальное чтиво', 'США', 1994, 'триллер, комедия, криминал', 154, 8.619],
    ['Хороший, плохой, злой', 'Италия', 1966, 'вестерн', 178, 8.521],
    ['Бойцовский клуб', 'США', 1999, 'триллер, драма, криминал', 139, 8.644],
    ['Харакири', 'Япония', 1962, 'драма, боевик, история', 133, 8.106],
    ['Сталкер', 'СССР', 1979, 'фантастика, драма, детектив', 163, 8.083],
    ['Иди и смотри', 'СССР', 1985, 'драма, военный', 136, 8.094]
]

filter_movies = filter_by_year(movies_table)
print_movie_table(filter_movies)




def filter_by_genre(data, genre='драма'):
    filter_genre = []
    for movie in data:
        if genre.lower() in movie[3].lower() :
            filter_genre.append(movie)
    return filter_genre

filter_by_ge = filter_by_genre(movies_table)
print_movie_table(filter_by_ge)
