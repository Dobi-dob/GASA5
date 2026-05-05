import turtle
import random
from PIL import Image
from pygame import mixer
from time import sleep

WORDLIST = [x.rstrip() for x in open("DAPA.exe\\main\\words.txt", encoding="UTF-8").readlines()]
SIZE = 100 # размер клетки
word = []
HALF = SIZE * (len(word) + 1) // 2 # половина окна: размер клетки умноженный на длину слова + 1 и поделённый на два
answer = ""
prev = [""]
score = 0
beats = 0 # кол-во ударов по кассиру
running = True # идёт ли игра?

background = Image.open("DAPA.exe\\textures\\forest.png")

mixer.init()
mixer.music.load("DAPA.exe\\sound\\forest.mp3")

with open("DAPA.exe\\main\\sound_stat.txt") as sound:
    if sound.read():
        mixer.music.play(-1)


# проверка на то, правильно ли введено слово
def check():
    global score
    if not word:
        if answer in WORDLIST:
            score += 1
            del WORDLIST[WORDLIST.index(answer)]
            new_game()
            say("success")
        else:
            say("loose")


# разброс букв
def rand(w):
    global HALF
    word_index = random.randint(0, len(WORDLIST) - 1)
    w_copy = list(WORDLIST[word_index])
    HALF = SIZE * (len(w_copy) + 1) // 2
    for _ in range(len(w_copy)):
        ltr = random.randint(0, len(w_copy) - 1)
        w.append(w_copy[ltr])
        del w_copy[ltr]
    return w


