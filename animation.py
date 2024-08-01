from tkinter import *
from ball import *
import time
window = Tk()

Width = 500
Height =500

canvas = Canvas(window,width=Width,height= Height)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,'white')
tennis_ball = Ball(canvas,0,0,50,4,3,'red')
basket_ball = Ball(canvas,0,0,125,8,7,'blue')
while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)
window.mainloop()