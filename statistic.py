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

def show_menu(menu):
    utils.clear_screen()
    while True:
        print(menu)
        num = int(input("Введите номер действия: "))
        if num == 0:
            break
        if num == 1:
            get_total_books()
        if num == 2:
            count_gived_books()
