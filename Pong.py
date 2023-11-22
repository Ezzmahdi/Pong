import turtle

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SPEED = 0.7

# Define a class for the Paddle
class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()

        # Set the drawing speed of 'paddle_a' to the fastest (no animation)
        self.speed(0)
        self.shape("square")
        self.color("white")
        # Change the dimensions of the square to make it look like a paddle
        # 'stretch_wid' is the height (vertical stretch), and 'stretch_len' is the length (horizontal stretch)
        self.shapesize(stretch_wid=5, stretch_len=1)
        # Lift the pen so the turtle doesn't draw while moving
        self.penup()
        self.goto(x, y)

        
    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)


# Define a class for the Ball
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)

        # Create attributes 'dx' and 'dy' to represent the change in x and y coordinates
        # These attributes are used to control the ball's movement
        self.dx = BALL_SPEED  # Horizontal movement (right) by 2 units
        self.dy = BALL_SPEED  # Vertical movement (up) by 2 unit 


# Define a class for the Pong game
class PongGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title('Pong')
        self.window.bgcolor('black')
        self.window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        #tracer() is a function that controls the animation speed.
        #It takes one argument, which is the number of animation frames to skip before updating the display.
        self.window.tracer(0)
        #This means that every step or movement made by the turtle will be immediately displayed on the screen without any delay.

        self.paddle_a = Paddle(-350, 0)
        self.paddle_b = Paddle(350, 0)
        self.ball = Ball()
        
        self.score_a = 0
        self.score_b = 0

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.update_score()

        self.window.listen()
        self.window.onkeypress(self.paddle_a.move_up, "w")
        self.window.onkeypress(self.paddle_a.move_down, "s")
        self.window.onkeypress(self.paddle_b.move_up, "Up")
        self.window.onkeypress(self.paddle_b.move_down, "Down")

    def update_score(self):
        self.pen.clear()
        self.pen.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align="center", font=("Courier", 24, "normal"))

    def run(self):
        while True:
            self.window.update()
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Border checking
            if self.ball.ycor() > 290 or self.ball.ycor() < -290:
                self.ball.dy *= -1

            if self.ball.xcor() > 350:
                self.score_a += 1
                self.update_score()
                self.ball.dx *= -1

            if self.ball.xcor() < -350:
                self.score_b += 1
                self.update_score()
                self.ball.dx *= -1

            if self.ball.xcor() < -340 and self.paddle_a.ycor() + 50 > self.ball.ycor() > self.paddle_a.ycor() - 50:
                self.ball.dx *= -1

            if self.ball.xcor() > 340 and self.paddle_b.ycor() + 50 > self.ball.ycor() > self.paddle_b.ycor() - 50:
                self.ball.dx *= -1

if __name__ == "__main__":
    game = PongGame()
    game.run()