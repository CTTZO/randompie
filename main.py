from tkinter import *

window = Tk()
window.title("image")
canvas = Canvas(window)
canvas.pack()
canvas.create_polygon(100, 100, 200, 30, 300, 50, fill="yellow")
canvas.create_polygon(300, 50, 300, 75, 100, 125, 100, 100, 300, 50, fill="gold")
window.mainloop()
