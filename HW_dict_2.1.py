# Значениями словаря могут быть и списки. Создайте словарь с ключами BMW,
# Tesla и списками из 3х моделей в качестве значений. Выведите первое и последнее значения каждого из ключей.

cars = {'BMW': ['X3', 'X5', 'X6'],
        'Tesla': ['Model S', 'Model T', 'Model Y']}
for key, value in cars.items():
    print(key, ' ', value[0])
    print(key, ' ', value[2])



