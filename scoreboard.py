import turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.game_is_on = True
        self.point = 0
        self.setposition(0, 250)
        self.write(f"Points: {self.point}", False, align="center", font=FONT)

    def game_over(self):
        self.setposition(0,-250)
        self.write("Game Over", False, align="center", font=FONT)

    def update_scoreboard(self):
        self.point += 1
        self.setposition(0, 250)
        self.clear()
        self.write(f"Points: {self.point}", False, align="center", font=FONT)





