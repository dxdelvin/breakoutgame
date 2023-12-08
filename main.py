import random
import turtle
# UI #
# Dash
# Colorful boxes
# Ball
# move the ball
#make borders
# collide the ball
# collide brick = destroy


from turtle import *

s = Screen()
s.title("Breakout Game")
s.bgcolor("black")

rectCors = ((10,-100),(10,100),(-10,100),(-10,-100));  # y,x rule (Refernence)
s.register_shape('Dash',rectCors);
rectCors = ((10,-20),(10,20),(-10,20),(-10,-20));  # y,x rule (Refernence)
s.register_shape('brick',rectCors)
speed = 1.5

turtle.tracer(0, 0)

Dash = Turtle()
Dash.shape("Dash")
Dash.color("white")
Dash.penup()
Dash.speed(0)
Dash.setpos(0, -270)
Dash.speed(1)



def right_move():
    Dash.forward(speed*30)

def left_move():
    Dash.backward(speed*30)






color = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "cyan"]

def create_box(color,x,y):
    for i in range(8):
        target_box = Turtle()
        target_box.shape("brick")
        target_box.color(random.choice(color))
        target_box.penup()
        target_box.speed(0)
        target_box.setpos(x=x+50,y=y)
        x = x+80





create_box(color,-350,250)
create_box(color,-350,200)
create_box(color,-350,150)






turtle.tracer(1,1)

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.right(90)

def move_forward():
    ball.forward(10)
    check_collision()
    s.ontimer(move_forward, 50)


def check_collision():
    distan = Dash.distance(ball)
    if distan < 50:
        ball.setheading(60)
    turtle.ontimer(check_collision, 100)



screen_width = turtle.window_width() // 2
screen_height = turtle.window_height() // 2
move_forward()


s.onkey(right_move,"d")
s.onkey(left_move,"a")






turtle.update()
s.listen()
s.mainloop()