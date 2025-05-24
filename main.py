# pong made with turtle
import turtle
import time
import random

amount_of_balls = 2  # Number of balls in the game

# Set up the screen
window = turtle.Screen()
window.title("Pong by erik")
window.bgcolor("black")
window.setup(width=800, height=600)
# window.tracer(0)  # Turns off the screen updates

def setupPlayer(player, x):
    player.speed(0)  # max speed
    player.shape("square")
    player.color("white")
    player.shapesize(stretch_wid=6, stretch_len=1)
    player.penup()
    player.goto(x, 0)

# Player 1
player1 = turtle.Turtle()
setupPlayer(player1, -350)

# Player 2
player2 = turtle.Turtle()
setupPlayer(player2, 350)

# Ball
def ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = random.randint(3,6)  # Ball speed in x direction
    ball.dy = random.randint(3,6)  # Ball speed in y direction
    return ball
balls = [ball() for _ in range(amount_of_balls)]

# Functions to move players
def up(player):
    y = player.ycor()
    if y < 250:  # Prevent moving out of bounds
        player.sety(y + 20)
def down(player):
    y = player.ycor()
    if y > -240:  # Prevent moving out of bounds
        player.sety(y - 20)

# Keyboard bindings
window.listen()
window.onkeypress(lambda: up(player1), "w")
window.onkeypress(lambda: down(player1), "s")
window.onkeypress(lambda: up(player2), "Up")
window.onkeypress(lambda: down(player2), "Down")


# Main game loop
last_time = time.time_ns()
def game_loop():
    global last_time
    # Move the ball using deltatime
    for ball in balls:
        ball.goto(ball.xcor() + ball.dx*((time.time_ns()-last_time)/20000000), ball.ycor() + ball.dy*((time.time_ns()-last_time)/20000000))

        # Ceiling and floor collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1  # Reverse the y direction
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1 # Reverse the y direction
        
        # Paddle collision
        if (330 < ball.xcor() < 350) and (player2.ycor() - 75 < ball.ycor() < player2.ycor() + 75):
            ball.setx(330)
            ball.dx *= -1  # Reverse the x direction
        if (-350 < ball.xcor() < -330) and (player1.ycor() - 75 < ball.ycor() < player1.ycor() + 75):
            ball.setx(-330)
            ball.dx *= -1
        # Out of bounds
        if ball.xcor() > 390:
            ball.goto(0, 0)  # Reset the ball position
            ball.dx *= -1  # Reverse the x direction
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1

    last_time = time.time_ns()
    window.update()
    window.ontimer(game_loop, 10)  # Call again after 10 ms

game_loop()
window.mainloop()