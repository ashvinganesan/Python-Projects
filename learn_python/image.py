from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 1439, height = 899)
canvas.pack()
my_image = PhotoImage(file =  '/Users/ashvin/Desktop/test.gif')
canvas.create_image(0, 0 , anchor = NW, image = my_image)
