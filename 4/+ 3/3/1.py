import random

random.seed(1111)  # метод seed() задаёт степень случайности, не меняйте её
def calculate_p(N):
    cnt_21_40 = 0
    for i in range(N):
        random_integer = random.randint(1, 100)
        if 21 <= random_integer <= 40:
            cnt_21_40 += 1 
    return cnt_21_40/N
p_20 = calculate_p(20)
p_400 = calculate_p(400)
p_10000 = calculate_p(10000)

print(p_20, p_400, p_10000)