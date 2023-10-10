from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self, score=1):
        self.clear()
        self.score += score

        self.write(
            f"Score: {self.score}", align="center", font=("Courier", 24, "normal")
        )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
