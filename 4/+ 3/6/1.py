import numpy as np

x_probs = {
    '-4': 0.05,
    '-2': 0.25,
    '0': 0.1,
    '1': 0.1,
    '5': 0.1,
    '7': 0.05,
    '15': 0.35,
}


expectation = sum(int(x) * p for x, p in x_probs.items())

variance = sum((int(x) - expectation)**2 * p for x, p in x_probs.items())


print('Математическое ожидание равно', expectation)
print('Дисперсия равна', variance)