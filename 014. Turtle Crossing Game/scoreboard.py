from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    """Manage the game scoreboard and level tracking."""

    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-260, y=260)
        self.update_level()

    def update_level(self):
        """Display the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase level by one."""
        self.level += 1
        self.update_level()

    def game_over(self):
        """Display game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
