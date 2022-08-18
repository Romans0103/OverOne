#  Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или равно длине слова,
# выводить все гласные, иначе согласные; если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе


class Example_str_int:

    def func1(self, arg):
        if isinstance(arg, str):
            if sum(x in "аеёиоуыюя" for x in arg.lower()) * sum(
                    x in "бвгджзйклмнпрстфхцчшщьъ" for x in arg.lower()) <= len(arg):
                return ''.join([x for x in arg if x.lower() in "аеёиоуыюя"])
            else:
                return ''.join([x for x in arg if x.lower() in "бвгджзйклмнпрстфхцчшщьъ"])
        elif isinstance(arg, int):
            return sum(int(x) for x in str(arg) if x in "2468") * self.func2(arg)

    def func2(self, arg):
        return len(str(arg))


object = Example_str_int()
test_1 = object.func1("Привет,поломал голову над домашним заданием.")
test_2 = object.func1("Это было сложно.")
test_3 = object.func1(756)

print(test_1)
print(test_2)
print(test_3)
