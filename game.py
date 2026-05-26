import turtle
import time

# Screen
wn = turtle.Screen()
wn.title("Simple Brick Breaker")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)



# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()

# Score
score = 0
paused = False
game_started = False

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)

title = turtle.Turtle()
title.hideturtle()
title.color("orange")
title.penup()
title.goto(0, 50)
title.write("BRICK BREAKER", align="center", font=("Arial", 28, "bold"))

instructions = turtle.Turtle()
instructions.hideturtle()
instructions.color("white")
instructions.penup()
instructions.goto(0, -20)
instructions.write("Press SPACE to Start\nLeft/Right to Move\nP = Pause | R = Restart",
                   align="center", font=("Arial", 14, "normal"))


pause_text = turtle.Turtle()
pause_text.hideturtle()
pause_text.color("yellow")
pause_text.penup()
pause_text.goto(0, 0)

# Bricks list
bricks = [] 

# Functions

def start_game():
    global game_started
    game_started = True
    title.clear()
    instructions.clear()
       
def update_score():
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

def create_bricks():
    bricks.clear()
    for x in [-200, -100, 0, 100, 200]:
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color("blue")
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(x, 200)
        bricks.append(brick)

def reset_game():
    global score, game_over

    # Reset ball
    ball.goto(0, 0)
    ball.dx = 1.8
    ball.dy = 1.8

    # Reset paddle
    paddle.goto(0, -250)

    # Reset score
    score = 0
    update_score()

    # Remove old bricks
    for brick in bricks:
        brick.hideturtle()

    create_bricks()

    game_over = False
    pen.goto(0, 260)



# Initial setup
ball.dx = 1.8
ball.dy = 1.8
create_bricks()
update_score()

# Controls
def move_left():
    paddle.setx(paddle.xcor() - 30)

def move_right():
    paddle.setx(paddle.xcor() + 30)

def toggle_pause():
    global paused
    paused = not paused
    if paused:
       
        pause_text.write("PAUSED", align="center", font=("Arial", 20, "bold"))
    else:
        pause_text.clear()

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(reset_game, "r")  # 🔁 Restart key
wn.onkeypress(toggle_pause, "p")  # ⏸️ Pause key
wn.onkeypress(start_game, "space")  # ▶️ Start key

# Game loop
game_over = False

while True:
    wn.update()
    time.sleep(0.01)

    if  game_started and not game_over and not paused:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Wall bounce
        if ball.xcor() > 290 or ball.xcor() < -290:
            ball.dx *= -1
            

        if ball.ycor() > 290:
            ball.dy *= -1
           

        # Paddle collision
        if (ball.ycor() < -230 and ball.ycor() > -250) and \
           (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
            ball.dy *= -1
           


        # Brick collision
        for brick in bricks:
            if brick.distance(ball) < 30:

                brick.color("yellow")
                wn.update()
                time.sleep(0.01)
               
                
                brick.hideturtle()
                bricks.remove(brick)
                ball.dy *= -1
                

                score += 1
                update_score()
                break

        # Game over
        if ball.ycor() < -300:
            pen.goto(0, 0)
            pen.write("GAME OVER\nPress R to Restart", align="center", font=("Arial", 18, "bold"))
            game_over = True

        # Win
        if len(bricks) == 0:
            pen.goto(0, 0)
            pen.write("YOU WIN!\nPress R to Restart", align="center", font=("Arial", 18, "bold"))
            game_over = True

turtle.done()         