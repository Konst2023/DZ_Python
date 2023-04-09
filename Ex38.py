# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
from time import sleep
import json
import os

file_name = "phonebook.txt"


def pause():
    sleep(5)


def write_json(file_name, list_name):
    with open(file_name, "w", encoding="UTF-8") as jf:
        json.dump(list_name, jf, indent=4, ensure_ascii=False)


def read_json(file_name):
    with open(file_name, "r+", encoding="UTF-8") as read_file:
        out_list = json.load(read_file)
    return out_list


def find_id(phonebook_lst: list):
    """
    Ищем максимальный ID из:
    - ID записанных в базе
    - кол-ва записей в базе
    """
    max_id = 0

    for rec in phonebook_lst:
        if rec["ID"] > max_id:
            max_id = rec["ID"]

    max_id = max(max_id, len(phonebook_lst))
    return max_id + 1


def add_record(phonebook_lst: list):
    """
    Добавляем запись (словарь) в список
    """
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    phone_number = input("Номер телефона: ")
    dic_rec = {
        "ID": find_id(phonebook_lst),
        "Фамилия": surname,
        "Имя": name,
        "Отчество": patronymic,
        "Телефон": phone_number,
    }
    phonebook_lst.append(dic_rec)
    print("Запись добавлена!")


def edit_record(phonebook_lst: list):
    """
    Редактируем запись по введенному ID
    """
    id = int(input("ID: "))

    for rec in phonebook_lst:
        if rec["ID"] == id:
            print("Обновите данные:")
            rec["Фамилия"] = input("Фамилия: ")
            rec["Имя"] = input("Имя: ")
            rec["Отчество"] = input("Отчество: ")
            rec["Телефон"] = input("Номер телефона: ")
            break

    print("Запись обновлена!")


def del_record(phonebook_lst: list):
    """
    Удаляем запись по введенному ID
    """
    id = int(input("ID: "))

    for rec in phonebook_lst:
        if rec["ID"] == id:
            phonebook_lst.remove(rec)
            break

    print("Запись удалена!")


def search_by_surname(phonebook_lst: list):
    """
    Поиск записи по фамилии
    """
    surname = input("Фамилия: ")

    temp_list = list()
    for rec in phonebook_lst:
        if rec["Фамилия"] == surname:
            temp_list.append(rec)

    print("Найдены совпадения:")
    for rec in temp_list:
        print(rec)


def print_phonebook(phonebook_lst: list):
    for rec in phonebook_lst:
        print(rec)


choice_str = """
Выберите функцию:
1. Вывести справочник
2. Добавить запись
3. Найти запись
4. Изменить запись
5. Удалить запись
0. Выход
"""
file_is_empty = False
phonebook_lst = list()

# Проверка на существование файла
if not os.path.isfile(file_name):
    with open(file_name, "a+") as f:
        pass

# Проверка на заполненность файла
if os.stat(file_name).st_size > 0:
    phonebook_lst = read_json(file_name)
else:
    file_is_empty = True
# Основной цикл
while True:
    print(choice_str)
    try:
        choice = int(input("Ваш выбор: "))
    except:
        choice = 0

    match choice:
        case 1:  # Read
            if file_is_empty:
                print("Справочник пуст!")
            else:
                print_phonebook(phonebook_lst)
            pause()
        case 2:  # Add
            add_record(phonebook_lst)
            write_json(file_name, phonebook_lst)
            file_is_empty = False
            pause()
        case 3:  # Find
            search_by_surname(phonebook_lst)
            pause()
        case 4:  # Edit
            edit_record(phonebook_lst)
            write_json(file_name, phonebook_lst)
            pause()
        case 5:  # Delete
            del_record(phonebook_lst)
            write_json(file_name, phonebook_lst)
            pause()
        case 0:  # Exit
            print("Выход. Спасибо...")
            exit()
