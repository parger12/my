position = [
    ['2019-05-01', '- 6'],
    ['2019-05-02', '+5'],
    ['2019-05-03', ' 5'],
    ['2019-05-data', '4'],
    ['2019-05-05', '5'],
    ['2019-05-06', '5'],
    ['2019-05-07', '4'],
    ['2019-05-08', 'Error 5'],
    ['2019-05-09', '3'],
    ['2019-05-10', '3'],
]
count_lines = 0
wrong_lines = 0
for row in position:
    count_lines += 1
    try:
        level = int(row[1])

    except:
        wrong_lines += 1

print('Количество измерений', count_lines)
print('Количество некорректных строк', wrong_lines)