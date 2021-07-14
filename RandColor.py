import random
from tkinter import *
import tkinter.font as tkf

window = Tk()
window.title("Color")
canvas = Canvas(window)
canvas.pack()

labelfont = tkf.Font(family="serif", size=7)
title = Label(text="HEX Values (Press C To Generate) The top of the pie is the color:", bg="black", bd=0, fg="white", font="serif")
title.pack()

cl = ["grey", "cyan", "lime", "yellow", "pink"]


def rectmake(event):
    r = random.randint(0, 3)
    hex_value = 0
    if r == 1:
        hex_value = "#" + str(random.randint(99, 999))
    if r == 2:
        hex_value = "#" + str(random.randint(99999, 999999))
    else:
        hex_value = "#" + str(random.randint(99999999, 999999999))
    hex_value = hex_value.replace("1", "F")
    hex_value = hex_value.replace("5", "A")
    hex_value = hex_value.replace("3", "D")
    canvas.create_polygon(100, 100, 200, 30, 300, 50, fill=hex_value)
    canvas.create_polygon(300, 50, 300, 75, 100, 125, 100, 100, 300, 50, fill=cl[random.randint(-1, 4)])
    label = Label(text=hex_value, bg="black", bd=0, fg="white", font=labelfont)
    label.pack()
    return


rectmake(0)
canvas.bind_all("c", rectmake)
window.mainloop()
