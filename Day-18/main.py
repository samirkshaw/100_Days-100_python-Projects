from turtle import Turtle , Screen
import random


roboo = Turtle()
screen = Screen()

turtle.colormode(255)

def random_colour():
    r = random.randot(0,255)
    g = random.random(0,255)
    b = random.random(0,255)
    random_colour  = (r,g,b)
    return random_colour


directions = [0,90,180,270]
roboo.pensize(10)
roboo.speed("fastest")

for i in range(100):
    roboo.colour(random_colour)
    roboo.forward(30)
    roboo.setheading(random.choice(directions))

turtle.done()
