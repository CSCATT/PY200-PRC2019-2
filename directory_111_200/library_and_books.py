"""
Библиотека книг, возможен поиск в каталоге по автору, названию, году;
добавление и удаление книги или автора в библиотеку
"""

import sqlite3
import json
import subprocess

SQL_JSON_SWITCHER = input("Введите sql для работы с БД или json (по шаблону если поле пустое) для работы с файлом .json: ")
CATALOG = {}  # Словарь для книг
COMMAND = str()  # переменная ввода команды для отработки ветки алгоритма

def sql_lite_connector():
    conn = sqlite3.connect('catalog.db')
    print ("Opened database successfully")

    conn.execute(''' CREATE TABLE BOOKS
             (ID INT PRIMARY KEY      NOT NULL,
             NAME           TEXT      NOT NULL,
             AUTHOR         TEXT      NOT NULL,
             YEAR           INT); ''')
    print ("Table created successfully")

    conn.close()
    #return conn

def insert_sql_operation ():
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AUTHOR,YEAR) \
          VALUES (ID_NUM, 'BOOK_NAME', 'AUTHOR_NAME', YEAR) ")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    conn.commit()
    print ("Records created successfully")

    conn.close()


def command_() -> str:
    """
    Use console for typing book name, author or command
    :return: str
    """
    global COMMAND; COMMAND = input("Ввод: ")
    return COMMAND


def add_or_rm(book: str, operation: str) -> None:
    """
    add/del the book from library
    :param book: str
    :param operation: str
    :return: None
    """

    global COMMAND
    # getting from catalog author, name and year
    book = book.split(", ")
    if len(book) == 2:
        name = book[0]
        author = book[1]
        year = "unknown"
    else:
        name = book[0]
        author = book[1]
        year = book[2]

    with open("catalog.json", "r") as file:
        CATALOG = json.load(file)

    if author in CATALOG and year in CATALOG[author]:
        # Add name
        if operation == "adding" or operation == "add":  # command add = adding
            if name not in CATALOG[author][year]:
                CATALOG[author][year].append(name)
                print("Book is added!")
            else:
                print("Book already is list!")

        # Name removal
        elif operation == "remove" or operation == "rm":  # command rm = remove
            if name in CATALOG[author][year]:
                index = -1
                for i in range(len(CATALOG[author][year])):
                    if name == CATALOG[author][year][i]:
                        index = i

                if index > -1:
                    del CATALOG[author][year][index]
                print("Book deleted!")

                if len(CATALOG[author][year]) == 0:
                    del CATALOG[author][year]
            else:
                print("There is nothing to delete! There was no such book on the list.")

    elif author in CATALOG and year not in CATALOG:
        # Adding year and name
        if operation == "adding" or operation == "add":
            CATALOG[author][year] = [name]
            print("Book is added!")

        # Year removal
        if operation == "remove" or operation == "rm":
            print("There is nothing to delete! There was no such book on the list.")

    # Adding author with name of the book
    else:
        CATALOG[author] = {year: [name]}
        print("NEW: Author and BooK is added!")

    # Insert to file
    with open("catalog.json", "w") as file:
        json.dump(CATALOG, file)
    return None


def search(book: str) -> None:
    """
    Функция поиска книг в библиотеке, поддерживает возможность поиска по автору, году, названию
    :param book: str
    :return: None
    """
    global CATALOG
    with open("catalog.json", "r") as file:
        CATALOG = json.load(file)

    txt_link = ".txt"  # переменная для открытия файла с текстом
    # вытаскивание автора, названия и года
    book = book.split(", ")

    # проверка нахождения книги в библиотеке
    if len(book) == 3:
        name = book[0]
        author = book[1]
        year = book[2]
        if author in CATALOG and year in CATALOG[author]:
            if name in CATALOG[author][year]:
                print("Есть такая книга!")
                txt_link = name + txt_link
            else:
                print("Данного произведения этого автора в библиотеке нет")
        elif year not in CATALOG[author]:
            print("В этом году данного произведения не было")
        else:
            print("Нет такого автора в библиотеке")

    elif len(book) == 1:
        # вывод всех произведений писателя
        if "." in book[0]:
            author = book[0]
            if author in CATALOG:
                for year in CATALOG[author]:
                    print(year)
                    for i in range(len(CATALOG[author][year])):
                        print(f"{i+1}. {CATALOG[author][year][i]}")
            else:
                print("Такого автора нет")

        # поиск всех произведений по году
        elif book[0].isdigit():
            year = book[0]
            flag = False
            for author in CATALOG:
                if year in CATALOG[author]:
                    flag = True
                    print(f"{author} в {year} написал:")
                    for i in CATALOG[author][year]:
                        print(i)
                    print()
            if not flag:
                print("В таком году произведений нет ни у одного автора.")

        # поиск автора и года по названию произведения
        else:
            name = book[0]
            author = None
            year = None
            for pisatel, chislo in CATALOG.items():
                for chislo, story in CATALOG[pisatel].items():
                    if name in CATALOG[pisatel][chislo]:
                        author = pisatel
                        year = chislo
                        break
            if author and year is not None:
                print(f"{name}, {author}, {year}")
                txt_link = name + txt_link
            else:
                print("Видимо, нет такого произведения в нашей библиотеке.")

    # поиск по автору и году, вывод всех произведений
    elif len(book) == 2:
        author = book[0]
        year = book[1]
        if author in CATALOG and year in CATALOG[author]:
            for i in CATALOG[author][year]:
                print(i)
        else:
            print("В этом году автор ничего не написал.")

    else:
        print("Нет такой книги в библиотеке")

    # открытие файла
    if txt_link != ".txt":
        print("Открыть книгу? (yes/no)")
        open_perem = command_()
        if open_perem == "yes":
            subprocess.Popen(["gedit", txt_link])

    return None


def run() -> None:
    """
    Выбор и запуск программ
    :return: None
    """

    global COMMAND
    while True:
        print("---------")
        print("Что будем делать?\nИскать книгу: find\nДобавить или удалить: act\nВыход: ext")
        command_()
        if COMMAND == "find":
            print("Введите название, автора и/или год:")
            command_()
            search(COMMAND)
        elif COMMAND == "act":
            print("Введите название книги:")
            act_kn = command_()
            print("Что нужно сделать, добавить (add) или удалить (del)?")
            command_()
            add_or_rm(act_kn, COMMAND)
        elif COMMAND == "ext":
            return None
        else:
            print("Введено не верно")


if __name__ == "__main__":
    # kn_a_g = "Ya vas lubil, Pushkin A.S., 1829"
    # op = "del"
    # dobavlenie_udalenie(kn_a_g)
    # console_vvod()
    # poisk_knigi(kn_a_g)
    run()

