import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)
 
pygame.init()

# Set the width and height of the screen [width, height]
size = (255, 255)
screen = pygame.display.set_mode(size)

# for later use on differet screen sizes
# resized_screen = pygame.transform.scale(screen, (windoWidth,windowHeight)) 
# window.blit(resized_screen, (0, 0)

WIDTH = 20
HEIGHT = 20
MARGIN = 5

# Left click on mouse, right click on mouse
LEFT = 1
RIGHT = 3

font = pygame.font.SysFont('Calibri', 25, True, False)

# --- Create grid of numbers
# Create an empty list
grid = []
# Loop for each row
for row in range(10):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(10):
        # Add a the number zero to the current row
        grid[row].append(0)

# Create mines
mines = 0
i = 0
while i < 10:
#for i in range(10):
    x = random.randrange(0,10)
    y = random.randrange(0,10)
    if grid[x][y] != 10:
        grid[x][y] = 10
        mines += 1
        i += 1
    else:
        i -= 1

# Add numbers to surrounding bomb locations
for row in range(10):
    for column in range(10):
        if grid[row][column] >= 10:
            if row < 9 and not grid[row + 1][column] == 10:
                grid[row + 1][column] += 1
            if column < 9 and not grid[row][column + 1] == 10:
                grid[row][column + 1] += 1
            if row > 0 and not grid[row - 1][column] == 10:
                grid[row - 1][column] += 1
            if column > 0 and not grid[row][column - 1] == 10:
                grid[row][column - 1] += 1
            if row < 9 and column < 9 and not grid[row + 1][column + 1] == 10:
                grid[row + 1][column + 1] += 1
            if row < 9 and column > 0 and not grid[row + 1][column - 1] == 10:
                grid[row + 1][column - 1] += 1
            if row > 0 and column < 9 and not grid[row - 1][column + 1] == 10:
                grid[row - 1][column + 1] += 1
            if row > 0 and column > 0 and not grid[row - 1][column - 1] == 10:
                grid[row - 1][column - 1] += 1

# Display grid in console
for row in range(10):
    for column in range(10):
        print(grid[row][column], end=" ") 
    print()

# Find a location with no bomb for game start
for row in range(10):
    for column in range(10):
        if grid[row][column] == 0:
            xSafe = row
            ySafe = column

pygame.display.set_caption("My Game")

revealed = 0

# Function to reveal surrounding squares
def check_adjacent_cells(x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if x + i >= 0 and y + j >= 0 and x + i <= 9 and y + j <= 9:
                if grid[x + i][y + j] == 0:
                    grid[x + i][y + j] = 9
                    check_adjacent_cells(x + i, y + j)
                    #revealed += 1
                if grid[x + i][y + j] > 0 and grid[x + i][y + j] < 9:
                    grid[x + i][y + j] *= -1
                    #revealed += 1       

# Loop until the user clicks the close button.
done = False
mineCount = 10
down = False
left = False
right = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    x = xSafe
    y = ySafe
    down = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Click Down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            y = pos[0] // 25
            x = pos[1] // 25
            down = True
            if event.button == LEFT:
                left = True
            if event.button == RIGHT:
                right = True

            # grid[x][y] += 50


        # Left Click Up
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT and not right:
            pos = pygame.mouse.get_pos()
            y = pos[0] // 25
            x = pos[1] // 25
            print("Click: (%s,%s) Value: %s"%(x,y,grid[x][y]))
            left = False

            # If left click on bomb game over
            if grid[x][y] == 10:
                print("Game Over")
                done = True
            
            # If next to bomb make number negative to later check and reveal
            elif grid[x][y] > 0 and grid[x][y] < 9:
                grid[x][y] *= -1
                xSafe = x
                ySafe = y
            
            # If square is empty reveal surrounding empty squares
            elif grid[x][y] == 0:
                grid[x][y] = 9
                xSafe = x
                ySafe = y
                check_adjacent_cells(x, y)

        # Right Click
        elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT and not left:
            pos = pygame.mouse.get_pos()
            y = pos[0] // 25
            x = pos[1] // 25
            print("Bomb Marked")
            right = False

            # Mark only squares that are unrevaled as possible bomb locations
            if grid[x][y] == 10:
                grid[x][y] = 20
            elif grid[x][y] < 9 and grid[x][y] > 0:
                grid[x][y] += 10
            elif grid[x][y] == 20:
                grid[x][y] = 10
            elif grid[x][y] < 20 and grid[x][y] > 10:
                grid[x][y] -= 10

           # Both Left and Right Click
        elif event.type == pygame.MOUSEBUTTONUP and left and right:
            pos = pygame.mouse.get_pos()
            y = pos[0] // 25
            x = pos[1] // 25
            right = False
            left = False

            # If both click revealed tile reveal surrounding tiles even if one is a bomb
            if grid[x][y] < 0:
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if x + i >= 0 and y + j >= 0 and x + i <= 9 and y + j <= 9:
                            if grid[x + i][y + j] == 10:
                                print("Game Over")
                                done = True
                            elif grid[x + i][y + j] == 0:
                                check_adjacent_cells(x, y)
                            elif grid[x + i][y + j] > 0 and grid[x + i][y + j] < 9:
                                grid[x + i][y + j] *= -1

            

            
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Game logic should go here

    text = ""
    
    # If all mines found end game
    if (100 - mines) == revealed:
        print("You Win")
        pygame.time.wait(5000)
        done = True
        
    print(revealed)
    
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    
 
    # --- Drawing code should go here
    revealed = 0
    
    for row in range(10):
        for column in range(10):
            color = (170, 170, 170)

            if grid[row][column] >= 50:
                color = (0,0,0)

            # Change background to white for all empty squares that have been clicked on
            if grid[row][column] == 9 :
                color = WHITE
                revealed += 1

            # Flag possible bomb location
            if grid[row][column] > 10:
                color = RED
            
            # Change background to white if square has been clicked on
            if grid[row][column] < 0:
                color = WHITE
                revealed += 1

            # Draw grid
            pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
            
            # Ouputs number in box if it is negative indicating it is next to a bomb and has been clicked on
            if grid[row][column] < 0:
                text = font.render(str(abs(grid[row][column])), True, BLACK)
                text_rect = text.get_rect(center=((column * 25) + WIDTH // 2 + 5, (row * 25) + HEIGHT // 2 + 5))
                screen.blit(text, text_rect)
    
    # if down == True:
        

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 10 frames per second
    clock.tick(10)
 
# Close the window and quit.
pygame.quit()