from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk,width = 400, height = 400)
canvas.pack()

colors = ['red', 'green', 'blue', 'orange', 'pink', 'purple', 'yellow']

for x in range (0,600, 20):
    randomcolors = random.choice(colors)
    canvas.create_polygon(10 + x , 10 + x, 10 + x, 60 + x, 50 + x, 35 + x, fill = randomcolors)



