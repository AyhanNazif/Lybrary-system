library_list = [["1", "Александрина", "София ул.Панега 15", [["11","Светлин Наков","Python Basics","Компютри","Софт Прес"],
                                                    ["12","Светлин Наков","Java Basics","Компютри","Софт Прес"]
                                                    ]],
                ["2", "БАН", "София ул.Лом 4", [["13","Светлин Наков","C++ Basics","Компютри","Софт Прес"],
                                                    ["14","Светлин Наков","PHP Basics","Компютри","Софт Прес"]
                                                    ]],
                ["3", "Съзнание", "София ул.Христо Ботев 20", [["15","Светлин Наков","C# Basics","Компютри","Софт Прес"],
                                                    ["16","Светлин Наков","Javascript Basics","Компютри","Софт Прес"]
                                                    ]]
                ]

print("Всички библиотеки:")
for x in library_list:
    print(x[0], x[1])

class Books:
    def __init__(self, book_number, author, title, genre, publisher):
        self.book_number = book_number
        self.author = author
        self.title = title
        self.genre = genre
        self.publisher = publisher

    def get_books_by_library(self):
        print(self.book_number,",", self.title)

    def get_info_book(self):
        print(self.author,",",self.title,",",self.genre,",",self.publisher)

class Library:
    def __init__(self, number, name, address, books:Books):
        self.number = number
        self.name = name
        self.address = address
        self.books = books

    def get_library(self):
        print("Име:", self.name, "Номер:", self.number)


while True:
    library_input = input("Избери библиотека по име или номер:").strip()

    for lib_list in library_list:
        library_name = lib_list[1]
        library_id = lib_list[0]
        if library_input == library_name or library_input == library_id:
            lib = Library(*lib_list)
            lib.get_library()
            for book in lib_list[3]:
                bk = Books(*book)
                bk.get_books_by_library()

            book_info = input("Въведи номер на книга за повече информация или с quit излез от програмата: ").strip()

            for book in lib_list[3]:
                book_id = book[0]
                if book_info == book_id:
                    bk = Books(*book)
                    bk.get_info_book()
                elif book_info == "quit":
                    exit("Край на програмата!")
