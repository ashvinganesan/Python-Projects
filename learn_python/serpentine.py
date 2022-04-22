import turtle
NUM_LEVELS = 7
TOTAL_TRIANGLES = int(((3 ** NUM_LEVELS) -1)/2)

LEVEL_ONE_SIZE = 128

t = turtle.Pen()
t.speed(11)



def get_path(num):
    out = [num%3]
    while (num > 1):
        num = int((num + 1)/3)
        out.append(num%3)
    out.reverse()
    del(out[0])
    return out
    

def goto_position(num):
    path = get_path(num)
    print("Use %s to go to %s" % (path, num))
    size = LEVEL_ONE_SIZE
    t.up()
    for x in path:
        if x == 1: # go right
            t.forward(size)
            t.right(120)
            t.forward(size/2)
            t.left(120)
        elif x == 0: # go left
            t.right(120)
            t.forward(size/2)
            t.left(120)
        elif x == 2: # go up
            t.left(60)
            t.forward(size/2)
            t.right(60)
        else:
            print('This is an Internal Error')
        size = size/2
    t.down()
    return size
        
    

def draw_triangle(size):
    for _x in range(0,3):
        t.forward(size)
        t.right(120)


def goto_position_and_draw_triangle(num):
    draw_triangle(goto_position(num))
    t.up()
    t.home()
    t.down()

def draw_outer_triangle():
    t.left(60)
    t.up()
    t.backward(LEVEL_ONE_SIZE)
    t.down()
    for x in range (0,3):
        t.forward(LEVEL_ONE_SIZE * 2)
        t.right(120)
    t.home()


## main section

draw_outer_triangle()

for x in range(1,TOTAL_TRIANGLES + 1):
    goto_position_and_draw_triangle(x)
  
t.up()
t.forward(1000)
