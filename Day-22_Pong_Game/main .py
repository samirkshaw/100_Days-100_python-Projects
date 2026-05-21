from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle =Paddle((380 ,0))
l_paddle =Paddle((-380 ,0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.up ,"Up")
screen.onkey(r_paddle.down ,"Down")
screen.onkey(l_paddle.up ,"w")
screen.onkey(l_paddle.down ,"s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()
    if  ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 360 and ball.xcor() <= 380:
        ball.bounce_x()
        scoreboard.increase_score()

    if ball.distance(l_paddle) < 60 and ball.xcor() < -360 and ball.xcor() >= -380:
        ball.bounce_x()
        scoreboard.increase_score()
    if ball.xcor() < -400 or ball.xcor() > 400:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()