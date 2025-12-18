from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Manage the player turtle and movement."""

    def __init__(self):
        """Initialize the player."""
        super().__init__()
        self.create_player()

    def create_player(self):
        """Set up the player turtle."""
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        """Move the player forward."""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Reset position if finish line reached."""
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
