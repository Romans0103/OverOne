#  1. Создайте функцию, добавьте в неё локальное значение.
#  Сделайте так, чтобы другая функция принимала это значение в качестве параметра.


def func_1():
    a = 'OverOne'
    return a


def func_2(c):
    b = 'IT'
    return b, c


print(func_2(func_1()))


# 2. Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.


def is_prime(a):
    for i in range(0, a):
        if a == 0 and a == 1:
            return 'не является простым числом'
        elif 1 < a and a <= 1000 or a % i == 0:
            return False
        else:
            return True


print(is_prime(int(input("Введите число от 0 до 1000: "))))