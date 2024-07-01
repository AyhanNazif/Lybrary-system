import csv
import mysql.connector

connector = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=3306,
)
cursor = connector.cursor()


def load_books_from_csv(file_path):

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return list(reader)


books = load_books_from_csv("books.csv")
libraries = load_books_from_csv("libraries.csv")

cursor.execute('CREATE DATABASE IF NOT EXISTS library')
cursor.execute('USE library')
cursor.execute('''
CREATE TABLE IF NOT EXISTS libraries(  
    id INT NOT NULL AUTO_INCREMENT,  
    name VARCHAR(50),  
    location VARCHAR(100),  
    PRIMARY KEY (id)  
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS books(  
    id INT NOT NULL AUTO_INCREMENT,  
    title VARCHAR(50),  
    author VARCHAR(50),  
    genre VARCHAR(50),  
    publisher VARCHAR(50),  
    library_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY(library_id) REFERENCES libraries(id)
);
''')

sql_libraries = "INSERT INTO libraries (id, name, location) VALUES (%s, %s, %s)"
cursor.executemany(sql_libraries, libraries)

sql_books = "INSERT INTO books (id, title, author, genre, publisher, library_id) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(sql_books, books)

connector.commit()
