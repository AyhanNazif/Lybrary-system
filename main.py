from hard import Library, Book

lib = Library.get_all_libraries()
Library_id = []
for x in lib:
    print(x)
    Library_id.append(str(x[0]))
print("За да излезете от програмата натиснете 0.")

while True:
    library_input = input("Въведете номер на библиотека: ").strip()
    if library_input == "0":
        exit("Край на програмата!")

    if library_input in Library_id:
        operation_input = input("Въведете операция add/show/delete: ").strip()
        if operation_input == "add":
            add_book_input = input("Добавете книга в библиотеката: заглавие(символи),автор(символи),жанр(символи),издател(символи)").strip().split(",")
            Book.add_book(add_book_input, library_input)
        elif operation_input == "show":
            Book.get_books(library_input)
            edit_message = input("Искате ли да редактирате някоя книга от библиотеката? y/n: ").strip()
            if edit_message == "y":
                edit_book_id = input("Въведете номер на книга от библиотеката: ").strip()
                Book.get_book_by_id(edit_book_id, library_input)
                edit_book_input = input("Редактирайте книгата:заглавие(символи),автор(символи),жанр(символи),издател(символи): ").strip().split(",")
                Book.update_book(edit_book_input, edit_book_id)
            else:
                pass
        elif operation_input == "delete":
            Book.get_books(library_input)
            delete_input = input("Изберете номер на книга за изтриване, от библиотеката: ").strip()
            Book.delete_book(delete_input, library_input)
        else:
            print("Невалидна операция!")
    else:
        print("Невалиден номер на библиотека!")
