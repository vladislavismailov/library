import db
import utils
from colorama import Fore, init, Style
init()
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
    error_line = ''
    while True:
        utils.clear_screen()
        print(menu)
        if len(error_line) > 0:
            print(Fore.RED + error_line + Style.RESET_ALL )
            error_line = ''
        try:
            num = int(input("Введите номер действия: "))
        except ValueError:
                error_line = "Вы ввели не номер!!!"
                continue
        if num == 0:
            break
        elif num == 1:
            isbn = input("Введите ИСБН: ")
            new_book["isbn"] = isbn
        elif num == 2:
            title = input("Введите название: ")
            new_book["title"] = title
        elif num == 3:
            author = input("Введите автора: ")
            new_book["author"] = author
        elif num == 4:
            try:
                year = int(input("Введите год: "))
                new_book["year"] = year
            except ValueError:
                error_line = "Вы ввели неверный год!!!"
                continue
        elif num == 5:
            try:
                pages = int(input("Введите количество страниц: "))
                new_book["pages"] = pages
            except ValueError:
                error_line = "Вы ввели не верное количество страниц!!!"
                continue
        elif num == 6:
            try:
                amount = int(input("Введите количество книг: "))
                new_book["amount"] = amount
            except ValueError:
                error_line = "Вы ввели не верное количество книг!!!"
                continue
        elif num == 7:
            if len(new_book["isbn"]) > 0 and len(new_book["title"]) > 0 and len(new_book["author"]) > 0 and new_book["year"] > 0 and new_book["pages"] > 0:
                books = db.db_open()
                books.append(new_book) 
                db.db_write(books)# Добавляем в базу
                break 
            else:
                error_line = "Ошибка! Заполнены не все поля!"
        else:
            error_line = "Ошибка! Неверный номер действия!"