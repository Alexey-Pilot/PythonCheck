from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import functions


def main_window():
    def click1():
        messagebox.showinfo("", functions.read_all())

    def click2():
        functions.add_note(txt.get())
        messagebox.showinfo("Сообщение", "Заметка добавлена")
        combo["values"] = functions.get_date_list()

    def click3():
        messagebox.showinfo("", functions.find_note_by_date(combo.get()))

    window = Tk()
    window.geometry("1000x500")
    window.title("Добро пожаловать в заметки")
    lbl = Label(window, text="Выберите действие", font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Прочитать заметки", command=click1, fg="red", font=("Arial Bold", 20))
    btn.grid(column=0, row=1)
    txt = Entry(window, width=25)
    txt.grid(column=2, row=2)
    btn1 = Button(window, text="Добавить заметку", command=click2, fg="blue", font=("Arial Bold", 20))
    btn1.grid(column=0, row=2)
    btn2 = Button(window, text="Найти заметку", command=click3, fg="dark green", font=("Arial Bold", 20))
    btn2.grid(column=0, row=3)
    combo = Combobox(window, width=25)
    combo["values"] = functions.get_date_list()
    if not combo["values"]:
        combo["values"] = functions.get_date_list()
    combo.current()
    combo.grid(column=1, row=3)
    window.mainloop()
