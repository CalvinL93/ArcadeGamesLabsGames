import pygame
import random

class Rectangle():
    def __init__(self):
        self.x_coord = random.randrange(0, 700)
        self.y_coord = random.randrange(0, 500)
        self.height = random.randrange(20, 70)
        self.width = random.randrange(20, 70)
        self.change_x = random.randrange(-3, 3)
        self.change_y = random.randrange(-3, 3)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

    def drawRectangle(self, screen):
        pygame.draw.rect(screen, self.color, [self.x_coord, self.y_coord, self.height, self.width])

    def move(self):
        self.x_coord += self.change_x
        self.y_coord += self.change_y

class Ellipse(Rectangle):
    def __init__(self):
        super().__init__()
    def drawEllipse(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x_coord, self.y_coord, self.height, self.width])
    def move(self):
        self.x_coord += self.change_x
        self.y_coord += self.change_y

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []
for i in range(1000):
    my_list.append(Rectangle())
for i in range(1000):
    my_list.append(Ellipse())

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for i in range(1000):
        Rectangle.drawRectangle(my_list[i], screen)
        Ellipse.drawEllipse(my_list[i + 1000], screen)
        # Rectangle.move(my_list[i])
        # Ellipse.move(my_list[i + 10])
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()