from colorama import Fore, init, Style
import db
import utils
init()
menu = '''
Вы попали в меню возврата книги
Сделать возврат по:
    1 - ISBN коду,
    2 - ИИН,
    0 - выход в гланое меню
'''
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
        books = db.db_open()
        if num == 1:
            isbn = input("Введите ИСБН: ")
            for book in books:
                if book["isbn"] == isbn:
                    book["amount"] += 1
                    index = 1
                    print("Данная книга находится у следующих читателей: ")
                    
                    for user in book["users"]:
                        print(f"{index} - {user["iin"]}")
                        index += 1

                    while True:
                        index = int(input("Введите номер читателя: "))
                        if(index >= 1 and index <= len(book["users"])):
                            break
                        print(f'{Fore.RED}Ошибка.  Введён неверный номер.{Style.RESET_ALL}')

                    index -= 1
                        
                    user = book["users"].pop(index)
                    book["users_history"].append(user)
                    db.db_write(books)
                    print(f"{Fore.GREEN}Книжка успешно возвращена{Style.RESET_ALL}")
                    break


        elif num == 2:
            iin = input("Введите ИИН Пользователя Который Возвращает Книгу: ")
            user_books = []
            name = ""
            for book in books:
                for user in book["users"]:
                    if user["iin"] == iin:
                        user_books.append(book)
                        if len(name) == 0:
                            name = user["fio"]
                    
            print(f"На ИИН {iin, name} Найдены Следующие Книги:")
            index = 1
            for book in user_books:
                print(f"{index} - ({book["isbn"]}) {book["title"]}")
                index += 1
            while True:
                try:
                    index = int(input("Введите номер книги: "))
                except ValueError:
                    error_line = "Вы ввели не номер!!!"
                if index >= 1 and index <= len(user_books):
                    break
                print(f'{Fore.RED}Ошибка.  Введён неверный номер.{Style.RESET_ALL}')

            index -= 1
            user_books[index]["amount"] += 1
            
            for idx, user in enumerate(user_books[index]["users"]):
                    if user["iin"] == iin:
                        user_books[index]["users_history"].append(user_books[index]["users"].pop(idx))
                        db.db_write(books)
                        print(f"{Fore.GREEN}Книжка успешно возвращена{Style.RESET_ALL}")
                        break
        elif num == 0:
            break
        else:
            error_line = "Ошибка! Введено неправильно число!"
