import turtle
t = turtle.Pen()
t.reset


def my_triangle(size, rotation):
    for x in range(0,3):
        t.forward(size)
        if rotation == True:
            t.left(120)
        if rotation == False:
            t.right(120)
y = 200
t.up()
t.backward(200)
t.down()
for x in range (0,6):
    my_triangle(y * (1/2**x),True)
    t.forward((1/2**x*1/2) * y)
    t.left(120)
    my_triangle(((1/2**x) * 1/2) * y, False)
    t.right(120)



