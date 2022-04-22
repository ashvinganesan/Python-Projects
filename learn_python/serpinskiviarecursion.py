import turtle

def draw_serpensky(level, size):
   for x in range(0, 3):
       t.forward(size)

       if level != 1:
           t.left(120)
           draw_serpensky(level - 1, size / 2)  # on exit points to the same direction as entry
           t.right(120)

       t.forward(size)
       t.right(120)  # on exit points to the same direction as entry
   

def draw_outer_triangle(size):
    t.left(60)
    t.forward(2*size)
    for x in range(0,3):
        t.right(120)
        t.forward(4*size)

# main section
t = turtle.Pen()
t.speed(0)
t.ht()

draw_serpensky(7,100)

draw_outer_triangle(100)




 
