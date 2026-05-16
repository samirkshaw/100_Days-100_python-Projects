from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
n = int(input("How many turtles do you want to play the race?\n"))
racers = []
colors = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan", "brown", "white"]
gap = int(600/n)
height = int(-((n - 1) / 2) * gap)
i =0
for i in range(0,n):
    racer = Turtle(shape="turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(-380, height)
    height += gap
    racers.append(racer)

user_bet = screen.textinput("Make a bet", prompt= "Which turtle will win  the race ? Enter a color : ").lower()
is_on = True
while is_on:
    for racer in racers:
        if racer.xcor() > 380:
            winning_turtle = racer.pencolor()
            is_on = False
        racer.forward(random.randint(1,10))

if user_bet==winning_turtle:
    print(f"{winning_turtle} turtle won the race! You win!")
else:
    print(f"{winning_turtle} turtle won the race! You lose!")

screen.exitonclick()
