#pgzero

WIDTH = 200 # Window width
HEIGHT = 200 # Window height

TITLE = "Crystals" # Title for the game window
FPS = 30 # Number of frames per second

# Create a character here
blue = Actor('blue', (20, 20))
red = Actor('red', (180, 20))
yellow = Actor('yellow', (180, 180))
green = Actor('green', (20, 180))

def draw():
    screen.fill('white')
    blue.draw()
    red.draw()
    yellow.draw()
    green.draw()

def update(dt):
    # Write your code below
    blue.y = blue.y + 1
    blue.x = blue.x + 1
    yellow.y = yellow.y - 1
    yellow.x = yellow.x - 1
    green.y = green.y - 1
    green.x = green.x + 1
    red.y = red.y + 1
    red.x = red.x - 1
