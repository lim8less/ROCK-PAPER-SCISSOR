import random
from tkinter import *
root = Tk()

photo1 = PhotoImage(file = r"ROCK.png")
photoimage1 = photo1.subsample(10, 10)
photo2 = PhotoImage(file = r"PAPER.png")
photoimage2 = photo2.subsample(10, 10)
photo3 = PhotoImage(file = r"SCISSOR.png")
photoimage3 = photo3.subsample(15, 15)

def myclick1():
    p1 = 1
    p2 = random.randint(1, 3)
    if p2 == 1:
        result.config(text='ROCK DRAWS ROCK', bg='yellow')
        result.place(x=550, y=250)
    elif p2 == 2:
        result.config(text='ROCK LOSES PAPER', bg='red')
        result.place(x=550, y=250)
    else:
        result.config(text='ROCK BEATS SCISSOR', bg='green')
        result.place(x=550, y=250)

def myclick2():
    p1 = 2
    p2 = random.randint(1, 3)
    if p2 == 1:
        result.config(text='PAPER BEATS ROCK', bg='green')
        result.place(x=550, y=250)
    elif p2 == 2:
        result.config(text='PAPER DRAWS PAPER', bg='yellow')
        result.place(x=550, y=250)
    else:
        result.config(text='PAPER LOSES SCISSOR', bg='red')
        result.place(x=550, y=250)

def myclick3():
    p1 = 3
    p2 = random.randint(1, 3)
    if p2 == 1:
        result.config(text='SCISSOR LOSES ROCK', bg='red')
        result.place(x=550, y=250)
    elif p2 == 2:
        result.config(text='SCISSOR BEATS PAPER', bg='green')
        result.place(x=550, y=250)
    else:
        result.config(text='SCISSOR DRAWS SCISSORS', bg='yellow')
        result.place(x=550, y=250)

root.geometry('100x100')
btn = Button(root, text='ROCK', image=photoimage1,
                    compound=LEFT, command=myclick1, padx=100, pady=60, borderwidth=5, relief='solid')
btn.place(x=100, y=20)

btn2 = Button(root, text='PAPER', image=photoimage2,
                    compound=LEFT, command=myclick2, padx=100, pady=60, borderwidth=5, relief='solid')
btn2.place(x=100, y=220)

btn3 = Button(root, text='SCISSOR', image=photoimage3,
                    compound=LEFT, command=myclick3, padx=98, pady=60, borderwidth=5, relief='solid')
btn3.place(x=99, y=450)

result = Label(root, font='Aerial', width=80, height=4, borderwidth=5, relief='solid')
result.place(x=550, y=250)
root.mainloop()
