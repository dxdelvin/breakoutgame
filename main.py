import random
import turtle
import  math
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
    turtle.tracer(0, 0)
    Dash.forward(speed*30)
    turtle.tracer(1, 1)


def left_move():
    turtle.tracer(0, 0)
    Dash.backward(speed*30)
    turtle.tracer(1, 1)







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
ball.penup()
ball.shape("circle")
ball.color("white")
ball.right(90)




def check_border_collision():
    screen_width = s.window_width() // 2 - 50
    screen_height = s.window_height() // 2- 50
    if Dash.ycor() -50 < ball.ycor() < Dash.ycor() + 50:
        if Dash.ycor() - 50 < ball.ycor():
            ball.setheading(random.randint(89,150))
        else:
            ball.setheading(random.randint(45,90))

    if ball.ycor() > screen_height or ball.ycor() < -screen_height:
        ball.setheading(360-ball.heading())

    if ball.xcor() > screen_width or ball.xcor() < -screen_width:
        ball.setheading(180-ball.heading())


def move_forward():
    turtle.tracer(0, 0)
    ball.forward(30)
    check_border_collision()
    turtle.tracer(1, 1)

    s.ontimer(move_forward, 90)







screen_width = turtle.window_width() // 2
screen_height = turtle.window_height() // 2
move_forward()




# Border







s.onkey(right_move,"d")
s.onkey(left_move,"a")






turtle.update()
s.listen()
s.mainloop()