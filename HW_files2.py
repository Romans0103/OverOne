# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os


import os

# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
os.chdir('C:/Users/Admin/Desktop')
os.mkdir('Folder')
os.chdir('Folder')
with open('test_1.txt', 'w+') as file:
    file.read()
with open('test_2.txt', 'w+') as file:
    file.read()
with open('test_3.txt', 'w+') as file:
    file.read()
#
# # Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
print('Переименованы файлы')

# После этого удалите созданную папку.
path_1 = 'C:/Users/Admin/Desktop/Folder/rename_1.txt'
path_2 = 'C:/Users/Admin/Desktop/Folder/rename_2.txt'
path_3 = 'C:/Users/Admin/Desktop/Folder/rename_3.txt'
os.remove(path_1)
os.remove(path_2)
os.remove(path_3)
print('Каталог "Folder" пустой')
os.chdir('..')
os.rmdir('Folder')
print('Каталог удалён')







