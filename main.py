import sqlite3


db = sqlite3.connect('puge.db')
c = db.cursor()
c.execute(
    '''CREATE TABLE IF NOT EXISTS user (hobby text,name text,surname text,year integer,points integer)''')

c.execute('INSERT INTO user VALUES ("чтение книг", "Jeka", "sj", 2007, 15)')
c.execute('INSERT INTO user VALUES ("спать", "Соня", "Иванов", 2006, 10)')

c.execute('INSERT INTO user VALUES ("Музыка", "Петр", "Попов", 2007, 15)')
c.execute('INSERT INTO user VALUES ("Рукоделие", "Мария", "Кузнецова", 2008, 12)')

c.execute('INSERT INTO user VALUES ("Чтение художественной и научной литературы", "", "", 2005, 10)')
c.execute('INSERT INTO user VALUES ("Игра на гитаре", "Вадим", "Сергеев", 2006, 8)')

c.execute('INSERT INTO user VALUES ("Паркур", "Эрбол", "Докторбеков", 2007, 17)')
c.execute('INSERT INTO user VALUES ("Тир", "Нурсултан", "Эшперов", 2007, 13)')

c.execute('INSERT INTO user VALUES ("Коллекционирование", "Актан", "Койчуманов", 2006, 9)')
c.execute('INSERT INTO user VALUES ("кулинария", "Аня", "Романова", 2008, 99)')


c.execute("SELECT rowid FROM user")
c.execute("UPDATE user SET name = 'genius' WHERE points = 10")
c.execute("SELECT rowid, surname, name FROM user ")
items = c.fetchall()
print(items)
for i in items: surname = i[1]
if len(surname) > 10: print(surname)
else: ...
c.execute("SELECT rowid, name FROM user WHERE name = 'genius'")
c.execute("DELETE FROM user WHERE rowid % 2 = 0")
print(c.fetchall())
db.commit()
db.close()






