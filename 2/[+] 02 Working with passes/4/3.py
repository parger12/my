import pandas as pd
hogwarts_points = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\4\hogwarts_points.csv')
hogwarts_points['faculty_name'] = hogwarts_points['faculty_name'].fillna('Гриффиндор')
faculty_points = hogwarts_points.groupby('faculty_name')['points'].sum()
winner = faculty_points.idxmax()
print (faculty_points)
print()
print (winner)