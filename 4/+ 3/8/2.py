from matplotlib import pyplot as plt
from math import factorial

n_exams = 6
failure_rate = 0.15
q = 1 - failure_rate

distr = []

for k in range(0, n_exams + 1):
    c = factorial(n_exams) // (factorial(k) * factorial(n_exams - k))
    prob = c * (failure_rate ** k) * (q ** (n_exams - k))
    distr.append(prob)

# построение гистограммы распределения вероятностей
plt.bar(range(0,n_exams+1), distr)
plt.show()
