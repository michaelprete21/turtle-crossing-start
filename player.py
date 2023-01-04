from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)
        self.shapesize(1.5, 1.5)

    def move_up(self):
        self.forward(50)



