from scipy import stats as st

mu = 2400
sigma = 320
threshold = 3/4

x_25 = st.norm.ppf(1 - threshold, loc=mu, scale=sigma)

max_delivery_price = x_25 / 2

print('Максимальная стоимость доставки курьером:', max_delivery_price)