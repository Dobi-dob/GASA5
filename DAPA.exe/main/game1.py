import turtle
from pygame import mixer
from random import randint
import time
from os import startfile

mixer.init()
mixer.music.load("DAPA.exe\\sound\\cashier.mp3")

root = turtle.Screen()
root.setup(600, 600)
root.bgpic("DAPA.exe\\textures\\baseplate.png")
root.title("")
# если в настройках была включена музыка, она включается
with open("DAPA.exe\\main\\sound_stat.txt") as sound:
    if sound.read():
        mixer.music.play(-1)

# создание и первичная настройка черепашек
turtles = {
    "player": turtle.Turtle(),
    "target": turtle.Turtle(shape="circle", visible=False),
    "cashier": turtle.Turtle(visible=False),
}
for item in "player", "cashier":
    turtles[item].pu()
    root.register_shape(item, f"DAPA.exe\\textures\\{item}.png")
    turtles[item].shape(item)
    turtles[item].speed(0)
turtles["target"].pu()
turtles["target"].speed(0)
turtles["target"].color("orange")
turtles["target"].shapesize(5)

target_timer, cashier_timer = 5000, 3000


def move(direction):
    directions = {"up": 90, "fd": 0, "bd": 180, "down": 270}
    if (
        abs(turtles["player"].xcor()) + 127 < 400
        and abs(turtles["player"].ycor()) + 127 < 400
    ):
        turtles["player"].seth(directions[direction])
        turtles["player"].fd(5)
    else:
        turtles["player"].goto(randint(-200, 200), randint(-200, 200))


# если кассир опускается за 0.8 секунд - окончить игру
def check():
    if cashier_timer == 800:
        win()
        return False
    return True


def win():
    root.clearscreen()
    mixer.music.pause()
    mixer.music.load("DAPA.exe\\sound\\win.mp3")
    mixer.music.play()
    turtle.ht()
    turtle.colormode(255)
    for i in range(100):
        turtle.color(
            255 - randint(i, 200), 255 - randint(i, 200), 255 - randint(i, 200)
        )
        turtle.write(
            "УРАА! Кассир устал, а ты забрал чипсы себе! Хорошая концовка!",
            font=("Comic Sans MS", 13),
            align="center",
        )
    turtle.bye()


def game_2():
    root.title("п̴̫͙̙́̀̚ӧ̸̦̦́͘͝п̴͔͚͇͊͑͌а̴̢̢͕͛̈́͘л̸͎͕͋͋с̵͖͍̞͒͒͋я̴̡̡̟͆̽͝п̸̺͚̈́̓̈́͜о̵̢͚̠̒͝п̴̢̘͔̽͌̚а̵͓̙̀͒͠л̵͙͇̒͌с̴͓̦͔͋̈́͠я̵͕͎͙͋͋̚")
    time.sleep(2)
    startfile("DAPA.exe\\main\\game2.exe")
    turtle.bye()


def grab(new_x, new_y):
    if (
        abs(turtles["player"].xcor() - new_x) <= 120
        and abs(turtles["player"].ycor() - new_y) <= 158
    ):
        mixer.music.pause()
        mixer.music.load("DAPA.exe\\sound\\oof.mp3")
        mixer.music.play()
        time.sleep(1)
        root.clearscreen()
        root.bgcolor("black")
        game_2()


def attack(new_x, new_y):
    global cashier_timer, target_timer
    duration = 1
    start = time.time()
    turtles["target"].ht()
    turtles["cashier"].goto(new_x, new_y)
    turtles["cashier"].st()
    while time.time() - start < duration:
        grab(new_x, new_y)
        time.sleep(0.1)
    turtles["cashier"].ht()
    cashier_timer -= 200
    target_timer -= 200
    turtle.ontimer(targ, target_timer)


def targ():
    if check():
        new_x, new_y = randint(
            int(turtles["player"].xcor()) - 20, int(turtles["player"].xcor()) + 50
        ), randint(int(turtles["player"].ycor()), int(turtles["player"].ycor()) + 50)
        turtles["target"].goto(new_x, new_y)
        turtles["target"].st()
        turtle.ontimer(lambda: attack(new_x, new_y), cashier_timer)


def keypress(event):
    if event.char in ("w", "W", "ц", "Ц"):
        move("up")
    if event.char in ("a", "A", "ф", "Ф"):
        move("bd")
    if event.char in ("s", "S", "ы", "Ы"):
        move("down")
    if event.char in ("d", "D", "в", "В"):
        move("fd")


root.listen()
canvas = root.getcanvas()
canvas.bind('<KeyPress>', keypress)
turtle.ontimer(targ, target_timer)
turtle.done()
