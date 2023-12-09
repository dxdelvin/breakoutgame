import random
import turtle

# UI #
# Dash
# Colorful boxes
# Ball
# move the ball
# make borders
# collide the ball
# collide brick = destroy :(


from turtle import *

s = Screen()
s.title("Breakout Game")
s.bgcolor("black")

rectCors = ((10, -100), (10, 100), (-10, 100), (-10, -100));  # y,x rule (Refernence)
s.register_shape('Dash', rectCors);
rectCors = ((10, -20), (10, 20), (-10, 20), (-10, -20));  # y,x rule (Refernence)
s.register_shape('brick', rectCors)
speed = 1.5

turtle.tracer(0, 0)

Dash = Turtle()
Dash.shape("Dash")
Dash.color("white")
Dash.penup()
Dash.speed(0)
Dash.setpos(0, -270)
Dash.speed(1)
turtle.update()


def right_move():
    turtle.tracer(0, 0)
    turtle.update()
    Dash.forward(speed * 30)
    turtle.tracer(1, 1)
    turtle.update()


def left_move():
    turtle.tracer(0, 0)
    turtle.update()
    Dash.backward(speed * 30)
    turtle.tracer(1, 1)
    turtle.update()


color = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "cyan"]


def create_box(colour, x, y):
    boxes = []
    for i in range(8):
        target_box = Turtle()
        target_box.shape("brick")
        target_box.color(random.choice(colour))
        target_box.penup()
        target_box.speed(0)
        target_box.setpos(x=x + 50, y=y)
        x = x + 80
        boxes.append(target_box)
    return boxes


bricks_row1 = create_box(color, -350, 250)
bricks_row2 = create_box(color, -350, 200)
bricks_row3 = create_box(color, -350, 150)

turtle.tracer(1, 1)

ball = Turtle()
ball.penup()
ball.shape("circle")
ball.color("white")
ball.right(90)
turtle.update()


def check_border_collision():
    screen_width = s.window_width() // 2 - 50
    screen_height = s.window_height() // 2 - 50
    if (Dash.ycor() - 15 < ball.ycor() < Dash.ycor() + 15) and (Dash.xcor() - 100 < ball.xcor() < Dash.xcor() + 100):
        if ball.xcor() > Dash.xcor():  # Moves to the right side and else is moving to the left side
            ball.setheading(random.randint(45, 90))
        else:
            ball.setheading(random.randint(91, 150))

    if ball.ycor() < -screen_height or score==25:
        write_game_over()
        turtle.tracer(0,0)

    if ball.ycor() > screen_height:
        ball.setheading(360 - ball.heading())

    if ball.xcor() > screen_width or ball.xcor() < -screen_width:
        ball.setheading(180 - ball.heading())


def brick_collision():
    global bricks_row1, bricks_row2, bricks_row3
    for brick in bricks_row1 + bricks_row2 + bricks_row3:
        if brick and (brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10) and \
                (brick.xcor() - 20 < ball.xcor() < brick.xcor() + 20):
            ball.setheading(-ball.heading())
            brick.penup()
            brick.goto(1000,1000)
            global score
            score += 1
            write_score()
            brick = None


def write_score():
    turtle.tracer(0, 0)
    turtle.clear()
    turtle.color('white')
    style = ('Courier', 30)
    turtle.penup()
    turtle.goto(0, 300)
    turtle.write(f'Score: {score}', font=style, align='center')
    turtle.hideturtle()
def write_game_over():
    turtle.tracer(0, 0)
    turtle.clear()
    turtle.color('white')
    style = ('Courier', 30)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write(f'Game Over\nYour Score: {score}', font=style, align='center')
    turtle.hideturtle()


def move_forward():
    turtle.tracer(0, 0)
    ball.forward(30)
    check_border_collision()
    brick_collision()

    turtle.update()
    turtle.tracer(1, 1)

    turtle.update()
    s.ontimer(move_forward, 100)


score = 0
move_forward()

s.onkey(right_move, "d")
s.onkey(left_move, "a")

turtle.update()
s.listen()
s.mainloop()
