
import pandas as pd
import numpy as np

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
variance = data.var(ddof=1)
standard_dev = data.std(ddof=1)
print(standard_dev)