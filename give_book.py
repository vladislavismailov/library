from datetime import datetime, timedelta
import db
import utils
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
    error_line = ""
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
        elif num == 2:
            iin = input("ВВедите ИИН: ")
            flag = False
            if len(iin) == 12 and iin.isdigit() == True:
                user["iin"] = iin
                flag = True
            if flag == False:
                print(f"{Fore.RED}Ошибка! Данный ИИН Не Верный{Style.RESET_ALL}")
        elif num == 3:
            fio = input("ВВедите ФИО Читателя: ")
            user["fio"] = fio
        elif num == 4:
            try:
                days = int(input("Введите на сколько дней выдать книгу от 1 до 365: "))
            except ValueError:
                error_line = "Вы ввели не число!!!"
                continue
            if days > 0 and days < 366:
                user["days"] = days
            else:
                print(f"{Fore.RED}Ошибка! Введите число от 1 до 365{Style.RESET_ALL}")
        elif num == 5:
            if len(user["isbn"]) > 0 and len(user["iin"]) > 0 and  len(user["fio"]) > 0:
                user["start"] = datetime.now().isoformat()
                user["end"] = (datetime.now() + timedelta(days=user["days"])).isoformat()
                print(user)
                for book in books:
                    if book["isbn"] == user["isbn"]:
                        if book["amount"] >= 1:
                            book["users"].append(user)
                            book["amount"] -= 1
                            print(book)
                            db.db_write(books)
            else:
                error_line = "Ошибка! Заполнены не все поля"
                continue
        else:
            error_line = "Ошибка! Неправильно набран номер действия"
 
