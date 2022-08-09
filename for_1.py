a = input('Введите трёхзначное число: ')

Sum = 0

for i in a:
    Sum += int(i)

print("Сумма цифр числа", a, "равна", Sum)