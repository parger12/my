from scipy import stats as st

mu = 420
sigma = 65
prob = 0.9

n_shipment = st.norm.ppf(prob, loc=mu, scale=sigma)

print('Нужно заказать единиц товара:', int(n_shipment))