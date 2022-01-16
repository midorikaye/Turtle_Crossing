FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.up()
        self.goto(-200, 260)
        self.write(f"LEVEL: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.boardupdate()

    def boardupdate(self):
        self.clear()
        self.write(f"LEVEL: {self.score}", False, align=ALIGNMENT, font=FONT)

    def addscore(self):
        self.score += 1
        self.boardupdate()

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER!Score = {self.score}", False, align=ALIGNMENT, font=FONT)