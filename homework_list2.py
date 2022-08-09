from random import randint

list1 = []
for i in range(50):
    list1.append(randint(0, 100))
print(list1)


list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print()
for i in list2:

    list2.sort()
print(list2)