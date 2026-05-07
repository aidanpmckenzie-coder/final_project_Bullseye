# Aidan McKenzie
# Computer Programming
# Period 5
# Final Project - Archery

# Imports
import turtle
import random
import math
from button import Button

# Screen
display_screen = "menu"
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")

# Turtle Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# Game Stats (While Playing game)
player = 1 # player 1's turn
arrows = 5 # each player gets 5 arrows
wind_x = 0 # x coordinate to aim for
wind_y = 0 # y coordinate to aim for



# Main Menu
start_button = Button(0, 20, "START", pen)
info_button = Button(0, -40, "INFO", pen)
def draw_menu():
    pen.clear()
    pen.goto(0, 100)
    pen.write("ARCHERY", align="center", font=("Arial", 24))
    start_button.draw()
    info_button.draw()


# Archery Board Rings (Colors & radius)
FIRST_RING_COLOR = "white"
SECOND_RING_COLOR = "black"
THIRD_RING_COLOR = "blue"
FOURTH_RING_COLOR= "red"
BULLSEYE_RING_COLOR = "yellow"

FIRST_RING_RADIUS = 100
SECOND_RING_RADIUS = 80
THIRD_RING_RADIUS = 60
FOURTH_RING_RADIUS = 40
BULLSEYE_RING_RADIUS = 20

# Arrow on Screen (shot taken)
ARROW_SHOT_RADIUS = 8
ARROW_SHOT = "green"

# Archery Board (Game Screen)
def draw_archery_board():
    pen.clear()
    colors = [FIRST_RING_COLOR, SECOND_RING_COLOR, THIRD_RING_COLOR, FOURTH_RING_COLOR, BULLSEYE_RING_COLOR]
    sizes = [FIRST_RING_RADIUS, SECOND_RING_RADIUS, THIRD_RING_RADIUS, FOURTH_RING_RADIUS, BULLSEYE_RING_RADIUS]
    for i in range(5):
        pen.goto(0, -sizes[i])
        pen.color(colors[i])
        pen.begin_fill()
        pen.circle(sizes[i])
        pen.end_fill()
    pen.color("black")

# Wind (The wind recommends the coordinate that the player should aim at, changes after each shot)
def wind():
    global wind_x, wind_y
    wind_x = random.randint(-200,200)
    wind_y = random.randint(-200,200)

    # Preventing easy shots 
    while -10 < wind_x < 10 and -10 < wind_y < 10:
        wind_x = random.randint(-200,200)
        wind_y = random.randint(-200,200)


# Game Text
def draw_text():
    # Player (1 for now)
    pen.goto(-220, 220)
    pen.write(f"Player: {player}",font=("Arial", 12))

    # Arrows (Maximum 5)
    pen.goto(140, 220)
    pen.write(f"Arrows: {arrows}",font=("Arial", 12))

    # Wind
    pen.goto(-80, -230)
    pen.write(f"Wind: ({wind_x}, {wind_y})",font=("Arial", 12))


# Information (Information Screen)
def draw_info():
    pen.clear()
    # How to Play 
    pen.goto(0, 125)
    pen.write("How to Play", align="center",font=("Arial", 20))
    pen.goto(0, 80)
    pen.write("Welcome to Archery! The rules of the game are simple, rack up points by hitting a ring on the archery board.", align="center", font=("Arial", 14))
    pen.goto(0,60)
    pen.write("Hitting the board will get you points, and points increase the closer you are to the bullseye", align="center", font=("Arial", 14))
    pen.goto(0,40)
    pen.write("However, it is not as simple as just clicking on the bullseye, as wind will play a factor in this challenge.", align="center", font=("Arial", 14))
    pen.goto(0,20)
    pen.write("The game consists of 2 players, the player with the most points after each player runs out of arrows, wins!", align="center", font=("Arial", 14))
    pen.goto(0,-20)
    # Start the Game
    pen.write("Click anywhere on the screen to begin!", align="center", font=("Arial", 14))


# Play the Game (Shooting)
def shoot(x,y):
    # Shooting using the wind (corrects shot)
    x -= wind_x
    y -= wind_y

    # Draw shot on the screen
    pen.goto(x, y)
    pen.dot(ARROW_SHOT_RADIUS, ARROW_SHOT)


# Clicking function
# This function determines which screen will be displayed to the user after clicking a certain button or action
# For the game, it determines what will appear on the screen after the player interacts with the game
def click(x, y):
    global display_screen
    # Main Menu
    if display_screen == "menu":
        if start_button.clicked(x, y):
            display_screen = "game"
            pen.clear()
            wind()
            draw_archery_board()
            draw_text()

        elif info_button.clicked(x, y):
            display_screen = "info"
            draw_info()

    # Information screen
    elif display_screen == "info":
        display_screen = "game"
        draw_archery_board()

    # Begin the Game
    elif display_screen == "game":
        shoot(x,y)

# Running
screen.onclick(click)
draw_menu()
turtle.done()