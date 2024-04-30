from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as highest:
            self.high_score = int(highest.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False,"center",
                   font=("Arial",15,"normal"))
        self.hideturtle()

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center",
                   font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as highest:
                highest.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center",
                   font=("Arial", 15, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, "center", font=("Arial", 15, "bold"))
