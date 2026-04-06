import pandas as pd
import matplotlib.pyplot as plt


pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54, 58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38, 55, 53, 53, 43, 77, 44, 63, 63, 54])

pur_time.hist(bins=([15, 35, 55, 75, 90]), alpha = 0.5)
plt.show()
pur_time.hist(bins=([15, 45, 55, 90]), alpha = 0.5)
plt.show()

