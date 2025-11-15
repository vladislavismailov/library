from datetime import datetime, timedelta
from colorama import Fore, init, Style
init()
import db
import utils
# 1 - Общее кол-во книг в библиотеке
# 0 - выход в главное меню
menu = '''
Вы попали в меню статистики
Выберите раздел:
    1 - количество книг,
    2 - количество выданных книг,
    3 - книги на просрочке,
    4 - лучшие 5 книг библиотеки,
    0 - выход в главное меню
'''

def get_total_books():
    books = db.db_open()
    counter_book = 0
    for book in books:
        counter_book += book["amount"]
        counter_book += len(book["users"])
    utils.clear_screen()
    print(f"{Fore.BLUE}Всего книг в библеотеке: {counter_book}{Style.RESET_ALL}")

def count_gived_books():
    books = db.db_open()
    counter_book = 0
    for book in books:
        counter_book += len(book["users"])
    utils.clear_screen()
    print(f"{Fore.BLUE}Из библиотеки выдано: {counter_book}{Style.RESET_ALL}")
def retured_books():
    books = db.db_open()
    counter_books = 0
    for book in books:
            overdue_days = 0
            for user in book["users"]:
                if datetime.now().isoformat() > user["end"]:
                    d1 = datetime.fromisoformat(user["end"])
                    d2 = datetime.now()
                    overdue_days = (d2 - d1).days
                    print(f"Название: {book["title"]}")
                    print(f"ИСБН: {book["isbn"]}")
                    print(f"Владелец: {user["fio"]}")
                    print(f"Книгу Взяли С: {user["start"]}")
                    print(f"Должны Отдать: {user["end"]}")
                    print(f"ИИН Пользователя: {user["iin"]}")
                    print(f"{Fore.RED}: Книга Просроченна На: {overdue_days}Дней{Style.RESET_ALL}")
                    print("############################################")
                    counter_books += 1
    print(f"Всего Просроченных Книг: {counter_books}")
    
def top5_books():
    live_books = {}
    top5  = {
    "1": [],
    "2": [],
    "3": [],
    "4": [], 
    "5": []}
    max = 0
    index = 1
    books = db.db_open()
    for book in books:
        if len(book["users"]) > 0 or len(book["users_history"]) > 0:
            live_books[book["isbn"]] = len(book["users"]) + len(book["users_history"])
    for top in top5:
        for isbn in live_books:
            if index == 1:
                if live_books[isbn] > max:
                    max = live_books[isbn]
            elif live_books[isbn] > max and live_books[isbn] < live_books[top5[str(index - 1)][0]]:
                max = live_books[isbn]
        for isbn in live_books:
            if live_books[isbn] == max:
                top5[str(index)].append(isbn)
        max = 0
        index += 1
    for top in top5:
        print(top + " Место")
        for isbn in top5[top]:
            for book in books:
                if isbn == book["isbn"]:
                    print(f"Название: {book["title"]}")
                    print(f"ИСБН: {isbn}")
                    print(f"Брали: {live_books[isbn]}")
                    print(f"Автор: {book["author"]}")
                    print("                                              ")
        print("====================================================================")


def show_menu(menu):
    error_line = ""
    utils.clear_screen()
    while True:
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
            get_total_books()
        elif num == 2:
            count_gived_books()
        elif num == 3:
            retured_books()
        elif num == 4:
            top5_books()
        else:
            error_line = "Введите верный номер действия: "
    
