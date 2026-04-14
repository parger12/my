import pandas as pd
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


target = pd.Series([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1])
predictions = pd.Series([1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1])

precision = precision_score(target, predictions)
recall = recall_score(target, predictions)
f1 = 2*precision*recall/(precision+recall)

print("Полнота:", recall)
print("Точность:", precision)
print("F1-мера:", f1)