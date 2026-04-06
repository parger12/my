from scipy import stats as st

mu = 100500 
sigma = 3500

bonus_threshold = 111000 
penalty_threshold = 92000 

p_bonus = 1 - st.norm.cdf(bonus_threshold, loc=mu, scale=sigma)

p_penalty = st.norm.cdf(penalty_threshold, loc=mu, scale=sigma)

print('Вероятность бонуса:', p_bonus)
print('Вероятность штрафа:', p_penalty)