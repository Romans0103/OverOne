# Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в списке чисел.
# Количество введенных чисел  в список и искомая цифра задаются с клавиатуры. Числа выбираются рандомно.
import random

number = int(input("Задайте количество чисел в списке: "))
number_des = int(input("Введите искомую цифру от 0 до 9: "))
count = 0
number_list = [(random.randint(0, 9)) for i in range(number)]

for k in number_list:
    if k == number_des:
        count += 1
print(number_list)
print(count)





