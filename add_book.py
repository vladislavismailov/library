import db
import utils
menu = '''
Вы попали в меню добавления книги
Добавить информацию:
    1 - ISBN код,
    2 - название, 
    3 - автора, 
    4 - год издания, 
    5 - кол-во страниц,
    6 - кол-во экземпляров (по умолчанию - 1)
    7 - ГОТОВО. ДОБАВИТЬ КНИГУ В БАЗУ!
    0 - выход в главное меню
'''

new_book = {
    "title": "",
    "author": "",
    "isbn": "",
    "year": 0,
    "pages": 0,
    "amount": 1,
}


def show_menu(menu):
    while True:
        utils.clear_screen()
        print(menu)
        num = int(input("Введите номер действия: "))
        if num == 0:
            break
        if num == 1:
            isbn = input("Введите ИСБН: ")
            new_book["isbn"] = isbn
        if num == 2:
            title = input("Введите название: ")
            new_book["title"] = title
        if num == 3:
            author = input("Введите автора: ")
            new_book["author"] = author
        if num == 4:
            year = int(input("Введите год: "))
            new_book["year"] = year
        if num == 5:
            pages = int(input("Введите количество страниц: "))
            new_book["pages"] = pages
        if num == 6:
            amount = int(input("Введите количество книг: "))
            new_book["amount"] = amount
        if num == 7:
            if len(new_book["isbn"]) > 0 and len(new_book["title"]) > 0 and len(new_book["author"]) > 0 and new_book["year"] > 0 and new_book["pages"] > 0:
                books = db.db_open()
                books.append(new_book) 
                db.db_write(books)# Добавляем в базу
                break 
            else:
                print("Ошибка! Заполнены не все поля!")