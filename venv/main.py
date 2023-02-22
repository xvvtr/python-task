import psycopg2
from config import host, user, password, db_name

# conn = psycopg2.connect(
#     dbname=db_name,
#     user=user, 
#     password=password,
#     host=host
#     )
# #conn.autocommit = True
# cursor = conn.cursor()

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user=user,
                                  # пароль, который указали при установке PostgreSQL
                                  password=password,
                                  host="127.0.0.1",
                                  port="5432",
                                  database=db_name)

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")


# SQL-запрос для создания новой таблицы
    # create_table_query = '''CREATE TABLE mobile
    #                       (ID INT PRIMARY KEY     NOT NULL,
    #                       MODEL           TEXT    NOT NULL,
    #                       PRICE         REAL); '''
    # # Выполнение команды: это создает новую таблицу
    # cursor.execute(create_table_query)
    # connection.commit()
    # print("Таблица успешно создана в PostgreSQL")

# Выполнение SQL-запроса для вставки данных в таблицу
    # insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (6, 'Iphone12 black', 1200)"""
    # cursor.execute(insert_query)
    # connection.commit()
    # print("1 запись успешно вставлена")
    # # Получить результат
    # cursor.execute("SELECT * from mobile")
    # record = cursor.fetchall()
    # print("Результат", record)

# Выполнение SQL-запроса для обновления таблицы
    # update_query = """Update mobile set price = 1500 where id = 1"""
    # cursor.execute(update_query)
    # connection.commit()
    # count = cursor.rowcount
    # print(count, "Запись успешно удалена")
    # # Получить результат
    # cursor.execute("SELECT * from mobile")
    # print("Результат", cursor.fetchall())

# Выполнение SQL-запроса для удаления таблицы
    # delete_query = """Delete from mobile where id = 1"""
    # cursor.execute(delete_query)
    # connection.commit()
    # count = cursor.rowcount
    # print(count, "Запись успешно удалена")
    # # Получить результат
    # cursor.execute("SELECT * from mobile")
    # print("Результат", cursor.fetchall())

# Поиск объекта по полю ID
    # cursor.execute("""SELECT * FROM mobile WHERE id=2""")
    # print("Результат", cursor.fetchall())

# Поиск объекта по полю MODEL
    # cursor.execute("""SELECT * FROM mobile WHERE model LIKE '%Iphone%'""")
    # print("Результат", cursor.fetchall())


# except (Exception, Error) as error:
#     print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

