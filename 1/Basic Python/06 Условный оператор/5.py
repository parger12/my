marks = [91, 35, 65, 89, 78, 93]
for mark in marks:
    if 0 <= mark <= 59:
        print (2)
    elif 60<=mark<=72:
        print (3)
    elif 73<=mark<=84:
        print (4)
    else:
        print (5)


countries = ['СССР', 'Новая Зеландия', 'Италия', 'Италия', 'СССР', 'США']
for country in countries:
    if country == "СССР":
        print('Фильм вышел в СССР.')
    elif country == 'США':
        print ('The movie was released in USA.')
    elif country == 'Италия':
        print ('Il film e stato rilasciato in Italia.')
    else:
        print('Страна не определена.')