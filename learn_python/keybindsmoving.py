from tkinter import *
import time



tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
def movetriangleright(event):
    canvas.move(1, 5, 0)
canvas.bind_all('<KeyPress-Right>', movetriangleright)
def movetriangleleft(event):
    canvas.move(1, -5, 0)
canvas.bind_all('<KeyPress-Left>', movetriangleleft)

def movetriangleup(event):
    canvas.move(1, 0, -5)
canvas.bind_all('<KeyPress-Up>', movetriangleup)
    
def movetriangledown(event):
    canvas.move(1, 0, 5)
canvas.bind_all('<KeyPress-Down>', movetriangledown)
    
