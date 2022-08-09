a = input("Введите 10-значное число: ")
even = str()

for i in str(a):
    if int(i) % 2 == 0:
        even += i

print(even)