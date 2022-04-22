from tkinter import *
def hello():
    print('hello there')
    
tk = Tk()
btn = Button(tk,text="CLICK ME", command = hello)
btn.pack()


def person(name, width, height):
    if width == 1:
        foot = "foot"
    else:
        foot = "feet"
    if height == 1:
        feet = "foot"
    else:
        feet = "feet"
    print("%s is %s %s wide, %s %s tall" % (name, width, foot, height, feet))


