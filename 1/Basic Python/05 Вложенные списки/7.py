sales = [
    ['Московская область', 105820, 112180],
    ['Ленинградская область', 85899, 91021],
    ['Самарская область', 35010, 32001],
    ['Ростовская область', 37011, 39595]
]

for sales_year in sales:
    sales_year.append ((sales_year[1]) + sales_year [2])

for row in sales:
    for elem in row:
        print (f'{elem:<45}', end=" ")
    print()