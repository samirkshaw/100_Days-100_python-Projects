from turtle import Screen,Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() < 250:  # 300 - 50 (half paddle height)
            self.goto(self.xcor(), self.ycor() + 40)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 40)