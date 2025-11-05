# Программа для управления библиотекой. Версия 0.1   2025
# Авторы: Влад Исмаилов, Анатолий Уваров
import utils
import add_book
import find_book
import statistic
import give_book
from colorama import Fore, init, Style
init()


menu = '''
Вас приветствует программа "Библиотекарь"
Главное меню
    1 - добавить книгу в библиотеку,
    2 - искать книги в библиотеке, 
    3 - выдать книгу читателю, 
    4 - забрать книгу у читателя, 
    5 - статистика библиотеки
    0 - выход из программы

'''
isbn = 0
while True:
    utils.clear_screen()
    print(menu)
    num = int(input("Введите номер действия: "))
    if num == 1:
        add_book.show_menu(add_book.menu)
    elif num == 2:
        find_book.show_menu(find_book.menu)
    elif num == 3:
        give_book.show_menu(give_book.menu)
    elif num == 4:
        print("Эта функция будет реализована позже: ")
    elif num == 5:
        statistic.show_menu(statistic.menu)   
    elif num == 6:
        print("Эта функция будет реализована позже: ")
    elif num == 0:
        break
    else:
        print(Fore.RED + "ОШИБКА! Неправильно набран номер!" + Style.RESET_ALL)