def field():
    t.clear()
    t.color("black", "white")
    t.goto(-(SIZE * len(word) // 2) - SIZE, SIZE // 2)
    for _ in range(len(word)):
        t.goto(t.xcor() + SIZE, SIZE // 2)
        with t.fill():
            for _ in range(4):
                t.down()
                t.fd(SIZE)
                t.right(90)
                t.up()


def letters():
    t.goto(-(SIZE * len(word) // 2) - SIZE * 0.6, SIZE // 2)
    for r in range(len(word)):
        t.goto(t.xcor() + SIZE, -(SIZE // 4))
        t.write(word[r], font=(None, 30))


# перевод экранных координатов в индекс списка
def indexes(x, y):
    r = int((x + HALF - (SIZE // 2 * (len(answer) + 1))) // SIZE)
    return r


def add(x, y):
    global answer
    r = indexes(x, y)
    answer += word[r]
    del word[r]
    field()
    letters()
    ans.clear()
    ans.write(answer, font=(None, 45), align="center")
    prev.append(answer)
    check()


def beat():
    global beats
    if beats < 3:
        new_game()
        say("beat")
        beats += 1


def cancel():
    global answer
    word.append(answer[-1])
    answer = str(prev[-2]) if len(prev) > 1 else str(prev[-1])
    del prev[-1]
    t.clear()
    ans.clear()
    field()
    letters()
    ans.write(answer, font=(None, 45), align="center")


def click(x, y):
    if x >= HALF - 118 and y >= 67:
        beat()
    elif y > -(SIZE // 2):
        add(x, y)
    else:
        cancel()


def say(mode):
    yes_or_no = random.choice((True, False))
    if yes_or_no:
        with open(f"DAPA.exe\\main\\phrases\\{mode}.txt", encoding="UTF-8") as saylist:
            phrases = [x.rstrip() for x in saylist.readlines()]
            phrase.clear()
            phr = random.choice(phrases)
            phrase.goto(HALF - 118 - len(phr) * 8, SIZE * 1.7)
            phrase.write(f"{phr}-", font=(None, 15), align="left")
            turtle.ontimer(phrase.clear, 2000)


def menu():
    for tur in ans, ret, t, scr, phrase:
        tur.clear()
        tur.ht()
        tur.pu()
    phrase.color("white")
    cashier.pu()
    cashier.goto(HALF - 67, SIZE * 1.3)
    ret.color("gray")
    ret.goto(0, -SIZE * 1.5)
    ret.write("Отмена", font=(None, 45), align="center")
    ans.color("green")
    ans.goto(0, SIZE)
    ans.write(answer, font=(None, 45), align="center")
    scr.goto(-HALF, SIZE * 1.5)
    scr.write(f"Счёт: {score}", font=(None, 35))


def clear():
    global answer
    answer = ""
    for _ in range(len(word)):
        del word[-1]
    for _ in range(len(prev) - 1):
        del prev[-1]


# изменение размера фона для правильного отображения
def modify_background(screen):
    res = background.resize((SIZE * (len(word) + 10), SIZE * 4))
    res.save("DAPA.exe\\textures\\forest_RESIZED.png")
    screen.bgpic("DAPA.exe\\textures\\forest_RESIZED.png")


def win():
    global running
    running = False
    turtle.clearscreen()
    turtle.setup(600, 300)
    mixer.music.pause()
    mixer.music.load("DAPA.exe\\sound\\neutral.mp3")
    mixer.music.play()
    turtle.ht()
    turtle.pu()
    turtle.color("orange")
    turtle.write(
        "Ты смог выбраться из леса, но без чипсов, и попа почему-то болит...",
        font=(None, 13),
        align="center",
    )
    turtle.goto(0, -16)
    turtle.write(
        "Нейтральная концовка.",
        font=(None, 13),
        align="center",
    )


def score_check():
    if score == 5:
        win()
        return False
    return True


def new_game():
    global HALF
    global word
    if score_check():
        clear()
        word = list(random.choice(WORDLIST))
        random.shuffle(word)
        HALF = SIZE * (len(word) + 1) // 2
        menu()
        sc = turtle.Screen()
        sc.setup(SIZE * (len(word) + 1), SIZE * 4)
        sc.title("Н̶̧̙͑͠а̵̧̦͉̒̊̂͠б҈̡̬̦҇̐е̴̛̥͍̽̍͢р̷̧̯͖̗̅̉̍̕и҈̡̳͕̫̎͠ 5̵̧̣͎͗͠ о̵̡͎̏̕ч҉̢̛͙̏̏к̸̢̗͔͐̐̚͞о̷̡͎̊͝в̸̨̙̭͇̑̄͡ и҈̘̗҇̐̇̑͢ о҉̢̛͎͙̈́̒͆н̷̧̛̥̤̏ т̶̨̛̩̦̩̈̍е҉҇͑͢ͅб̸̡̛̞͉͂̓ͅя҉̨͍̦̱͆̊͠ о҉͚̙͚҇͐͊̍͢т̵̢̜̗͗̕п̵̡̦͇͊̄̐͠ͅу̷̟̫҇̂͢с̵̡̥̳̂̈̿͠т҈̧͕̖̓̕и̵̨̲̍̔͡т҈̧̯̩҇̿.̵̢͍̃̏͠.̸̧͚͇͍͂̕.̴̢͓̱̊̽͠")
        modify_background(sc)
        sc.listen()
        sc.onclick(click, 1)
        field()
        letters()


def game_over():
    if running:
        turtle.clearscreen()
        turtle.setup(1000, 300)
        mixer.music.pause()
        mixer.music.load("DAPA.exe\\sound\\oof.mp3")
        mixer.music.play()
        turtle.bgcolor("black")
        turtle.pencolor("red")
        turtle.ht()
        sleep(1)
        turtle.write(
            "Кассир выебал тебя и убил. Плохая концовка.",
            font=(None, 27),
            align="center",
        )


turtle.register_shape("cashier", "DAPA.exe\\textures\\mini_cashier.png")
ans, ret, t, scr = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
cashier, phrase = turtle.Turtle(shape="cashier"), turtle.Turtle()
turtle.tracer(0)

turtle.ontimer(game_over, 90000)
new_game()
turtle.mainloop()