position = [
    ['2019-data-01', '- 6'],
    ['2019-data-02', '+5'],
    ['2019-data-03', ' 5'],
    ['2019-data-04', '4'],
    ['2019-data-data', '5'],
    ['2019-data-06', '5'],
    ['2019-data-07', '4'],
    ['2019-data-08', 'Error 5'],
    ['2019-data-09', '3'],
    ['2019-data-10', '3'],
]
total_position = 0
count_lines = 0
wrong_lines_content = []
for row in position:
    try:
        count_lines += 1
        level = int(row[1])
        total_position += level
    except:
        wrong_lines_content.append(row)

print (f'Количество измерений ...{count_lines}')
print (f'Некорректные строки ... {wrong_lines_content}')