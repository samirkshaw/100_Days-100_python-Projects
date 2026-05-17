from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self  ):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.color("blue")
        self.refresh()

    def refresh(self):
        x_coordinate = random.randint(-290, 290)
        y_coordinate = random.randint(-290, 290)
        self.goto(x_coordinate, y_coordinate)
