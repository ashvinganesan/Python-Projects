from tkinter import *

class H:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_polygon(10,10,25,25)
        return self.id
tk = Tk()
canvas = Canvas(tk, width = 500, height = 400)
canvas.pack()
tk.update()

b = H(canvas)
