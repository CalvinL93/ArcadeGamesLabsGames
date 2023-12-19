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
    pygame.draw.rect(screen, GRAY, [25+x, 40+y, 2, 12])
    pygame.draw.rect(screen, GRAY, [85+x, 40+y, 2, 12])
    pygame.draw.rect(screen, GRAY, [12+x, 48+y, 2, 12])
    pygame.draw.rect(screen, GRAY, [98+x, 48+y, 2, 12])

    # Body
    pygame.draw.polygon(screen, BLUE, [[55+x, 0+y], [20+x, 75+y], [90+x, 75+y]])
    pygame.draw.polygon(screen, BLUE, [[0+x, 65+y], [55+x, 65+y], [55+x, 30+y]])
    pygame.draw.polygon(screen, BLUE, [[110+x, 65+y], [55+x, 65+y], [55+x, 30+y]])
    pygame.draw.polygon(screen, BLACK, [[19+x, 75+y], [24+x, 66+y], [25+x, 75+y]])
    pygame.draw.polygon(screen, BLACK, [[91+x, 75+y], [86+x, 66+y], [85+x, 75+y]])
    pygame.draw.line(screen, BLACK, [53+x, 15+y], [32+x, 62+y])
    pygame.draw.line(screen, BLACK, [57+x, 15+y], [78+x, 62+y])

    # Engine
    pygame.draw.rect(screen, GRAY, [38+x, 72+y, 10, 10])
    pygame.draw.polygon(screen, GRAY, [[34+x, 81+y], [38+x, 81+y], [38+x, 72+y]])
    pygame.draw.polygon(screen, GRAY, [[52+x, 81+y], [48+x, 81+y], [48+x, 72+y]])
    pygame.draw.rect(screen, GRAY, [62+x, 72+y, 10, 10])
    pygame.draw.polygon(screen, GRAY, [[58+x, 81+y], [62+x, 81+y], [62+x, 72+y]])
    pygame.draw.polygon(screen, GRAY, [[76+x, 81+y], [72+x, 81+y], [72+x, 72+y]])

    # Window
    pygame.draw.rect(screen, GRAY, [50+x, 43+y, 10, 20])
    pygame.draw.circle(screen, GRAY, [55+x, 43+y], 5)



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

    pygame.mouse.set_visible(False)

   # Speed in pixels per frame
    x_speed = 0
    y_speed = 0
    
    # Current position
    x_coord = 10
    y_coord = 10
 
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3
        
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        # Move the object according to the speed vector.
        if x_coord < 590 and x_coord > 0:            
            x_coord += x_speed
        elif x_coord >= 590:
            x_coord -= 1
        elif x_coord <= 0:
            x_coord += 1
        if y_coord < 419 and y_coord > 0:
            y_coord += y_speed
        elif y_coord >= 419:
            y_coord -= 1
        elif y_coord <= 0:
            y_coord += 1
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        
 
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)

        # With Keyboard arrow keys
        draw_ship(screen, x_coord, y_coord)

        # With mouse
        # draw_ship(screen, x, y)
        
 
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
