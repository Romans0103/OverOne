# Задание 1
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


a = float(input('a = '))
b = float(input('b = '))
choice_operator = input('Выберите операцию (+, -, *, /) или введите "0" для выхода из калькулятора: ')
if choice_operator == '+':
    result = addition(a, b)
    print(f'Операция сложения. Результат {a} + {b} равен {result}')
elif choice_operator == '-':
    result = subtraction(a, b)
    print(f'Операция вычитания. Результат {a} - {b} равен {result}')
elif choice_operator == '*':
    result = multiply(a, b)
    print(f'Операция умножения. Результат {a} * {b} равен {result}')
elif choice_operator == '/':
    if b == 0:
        print('Деление на ноль')
    else:
        result = division(a, b)
    print(f'Операция деление. Результат {a} / {b} равен {result}')
elif choice_operator == '0':
    print('Программа завершена')



# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями

def func_type(x):
    if type(x) == tuple:
        print('Длина слов', len(x))
    elif type(x) == list:
        print('Количество букв',  len(list(filter(lambda x: type(x) == str, x))), 'чисел',
              len(list(filter(lambda x: type(x) in (int, float), x))))
    elif type(x) == int:
        odd = 0
        num = [int(i) for i in str(x)]
        print(num)
        for i in num:
            if int(i) % 2 != 0:
                odd += 1
        print(f'Количество нечётных цифр равно {odd}')
    elif type(x) == str:
        print('Количество букв', len(x))
    else:
        print('Неизвестный тип данных')


func_type((1, 2, 3))
func_type([1, 2, 3, 'a', 'b', 'c'])
func_type(129546)
func_type('OverOne')
func_type({1, 2, 5, 9, 81})


