from scipy import stats as st

import math as mt

binom_n = 23000
binom_p = 0.4

threshold = 9000

mu = binom_n * binom_p
sigma = (binom_n * binom_p * (1 - binom_p))**0.5

p_threshold = 1 - st.norm.cdf(threshold, loc=mu, scale=sigma)

print(p_threshold)