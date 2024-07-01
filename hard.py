import mysql.connector
connector = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=3306,
    database = 'library'
)
cursor = connector.cursor()

class Library:
    def __init__(self, pk, name, location):
        self.pk = pk
        self.name = name
        self.location = location

    @staticmethod
    def get_all_libraries():
        sql = "SELECT id,name FROM libraries"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            return result

class Book:

    def __init__(self,pk,title,author,genre,publisher,library_id):
        self.pk = pk
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.library_id = library_id

    @staticmethod
    def add_book(book:list, pk):
        try:
            sql = "INSERT INTO books(title,author,genre,publisher,library_id) VALUES(%s,%s,%s,%s,%s)"
            book.append(pk)
            cursor.execute(sql, book)
            connector.commit()
            print("Книгата е добавена успешно!")
        except mysql.connector.errors.ProgrammingError as err:
            print(err)
        except mysql.connector.errors.DatabaseError as err:
            print(err)


    @staticmethod
    def delete_book(pk, lk):
        try:
            sql = "DELETE FROM books WHERE id=%s AND library_id=%s"
            val = (pk, lk)
            cursor.execute(sql, val)
            connector.commit()
            if cursor.rowcount != 0:
                print("Книгата е изтрита успешно!")
            else:
                print("Неуспешно изтриване! Моля проверете номера на книгата от съответната библиотека")
        except mysql.connector.errors.DatabaseError as err:
            print(err)

    @staticmethod
    def update_book(book:list, pk):
        try:
            sql = "UPDATE books SET title = %s, author = %s, genre = %s, publisher = %s WHERE id = %s"
            book.append(pk)
            cursor.execute(sql, book)
            connector.commit()
            print("Книгата е редактирана успешно!")
        except mysql.connector.errors.ProgrammingError as err:
            print(err)

    @staticmethod
    def get_books(pk):
        sql = "SELECT books.id,books.title,books.author,books.genre,books.publisher,libraries.name " \
              "FROM books " \
              "LEFT JOIN libraries ON books.library_id = libraries.id " \
              "WHERE libraries.id = %s"
        cursor.execute(sql, [pk])
        result = cursor.fetchall()
        if result:
            for x in result:
                print(x)
        else:
            print("Невалиден номер за библиотека! Моля въведете номер от изброените библиотеки.")
            exit("Започнете от начало")

    @staticmethod
    def get_book_by_id(pk, lk):
        sql = "SELECT books.id,books.title,books.author,books.genre,books.publisher,libraries.name " \
                "FROM books " \
                "LEFT JOIN libraries ON books.library_id = libraries.id " \
                "WHERE books.id = %s AND books.library_id = %s"
        val = (pk, lk)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            print(result)
        else:
            print("Невалиден номер! Моля проверете номера на книгата от съответната библиотека.")
            exit("Започнете от начало.")
