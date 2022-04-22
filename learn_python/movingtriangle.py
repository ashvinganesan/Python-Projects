from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width = 400, height = 400)
canvas.pack()
my_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill = 'red')

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move (my_triangle, 0, -5)
    elif event.keysym == 'Down':
        canvas.move (my_triangle, 0, 5)
    elif event.keysym == 'Left':
        canvas.move (my_triangle, -5, 0)
    else:
        canvas.move(my_triangle, 5, 0)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)





