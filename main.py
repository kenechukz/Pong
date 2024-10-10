
from paddle import Paddle
from turtle import Screen,Turtle
from ball import Ball
from scoreboard import Scoreboard
import turtle
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.tracer(0)

middle_line = Turtle('square')
SHAPESIZE = middle_line.shapesize(stretch_len=0.75,stretch_wid=0.3)
STARTING_POSITION = (0,0)
COLOUR = middle_line.color('white')
middle_line.pu()
MIDDLE_LINE_CORDINATE = middle_line.goto(0,-280)
middle_line.left(90)
middle_line.width(5)

for _ in range(20):
    middle_line.color('white')
    middle_line.stamp()
    middle_line.color('black')
    middle_line.forward(30)

ball = Ball()
p1 = Paddle()
p1.pu()
p1.goto(-350,0)
p1.left(90)
p2 = Paddle()
p2.pu()
p2.goto(350,0)
p2.left(90)
score = Scoreboard()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    screen.listen()
    # Player 1 Bindings
    screen.onkeypress(p1.up,'w')
    screen.onkeyrelease(p1.stop,'w')
    screen.onkeypress(p1.down,'s')
    screen.onkeyrelease(p1.stop,'s')

    # Player 2 Bindings
    screen.onkeypress(p2.up,'Up')
    screen.onkeypress(p2.down,'Down')
    print(ball.position())

    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(p2) < 50 and ball.xcor() > 320 or ball.distance(p1) < 50 and ball.xcor() < -320: 
        ball.bounce_x()
    
    # Return to starting position after paddle misses the ball and restart
    if ball.xcor() > 380:
        ball.reset_position()
        score.p1_point()
        score.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score.p2_point()
        score.update_score()




    






screen.exitonclick()