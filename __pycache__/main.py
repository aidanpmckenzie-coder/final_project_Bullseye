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
SCREEN_BACKGROUND_COLOR = "linen"
display_screen = "menu"
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)

# Turtle Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# Game Stats (While Playing game)
player = 1 # player 1's turn
arrows = 10 # each player gets 5 arrows
wind_x = 0 # x coordinate to aim for
wind_y = 0 # y coordinate to aim for
player_one_score = 0
player_two_score = 0


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
OUTLINE_RING_COLOR = "black"
FIRST_RING_COLOR = "white"
SECOND_RING_COLOR = "black"
THIRD_RING_COLOR = "blue"
FOURTH_RING_COLOR= "red"
BULLSEYE_RING_COLOR = "yellow"

OUTLINE_RING_RADIUS = 100.6
FIRST_RING_RADIUS = 100
SECOND_RING_RADIUS = 80
THIRD_RING_RADIUS = 60
FOURTH_RING_RADIUS = 40
BULLSEYE_RING_RADIUS = 20

# Arrow on Screen (shot taken)
ARROW_SHOT_RADIUS = 8

# Archery Board (Game Screen)
def draw_archery_board():
    pen.clear()
    colors = [OUTLINE_RING_COLOR,FIRST_RING_COLOR, SECOND_RING_COLOR, THIRD_RING_COLOR, FOURTH_RING_COLOR, BULLSEYE_RING_COLOR]
    sizes = [OUTLINE_RING_RADIUS, FIRST_RING_RADIUS, SECOND_RING_RADIUS, THIRD_RING_RADIUS, FOURTH_RING_RADIUS, BULLSEYE_RING_RADIUS]
    for i in range(6):
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
    pen.goto(-220, 190)
    pen.write(f"Arrows: {arrows}",font=("Arial", 12))

    # Wind
    pen.goto(-80, -230)
    pen.write(f"Wind: ({wind_x}, {wind_y})",font=("Arial", 12))

    # Scores
    pen.goto(140, 220)
    pen.write(f"P1: {player_one_score}", font=("Arial", 12))

    pen.goto(140, 190)
    pen.write(f"P2: {player_two_score}", font=("Arial", 12))

# Score
def score(x,y):
    distance = math.dist((x, y), (0, 0))  # shot distance from bullseye center
    # Hits Bullseye
    if distance <= 20:
        return 10
    
    # Hits Fourth Ring 
    elif distance <= 40:
        return 8
    
    # Hits Third Ring 
    elif distance <= 60:
        return 6
    
    # Hits Second Ring 
    elif distance <= 80:
        return 4
    
    # Hits First Ring 
    elif distance <= 100:
        return 2
    
    # Does not Hit Archery Board
    else:
        return 0


# Information (Information Screen)
def draw_info():
    pen.clear()
    # How to Play 
    pen.goto(0, 190)
    pen.write("How to Play", align="center",font=("Arial", 20))
    pen.goto(0, 160)
    pen.write("Welcome to Archery! The rules of the game are simple, rack up points by hitting a ring on the archery board.", align="center", font=("Arial", 14))
    pen.goto(0,140)
    pen.write("Hitting the board will get you points, and points increase the closer you are to the bullseye", align="center", font=("Arial", 14))
    pen.goto(0,120)
    pen.write("However, it is not as simple as just clicking on the bullseye, as wind will play a factor in this challenge.", align="center", font=("Arial", 14))
    pen.goto(0,100)
    pen.write("The game consists of 2 players, the player with the most points after each player runs out of arrows, wins!", align="center", font=("Arial", 14))
    
    # Score Distribution
    pen.goto(0, 80)
    pen.write("Bullseye: 10 Points", align="center",font=("Arial", 12))
    pen.goto(0, 60)
    pen.write("Red: 8 Points", align="center",font=("Arial", 12))
    pen.goto(0, 40)
    pen.write("Blue: 6 points", align="center",font=("Arial", 12))
    pen.goto(0, 20)
    pen.write("Black: 4 points", align="center",font=("Arial", 12))
    pen.goto(0, 0)
    pen.write("White: 2 points", align="center",font=("Arial", 12))
    pen.goto(0, -20)
    pen.write("Miss: 0 Points", align="center",font=("Arial", 12))


    # Start the Game
    pen.goto(0,-70)
    pen.write("Click anywhere on the screen to begin!", align="center", font=("Arial", 14))

# Game Results
def draw_game_results():
    pen.clear()
    # Finding the Winner
    if player_one_score > player_two_score:
        result = "Player 1 Wins!"
    elif player_two_score > player_one_score:
        result = "Player 2 Wins!"
    else: 
        result = "Tie Game!"
    
    # Results Displayed
    pen.goto(0,80)
    pen.write(result,align="center",font=("Arial", 24))
    pen.goto(0,30)
    pen.write(f"P1: {player_one_score}   P2: {player_two_score}",align="center",font=("Arial", 16))

    # Return to Main Menu
    pen.goto(0, -50)
    pen.write("Click anywhere to return to menu!",align="center",font=("Arial", 12))


# Play the Game (Shooting)
def shoot(x,y):
    global player, arrows, player_one_score, player_two_score, display_screen

    # Shooting using the wind (corrects shot)
    x -= wind_x
    y -= wind_y

    # Player arrow shots appear on screen in different colors to indicate which player shot where
    if player == 1:
        shot_color = "green"

    else:
        shot_color = "magenta"

    # Draw shot on the screen
    pen.goto(x, y)
    pen.dot(ARROW_SHOT_RADIUS, shot_color)

    # Updating Points
    points = score(x,y)
    if player == 1:
        player_one_score += points
    else:
        player_two_score += points
    
    # Updating Game Stats after each shot
    arrows -= 1

    #alternate shots
    if player == 1:
        player = 2
    else: 
        player = 1

    # Update 
    wind()
    draw_text()

    # End the game
    if arrows == 0:
        display_screen = "game_over"
        draw_game_results()


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
        wind()
        draw_text()

    # Begin the Game
    elif display_screen == "game":
        shoot(x,y)

    # Game Results and Reset
    elif display_screen == "game_over":
        player = 1
        arrows = 10
        player_one_score = 0
        player_two_score = 0
        display_screen = "menu"
        draw_menu()


# Running
screen.onclick(click)
draw_menu()
turtle.done()