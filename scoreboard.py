from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.count = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.count}   High Score: {self.high_score}", move=False, align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.count += 1
        self.update_scoreboard()

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode="w") as data:
                data.write(f"{self.count}")
        self.count = 0
        self.update_scoreboard()






