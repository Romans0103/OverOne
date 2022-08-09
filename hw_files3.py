# В текстовом файле посчитать количество строк, а также для каждой отдельной строки
# определить количество в ней символов.

file = open('1.txt')
line = 0
symbols = 0
for i in file:
    line += 1

    for k in i:
        if k != ' ' and symbols == 0:
            symbols = 1
        elif k == ' ':
            symbols = 0
    print(i, len(i), 'символов')
print(line, 'строк(и)')
file.close()
