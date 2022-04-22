from tkinter import *
tk = Tk()
canvas = Canvas(tk,width = 800, height = 800)
canvas.pack()
my_image = PhotoImage(file =  '/Users/ashvin/Desktop/test.gif')
canvas.create_image(10, 10, anchor = NW, image = my_image)


def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move (1, 0, -5)
    elif event.keysym == 'Down':
        canvas.move (1, 0, 5)
    elif event.keysym == 'Left':
        canvas.move (1, -5, 0)
    else:
        canvas.move(1, 5, 0)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)







            
















