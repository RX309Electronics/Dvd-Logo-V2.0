from random import randint
import pygame
pygame.init()

# Define the running variable
running = True

# Pygame Window settings
Window_SIZE = width, height = 800, 600  # Resolution. (4:3)!
BG_COLOR = (0, 0, 0)  # Background color in RGB
screen = None  # Initialize screen later based on fullscreen status
fullscreen = False  # Fullscreen

# Configure The Logo size and image
dvd_logo = pygame.image.load('DVD-LOGO.png')
dvd_logo = pygame.transform.scale(dvd_logo, (100, 100))
img_size = dvd_logo.get_rect().size

# Configure the clock variable
clock = pygame.time.Clock()

# Set the name of the window
pygame.display.set_caption('DVD Corner')

# Set initial position and speeds
x = randint(0, width-8)
y = randint(0, height-6)
x_speed = 2.0
y_speed = 2.0

# Function to move the logo
def move(x, y):
    screen.blit(dvd_logo, (x, y))

# Main game loop

while running:
    if screen is None:
        # Initialize the display surface based on fullscreen status
        if fullscreen == True:
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            pygame.mouse.set_visible(False)
        else:
            screen = pygame.display.set_mode(Window_SIZE)
    
    screen.fill(BG_COLOR)
    
    # Adjust maximum movement range based on screen size
    max_x = width if not fullscreen else screen.get_width()
    max_y = height if not fullscreen else screen.get_height()
    
    if (x + img_size[0] >= max_x) or (x <= 0):
        x_speed = -x_speed
    if (y + img_size[1] >= max_y) or (y <= 0):
        y_speed = -y_speed
    
    x += x_speed   
    y += y_speed   
    move(x, y)     
    pygame.display.update() # Constantly update the display frames
    clock.tick(60)  # Define the clock speed of the game

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                # Toggle fullscreen mode
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    pygame.mouse.set_visible(False)
                else:
                    screen = pygame.display.set_mode(Window_SIZE)

pygame.quit()
