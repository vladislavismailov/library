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
    while True:
        print(menu)
        num = int(input("Введите номер действия: "))
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


        if num == 2:
            print("Эта функция будет реализована позже: ")
        if num == 0:
            break
