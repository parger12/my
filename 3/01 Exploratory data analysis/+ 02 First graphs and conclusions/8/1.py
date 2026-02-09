import random
import pandas as pd
import matplotlib.pyplot as plt

def coin_flip():
    score = random.randint(0, 1)
    return score

def flips_heads(repeat):
    total = 0
    for i in range(repeat):
        flip = coin_flip()
        total += flip
    return total

experiments = []

for i in range(1000):
    experiments.append(flips_heads(10))


df_experiments = pd.DataFrame(experiments, columns=['heads'])

df_experiments.hist(bins=11, range=(0,10))
plt.show()
