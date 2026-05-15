from turtle import Turtle , Screen
import random

screen = Screen()
screen.colormode(255)
roboo = Turtle()
roboo.shape("turtle")

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

roboo.speed("fastest")


for i in range(int(360/5)):
    roboo.color(random_colour())
    roboo.circle(100)
    roboo.setheading(roboo.heading()+5)



screen.exitonclick()





