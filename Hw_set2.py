from random import random
n = 10
lst = [0] * n
for i in range(n):
    lst[i] = int(random() * 30)
print(lst)

set1 = set(lst)
if len(lst) == len(set1):
    print("Дубликатов нет, все элементы уникальны")
else:
    print("Есть дубликаты")