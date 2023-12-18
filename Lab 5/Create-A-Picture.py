# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653
 
# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Christmas Tree")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill([173, 114, 114]) # 59, 188, 235

    # Floor
    pygame.draw.rect(screen, [43, 25, 3], [0, 350, 400, 150])
    for x_offset in range(0, 400, 15):
        pygame.draw.line(screen, BLACK, [0 + x_offset, 350], [0 + x_offset, 500])
        # yLine = random.randrange(350, 500)
        # pygame.draw.line(screen, BLACK, [0 + x_offset, yLine], [15 + x_offset, yLine])
    
    # Wall
    pygame.draw.rect(screen, [183, 184, 154], [0, 340, 400, 10])

    # Window
    pygame.draw.rect(screen, BLACK, [255, 150, 115, 110])
    # pygame.draw.arc(screen, WHITE, [170, 230, 600, 100], PI * (2/3), PI * (3/4))
    pygame.draw.arc(screen, WHITE, [170, 230, 600, 100], 1.932, 2.36, 18)
    pygame.draw.rect(screen, [183, 184, 154], [250, 250, 125, 10])
    pygame.draw.rect(screen, [183, 184, 154], [255, 150, 115, 110], 5)
    pygame.draw.line(screen, [183, 184, 154], [312.5, 250], [312.5, 150])
    pygame.draw.line(screen, [183, 184, 154], [255, 202.5], [365, 202.5])

    # Rug Under Tree
    pygame.draw.ellipse(screen, RED, [100, 375, 200, 75], 0)
    pygame.draw.ellipse(screen, WHITE, [100, 375, 200, 75], 5)
    pygame.draw.ellipse(screen, BLACK, [100, 375, 200, 75], 1)

    # Tree & Stump
    pygame.draw.polygon(screen, GREEN, [[200,115], [150,200],[250,200]], 0)
    pygame.draw.polygon(screen, GREEN, [[200,150], [125,285],[275,285]], 0)
    pygame.draw.polygon(screen, GREEN, [[200,200], [100,375],[300,375]], 0)
    pygame.draw.rect(screen, [74,44,15], [180, 375, 40, 40], 0)

    # Tree Star
    pygame.draw.polygon(screen, [232, 221, 2], [[180, 125], [200, 114], [200, 100]], 0)
    pygame.draw.polygon(screen, [232, 221, 2], [[220, 125], [200, 114], [200, 100]], 0)
    pygame.draw.polygon(screen, [232, 221, 2], [[220, 95], [200, 110], [200, 98]], 0)
    pygame.draw.polygon(screen, [232, 221, 2], [[180, 95], [200, 110], [200, 98]], 0)
    pygame.draw.polygon(screen, [232, 221, 2], [[200, 78], [192, 110], [208, 110]], 0)

    # Ornaments
    pygame.draw.circle(screen, RED, [230, 200], 8)
    pygame.draw.circle(screen, BLUE, [188, 168], 8)
    pygame.draw.circle(screen, [43, 138, 34], [161, 254], 8)
    pygame.draw.circle(screen, [96, 19, 110], [280, 360], 8)
    pygame.draw.circle(screen, RED, [170, 322], 8)
    pygame.draw.circle(screen, BLUE, [220, 300], 8)
    pygame.draw.circle(screen, [251, 255, 5], [119, 355], 8)
    pygame.draw.circle(screen, [251, 255, 5], [260, 274], 8)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()