from datetime import datetime as dt, timedelta as td
from loremipsum import get_sentences
from random import randint


def create_note():
    date = dt(2010, 10, 20)
    with open("Note.txt", "w", encoding="UTF-8") as file:
        for _ in range(10):
            file.writelines(str(date) + "       " + " ".join(get_sentences(randint(1, 10))))
            file.writelines("\n\n")
            date = date + td(days=randint(1, 15), hours=randint(0, 23), minutes=randint(1, 59))


def add_note(text):
    try:
        date = dt.now()
        with open("Note.txt", "r+", encoding="UTF-8") as file:
            file.readlines()
            file.writelines(str(date) + "        " + text)
            file.writelines("\n\n")
            print("Новая запись добавленна")
    except(FileNotFoundError):
        create_note()
        add_note(text)


def find_note_by_date(date):
    try:
        with open("Note.txt", "r", encoding="UTF-8") as file:
            note_list = []
            flag = False
            for line in file:
                if line.startswith(str(date)):
                    note_list.append(line)
                    flag = True
            if flag is False:
                return "{date: %Y-%m-%d} нет заметок"
            return "\n".join(note_list)
    except(FileNotFoundError):
        return "Записи не найдены"


def read_all():
    try:
        with open("Note.txt", "r", encoding="UTF-8") as file:
            return file.readlines()
    except(FileNotFoundError):
        print("Записи не найдены")


def get_date_list():
    try:
        date_list = []
        with open("Note.txt", "r", encoding="UTF-8") as file:
            for line in file:
                date_list.append(line[:11])
        return tuple(set(date_list))
    except(FileNotFoundError):
        create_note()
        get_date_list()
