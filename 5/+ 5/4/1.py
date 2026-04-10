def mse(answers, predictions):
    total = 0
    for i in range(len(answers)):
        errow = predictions[i] - answers[i]
        total = errow**2 + total
    return total/len(answers)

answers = [623, 253, 150, 237]
predictions = [649, 253, 370, 148]

print(mse(answers, predictions))