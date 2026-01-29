monuments = [
    {
        'name': 'Статуя Единства', # название
        'country': 'Индия', # страна
        'height': 182 # высота без постамента
    },
    {
        'name': 'Статуя богини Каннон в Сендае',
        'country': 'Япония',
        'height': 100
    },
    {
        'name': 'Родина-Мать зовёт!',
        'country': 'Россия',
        'height': 85
    },
    {
        'name': 'Будда Дорденма',
        'country': 'Бутан',
        'height': 51.5
    },
    {
        'name': 'Статуя Свободы',
        'country': 'США',
        'height': 46
    }
]

height_total = 0
for monument in monuments:
    height_total += monument ['height']

average_height = height_total/len(monuments)

print (average_height)



order = [
    {
        'item': 'Пицца Маргарита', # название позиции
        'category': 'пицца', # категория товара
        'quantity': 2, # количество в заказе
        'comment': 'Побольше сыра, пожалуйста!', # комментарий к заказу
        'price': 320 # стоимость одной единицы товара
    },
    {
        'item': 'Пицца с ветчиной',
        'category': 'пицца',
        'quantity': 1,
        'comment': '',
        'price': 410
    },
    {
        'item': 'Pepsi 1 л',
        'category': 'напитки',
        'quantity': 3,
        'comment': '',
        'price': 75
    },
    {
        'item': 'Сок яблочный 0.5 л',
        'category': 'напитки',
        'quantity': 1,
        'comment': '',
        'price': 80
    },
    {
        'item': 'Круассан с сыром',
        'category': 'выпечка',
        'quantity': 2,
        'comment': '',
        'price': 130
    }
]


total_price = 0
for elem in order:
    total_price += elem['price'] * elem['quantity']

print(total_price)