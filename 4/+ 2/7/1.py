import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_value =  data.mean()
spacing_all =  (data-mean_value).abs()
spacing_all_mean = spacing_all.mean()
print(spacing_all_mean)