import pygame
 
# The use of the main function is described in Chapter 9.
 
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (105, 106, 107)

def draw_ship(screen, x, y):
    # Weapons
    pygame.draw.rect(screen, GRAY, [25, 40, 2, 12])
    pygame.draw.rect(screen, GRAY, [85, 40, 2, 12])
    pygame.draw.rect(screen, GRAY, [12, 48, 2, 12])
    pygame.draw.rect(screen, GRAY, [98, 48, 2, 12])

    # Body
    pygame.draw.polygon(screen, BLUE, [[55, 0], [20, 75], [90, 75]])
    pygame.draw.polygon(screen, BLUE, [[0, 65], [55, 65], [55, 30]])
    pygame.draw.polygon(screen, BLUE, [[110, 65], [55, 65], [55, 30]])
    pygame.draw.polygon(screen, BLACK, [[19, 75], [24, 66], [25,75]])
    pygame.draw.polygon(screen, BLACK, [[91, 75], [86, 66], [85, 75]])
    pygame.draw.line(screen, BLACK, [53, 15], [32, 62])
    pygame.draw.line(screen, BLACK, [57, 15], [78, 62])

    # Engine
    pygame.draw.rect(screen, GRAY, [38, 72, 10, 10])
    pygame.draw.polygon(screen, GRAY, [[34, 81], [38, 81], [38, 72]])
    pygame.draw.polygon(screen, GRAY, [[52, 81], [48, 81], [48, 72]])
    pygame.draw.rect(screen, GRAY, [62, 72, 10, 10])
    pygame.draw.polygon(screen, GRAY, [[58, 81], [62, 81], [62, 72]])
    pygame.draw.polygon(screen, GRAY, [[76, 81], [72, 81], [72, 72]])

    # Window
    pygame.draw.rect(screen, GRAY, [50, 43, 10, 20])
    pygame.draw.circle(screen, GRAY, [55, 43], 5)



def main():
    """ Main function for the game. """
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)

        draw_ship(screen, 0, 0)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
 
if __name__ == "__main__":
    main()
