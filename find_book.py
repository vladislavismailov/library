from colorama import Fore, init, Style
import db
init()
menu = '''
Вы попали в меню поиска книги
Искать по:
    1 - ISBN коду,
    2 - Названию,
    3 - автору,
    4 - году,
    0 - выход в гланое меню
'''
def by_isbn(isbn):
    books = db.db_open()
    finded = False
    for book in books:
        if book["isbn"] == isbn:
            print("Книга Найдена: ")
            print(f"{Fore.GREEN}Название:{Style.RESET_ALL} {book["title"]}")
            print(f"{Fore.GREEN}Автор:{Style.RESET_ALL} {book["author"]}")
            print(f"{Fore.GREEN}Страниц:{Style.RESET_ALL} {book["pages"]}")
            print(f"{Fore.GREEN}Год выпуска:{Style.RESET_ALL} {book["year"]}")
            print(f"{Fore.GREEN}ИСБН:{Style.RESET_ALL} {book["isbn"]}")
            finded = True
        # print(Fore.RED + "Книга Не Найдена" + Style.RESET_ALL)
    if finded != True:
        print(f"{Fore.RED}Книга Не Найдена{Style.RESET_ALL}")


def by_title(title): 
    books = db.db_open()
    finded = False
    counter = 0
    for book in books:
        if title.lower() in book["title"].lower():
            print("\nКнига Найдена: ")
            print(f"{Fore.GREEN}Название:{Style.RESET_ALL} {book["title"]}")
            print(f"{Fore.GREEN}Автор:{Style.RESET_ALL} {book["author"]}")
            print(f"{Fore.GREEN}Страниц:{Style.RESET_ALL} {book["pages"]}")
            print(f"{Fore.GREEN}Год выпуска:{Style.RESET_ALL} {book["year"]}")
            print(f"{Fore.GREEN}ИСБН:{Style.RESET_ALL} {book["isbn"]}")
            finded = True
            counter += 1
        # print(Fore.RED + "Книга Не Найдена" + Style.RESET_ALL)
    if finded != True:
        print(f"{Fore.RED}Книга Не Найдена{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Найдено книг: {counter}{Style.RESET_ALL}")

def by_year(year):
    books = db.db_open()
    finded = False
    counter = 0
    for book in books:
        if book["year"] == int(year):
            print("Книга Найдена: ")
            print(f"{Fore.GREEN}Название:{Style.RESET_ALL} {book["title"]}")
            print(f"{Fore.GREEN}Автор:{Style.RESET_ALL} {book["author"]}")
            print(f"{Fore.GREEN}Страниц:{Style.RESET_ALL} {book["pages"]}")
            print(f"{Fore.GREEN}Год выпуска:{Style.RESET_ALL} {book["year"]}")
            print(f"{Fore.GREEN}ИСБН:{Style.RESET_ALL} {book["isbn"]}")
            finded = True
            counter += 1
        # print(Fore.RED + "Книга Не Найдена" + Style.RESET_ALL)
    if finded != True:
        print(f"{Fore.RED}Книга Не Найдена{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Найдено книг: {counter}{Style.RESET_ALL}")

def by_author(author): 
    books = db.db_open()
    finded = False
    counter = 0
    for book in books:
        if author.lower() in book["author"].lower():
            print("\nКнига Найдена: ")
            print(f"{Fore.GREEN}Название:{Style.RESET_ALL} {book["title"]}")
            print(f"{Fore.GREEN}Автор:{Style.RESET_ALL} {book["author"]}")
            print(f"{Fore.GREEN}Страниц:{Style.RESET_ALL} {book["pages"]}")
            print(f"{Fore.GREEN}Год выпуска:{Style.RESET_ALL} {book["year"]}")
            print(f"{Fore.GREEN}ИСБН:{Style.RESET_ALL} {book["isbn"]}")
            finded = True
            counter += 1
        # print(Fore.RED + "Книга Не Найдена" + Style.RESET_ALL)
    if finded != True:
        print(f"{Fore.RED}Книга Не Найдена{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Найдено книг: {counter}{Style.RESET_ALL}")

def show_menu(menu):
    while True:
        print(menu)
        num = int(input("Введите номер действия: "))
        if num == 0:
            break
        if num == 1:
            isbn = input("Введите ИСБН: ")
            by_isbn(isbn)
        if num == 2:
            title = input("Введите Часть Названия: ")
            by_title(title)
        if num == 3:
            author = input("Введите автора: ")
            by_author(author)
        if num == 4:
            year = input("Введите год: ")
            by_year(year)