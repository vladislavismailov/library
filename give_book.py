import db
from colorama import Fore, init, Style
init()
menu = '''
Вы попали в меню выдачи книги
Добавьте информацию о пользователе:
    1 - ISBN код книги,
    2 - Введите ИИН читателя,
    3 - Введите ФИО читателя,
    4 - Срок на сколько выдать книгу (по умолчанию: 14 дней),
    5 - ГОТОВО! ВЫДАТЬ КНИГУ!
    0 - выход в гланое меню
'''

user = {
    "isbn": "",
    "iin": "",
    "fio": "",
    "days": 14,
    "start": "", # заполняется автоматически
    "end": "" # заполняется автоматически (сегодяшняя дата + 14 дней)
}

def show_menu(menu):
    while True:
        print(menu)
        num = int(input("Введите номер действия: "))
        if num == 0:
            break
        if num == 1:
            isbn = input("ВВедите ИСБН: ")
            flag = False
            books = db.db_open()
            for book in books:
                if book["isbn"] == isbn:
                    print('Найдено')
                    user["isbn"] = isbn
                    flag = True
            if flag == False:
                print(f"{Fore.RED}Ошибка! Данный ИСБН Не Верный{Style.RESET_ALL}")
        if num == 2:
            iin = input("ВВедите ИИН: ")
            flag = False
            if len(iin) == 12 and iin.isdigit() == True:
                user["iin"] = iin
                flag == True
            if flag == False:
                print(f"{Fore.RED}Ошибка! Данный ИИН Не Верный{Style.RESET_ALL}")
        if num == 3:
            fio = input("ВВедите ФИО Читателя: ")
            user["fio"] = fio
        if num == 4:
            print("Эта функция будет реализована позже: ")
        if num == 5:
            print("Эта функция будет реализована позже: ")