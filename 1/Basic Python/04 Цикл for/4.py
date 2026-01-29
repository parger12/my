total = 0
marks = [90, 85, 83, 92]
for mark in marks:
    total += mark 
print (total)



marks = [90, 85, 83, 92]
total = sum(marks)
print(total)



marks = [90, 85, 83, 92]
max_mark = max(marks)
print(max_mark)


marks = [90, 85, 83, 92]
max_mark = 0
for mark in marks:
    if mark > max_mark:
        max_mark = mark
print(max_mark)