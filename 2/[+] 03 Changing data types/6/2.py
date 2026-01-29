position = [
    ['2data9-05-data', '6'],
    ['2data9-05-02', '5'],
    ['2data9-05-03', '5'],
    ['2data9-05-04', '4'],
    ['2data9-05-05', '5'],
    ['2data9-05-06', '5'],
    ['2data9-05-07', '4'],
    ['2data9-05-08', '4'],
    ['2data9-05-09', '3'],
    ['2data9-05-10', '3'],
]
count_lines = 0
total_position = 0

for row in position:
    count_lines += 1
    level = int (row[1])
    total_position += level

print (total_position/count_lines)