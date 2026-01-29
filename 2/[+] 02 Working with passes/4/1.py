import pandas as pd
hogwarts_points = pd.read_csv(r'E:\courses\Data science\my\2\02 Working with passes\4\hogwarts_points.csv')
print (hogwarts_points[hogwarts_points['faculty_name'].isnull()])