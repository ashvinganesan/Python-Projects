from tkinter import *
import random
import time

score = 0

class Player:
    def __init__(self):
        self.score = 0
    def inc_score(self):
        self.score = self.score + 1
    def get_score(self):
        return self.score

class Ball:
    def __init__(self, canvas, paddle, player, color):
        self.canvas = canvas
        self.paddle = paddle
        self.player = player
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.start = False
        self.canvas.bind_all("<Button-1>", self.start_moving)
    def start_moving(self, evt):
        self.start = True
    
        
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <+ paddle_pos[3]:
                self.player.inc_score()
                return True
        return False

    def draw(self):
        if self.start:
            self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self,evt):
        self.x = -2
    def turn_right(self,evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id,self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
            
        


tk = Tk()
tk.title("Bounce Game!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

new_player = Player()
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, new_player, 'red')




while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if ball.hit_bottom == True:
        canvas.create_text(250, 170, text = "Game Over", font=('Times', 40))
        canvas.create_text(250, 200, text = "Your Score was " + str(new_player.get_score()) + "!",  font=('Times', 40))
        break




        
    
