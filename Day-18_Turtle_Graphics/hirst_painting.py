from turtle import Turtle , Screen
import random
import colorgram
turtle = Turtle()
color_list = []

turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
turtle.goto(-200,-100)

screen = Screen()
screen.colormode(255)
colours = colorgram.extract('image.jpg', 50)

for color in colours:
    color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

for i in range(10):
    for j in range (10):
        turtle.pendown()
        turtle.dot(10,random.choice(color_list))
        turtle.penup()
        turtle.forward(30)
    if(i%2==0):
        turtle.left(90)
    else:
        turtle.right(90)
    turtle.forward(30)
    if (i % 2 == 0):
        turtle.left(90)
    else:
        turtle.right(90)

screen.exitonclick()
