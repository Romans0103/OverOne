import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS WORDS(
        id INTEGER PRIMARY KEY,
        words TEXT
    );
    CREATE TABLE IF NOT EXISTS DIGITS(
        id INTEGER PRIMARY KEY,
        digits INTEGER
    )   
    '''
    cursor.executescript(query)


spisok = ['white', 'black', 'red', 'yellow', 'orange', 'green', 'blue', 38, 75, 15, 24, 2, 99]
for i in spisok:
    if type(i) == str:
        cursor.execute('''INSERT INTO WORDS(words)  VALUES(?)''', (i,))
        db.commit()
        cursor.execute('''INSERT INTO DIGITS(digits) VALUES(?)''', (len(i),))
        db.commit()
    elif type(i) == int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO DIGITS(digits) VALUES(?)''', (i,))
            db.commit()
        else:
            cursor.execute('''INSERT INTO DIGITS(digits) VALUES('нечётное')''')
            db.commit()
    else:
        continue
cursor.execute('SELECT COUNT (*) FROM DIGITS')
count = cursor.fetchone()
for i in count:
    if i > 5:
        cursor.execute('DELETE FROM WORDS WHERE id = 1')
        db.commit()
    else:
        cursor.execute('UPDATE WORDS SET words = "hello" WHERE id = 1')
        db.commit()
    print(f'Строк во второй таблице: {count[0]}.')
