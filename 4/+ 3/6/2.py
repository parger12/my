weight_probs = {
    '2': 0.25,
    '3': 0.5,
    '5': 0.25
}

# Математическое ожидание
expectation = sum(int(x) * p for x, p in weight_probs.items())

# Дисперсия
variance = sum((int(x) - expectation)**2 * p for x, p in weight_probs.items())

# Вывод
print('weight_probs =', weight_probs)
print('Математическое ожидание равно', expectation)
print('Дисперсия равна', variance)