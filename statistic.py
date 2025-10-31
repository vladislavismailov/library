import db
# 1 - Общее кол-во книг в библиотеке
# 0 - выход в главное меню
menu = '''
Вы попали в меню статистики
Выберите раздел:
    1 - количество книг,
    0 - выход в главное меню
'''

def get_total_books():
    books = db.db_open()
    counter_book = 0
    for book in books:
        counter_book += book["amount"]
    print(f"Всего книг в библеотеке: {counter_book}")

def show_menu(menu):
    while True:
        print(menu)
        num = int(input("Введите номер действия: "))
        if num == 0:
            break
        if num == 1:
            get_total_books()