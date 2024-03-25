from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.pencolor("white")
        self.score = 0
        self.hideturtle()
        self.update()

    def update(self):
        self.write(arg=f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
