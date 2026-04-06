from scipy import stats as st
import numpy as np

pages_per_session_autumn = [7.1, 7.3, 9.8, 7.3, 6.4, 10.5, 8.7, 
                            17.5, 3.3, 15.5, 16.2, 0.4, 8.3, 
                            8.1, 3.0, 6.1, 4.4, 18.8, 14.7, 16.4, 
                            13.6, 4.4, 7.4, 12.4, 3.9, 13.6, 
                            8.8, 8.1, 13.6, 12.2]
pages_per_session_summer = [12.1, 24.3, 6.4, 19.9, 19.7, 12.5, 17.6, 
                            5.0, 22.4, 13.5, 10.8, 23.4, 9.4, 3.7, 
                            2.5, 19.8, 4.8, 29.0, 1.7, 28.6, 16.7, 
                            14.2, 10.6, 18.2, 14.7, 23.8, 15.9, 16.2, 
                            12.1, 14.5]

alpha = 0.01

results = st.ttest_ind(pages_per_session_autumn, pages_per_session_summer)

print('p-значение:', results.pvalue)

if results.pvalue < alpha:
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")