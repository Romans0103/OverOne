import sqlite3

conn = sqlite3.connect('База Данных.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS WORDS(word TEXT) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS DIGIT(digit INTEGER) ''')

spisok = ['white', 'black', 'red', 'yellow', 'orange', 'green', 'blue', 38, 75, 15, 24, 2, 99]
for element in spisok:
    if isinstance(element, str):
        cursor.execute(f'INSERT INTO WORDS  VALUES ("{element}"),')
        cursor.execute(f'INSERT INTO DIGITS VALUES ("{len(element)},")')
    elif element % 2:
        cursor.execute(f'INSERT INTO WORDS VALUES ("нечётное")')
    else:
        cursor.execute(f'INSERT INTO DIGITS VALUES ("{element}",)')
    conn.commit()
k = cursor.fetchall()
print(k)