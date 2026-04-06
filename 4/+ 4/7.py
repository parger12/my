from scipy import stats as st
import numpy as np
import pandas as pd

revenue = pd.read_csv('/datasets/revenue.csv', header = None)
revenue = revenue.loc[:, 0]

interested_value = 50000

alpha = 0.05

results = st.ttest_1samp(revenue, interested_value)

print('p-значение:',  results.pvalue/2) 

if (results.pvalue / 2 < alpha) and (revenue.mean() < interested_value):
    print("Отвергаем нулевую гипотезу: выручка значимо меньше 50 тысяч")
else:
    print("Не получилось отвергнуть нулевую гипотезу: выручка достигает запланированных показателей")