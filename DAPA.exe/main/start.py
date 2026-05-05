import tkinter
import random
from pygame import mixer
import os

TITLES = [
    x.rstrip() for x in open("DAPA.exe\\main\\titles.txt", encoding="UTF-8").readlines()
]  # открытие файла с набором имён окна
title = random.choice(TITLES)  # выбор случайного имени окна

root = tkinter.Tk()
root.geometry("600x600")

# переменные для меню с настройками
plays = False  # играет ли сейчас музыка?
snd = tkinter.BooleanVar()  # включает музыку
snd.set(False)
fun = tkinter.BooleanVar()  # переменная с шуточной опцией: никак не влияет ни на что.
fun.set(True)

mixer.init()
mixer.music.load("DAPA.exe\\sound\\menu.mp3")


def sound():
    global plays
    if snd.get():
        if not plays:
            mixer.music.play(-1)
            plays = True
    else:
        plays = False
        mixer.music.pause()


def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()


def prologue():
    clear_frame()
    lbl3 = tkinter.Label(
        root,
        text="Пролог!",
        font=("Haettenschweiler", 50)
    ).pack()
    btn5 = tkinter.Button(
        root,
        text="Назад",
        width=10,
        height=2,
        font=("Rockwell"),
        bg="gray",
        fg="white",
        command=menu,
    ).place(x=520)
    txt = tkinter.Text(root, height = 15, width = 52)
    txt.insert(tkinter.END, '''Итак, ты - малолетний звездюк Плеер, и ты решил, что украсть чипсеке у Срассира - отличная идея!
Этот дебил как раз мирно спал в магазе. Идеальный момент, чтоб выкрасть чипсы, подумал ты...
Только вот выйдя из магазина обнаружилось, что вокруг тебя выросли стены, ты никуда не можешь идти. Кассир парит в воздухе!
Он что, собирается на тебя прыгать? ААА! Уворачивайся и не попадись! Иначе дядя Кассир в лес утащит!
Но если всё же попался, то можешь ещё спастись. Для этого за полторы минуты собери несколько слов! Сколько? Секрет!''')
    txt.pack()
    btn6 = tkinter.Button(
        root,
        text="Понял",
        width=20,
        height=2,
        font=("Rockwell"),
        bg="green",
        fg="white",
        command=start_game,
    ).pack()
    


def menu():
    sound()
    clear_frame()
    root.title(title)
    lbl = tkinter.Label(root, text="GASA 5", font=("Rockwell", 50)).pack()
    lbl1 = tkinter.Label(
        root,
        text="Cashier escape",
        font=("Rockwell Condensed", 50),
        fg="red",
        bg="black",
    ).pack()
    btn = tkinter.Button(
        root,
        text="Играть",
        width=20,
        height=2,
        font=("Rockwell"),
        bg="green",
        fg="white",
        command=prologue,
    ).pack(padx=210, pady=100)
    btn1 = tkinter.Button(
        root,
        text="Настройки",
        width=20,
        height=2,
        font=("Rockwell"),
        bg="gray",
        fg="white",
        command=settings,
    ).pack()


def settings():
    clear_frame()
    root.title("Настройки")
    btn2 = tkinter.Button(
        root,
        text="Назад",
        width=10,
        height=2,
        font=("Rockwell"),
        bg="gray",
        fg="white",
        command=menu,
    ).place(x=520)
    btn3 = tkinter.Checkbutton(
        root, text='Музыка в меню и игре (работает после нажатия "Назад", звуки останутся)', var=snd
    ).place(y=100)
    btn4 = tkinter.Checkbutton(
        root, text="Убить селфшипперов и фанатов к*шдамми", var=fun
    ).place(y=150)
    lbl2 = tkinter.Label(
        root,
        text="Версия 1.0.1",
        font=("Haettenschweiler", 30),
        fg="black",
    ).place(y=200)


def start_game():
    os.startfile("DAPA.exe\\main\\game1.exe")
    with open("DAPA.exe\\main\\sound_stat.txt", "w") as stat:
        if snd.get():
            stat.write("1")
        else:
            stat.write("")
    root.destroy()


menu()
root.mainloop()