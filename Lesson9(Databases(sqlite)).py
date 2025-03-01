import sqlite3

"""простое подключение"""
# создаем подключение к базе данных
connection = sqlite3.connect("CPS_22134_DB.sl3")

# указываем курсор
cur = connection.cursor()

print(connection)
print(cur)
connection.close()


"""создание таблицы"""
connection = sqlite3.connect("CPS_22134_DB.sl3")
cur = connection.cursor()
# выполняем скрипт позволяющий создать новую таблицу
cur.execute("CREATE TABLE students (name TEXT);")
# подтверждаем
connection.commit()
connection.close()


"""добавление элементов в таблицу"""
connection = sqlite3.connect("CPS_22134_DB.sl3")
cur = connection.cursor()
# выполняем скрипт позволяющий добавить элемент в таблицу
cur.execute("INSERT INTO students (name) VALUES ('Aruz');")
# подтверждаем
connection.commit()
connection.close()


"""вывод элементов из таблицы"""
connection = sqlite3.connect("CPS_22134_DB.sl3")
cur = connection.cursor()
# выполняем скрипт позволяющий достать элемент из таблицу
cur.execute("SELECT name FROM students;")
# подтверждаем
connection.commit()
res = cur.fetchall()
print(res)
connection.close()


"""удаление элемента"""
connection = sqlite3.connect("CPS_22134_DB.sl3")
cur = connection.cursor()
# выполняем скрипт позволяющий удалить элемент из таблицы
cur.execute("DELETE FROM students WHERE(name == 'Aziz');")
# подтверждаем
connection.commit()
connection.close()


"""обновление данные"""
connection = sqlite3.connect("CPS_22134_DB.sl3")
cur = connection.cursor()
# выполняем скрипт позволяющий изменить элемент из таблицы
cur.execute("UPDATE students SET name='Shamsaddin' WHERE rowid=1;")
# подтверждаем
connection.commit()
connection.close()


"""обновление данные"""
connection = sqlite3.connect("CPS_22134_DB.sl3")
cur = connection.cursor()
# выполняем скрипт позволяющий удалить таблицу
cur.execute("DROP TABLE students")
# подтверждаем
connection.commit()
connection.close()