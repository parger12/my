from matplotlib import pyplot as plt
from math import factorial

p =   0.2
n =   45

distr = []

for k in range(0, n + 1):
    c = factorial(n) // (factorial(k) * factorial(n-k))
    prob = c * (p**k) * ((1-p) ** (n - k))
    distr.append(prob)
                        

plt.bar(range(0,n+1), distr)
plt.show()