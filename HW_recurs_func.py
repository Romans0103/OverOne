import random

num = [random.randint(1, 100) for i in range(10)]
print(num)


def number_sum(a):
    if not a:
        return 0
    else:
        return a[0] + number_sum(a[1:])


print(number_sum(num))