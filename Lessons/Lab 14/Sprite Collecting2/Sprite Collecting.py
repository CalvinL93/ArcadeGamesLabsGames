import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y



class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class GoodBlock(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += random.randrange(-3,4)
        self.rect.y += random.randrange(-3,4)

class BadBlock(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        
        if self.rect.y > 400:
            self.rect.y = -5
            self.rect.x += random.randrange(-20, 20)
            if self.rect.x > 700:
                self.rect.x -= 40
            if self.rect.x < 0:
                self.rect.x += 40

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block1 = GoodBlock(GREEN, 20, 15)
    block2 = BadBlock(RED, 20, 15)
 
    # Set a random location for the block
    block1.rect.x = random.randrange(screen_width)
    block1.rect.y = random.randrange(screen_height)
    block2.rect.x = random.randrange(screen_width)
    block2.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    good_block_list.add(block1)
    all_sprites_list.add(block1)
    bad_block_list.add(block2)
    all_sprites_list.add(block2)
 
# Create a RED player block
player = Player(20, 15)
all_sprites_list.add(player)

good_sound = pygame.mixer.Sound("Lessons/Lab 13/Sprite Collecting/good_block.wav")
bad_sound = pygame.mixer.Sound("Lessons/Lab 13/Sprite Collecting/bad_block.wav")
border_sound = pygame.mixer.Sound("Lessons/Lab 13/Sprite Collecting/bump.wav")
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # Clear the screen
    screen.fill(WHITE)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    if pos[0] < 685 and pos[0] > 0:
        player.rect.x = pos[0]
    if pos[0] >= 685:
        player.rect.x = 685
        # border_sound.play()
    if pos[0] <= 0:
        player.rect.x = 0
        # border_sound.play()
    if pos[1] < 385 and pos[1] > 0:
        player.rect.y = pos[1]
    if pos[1] >= 385:
        player.rect.y = 385
        # border_sound.play()
    if pos[1] <= 0:
        player.rect.y = 0
        # border_sound.play()
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        bad_sound.play()
        # print(score)

    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)

    for block in blocks_hit_list:
        score -= 1
        good_sound.play()
        # print(score)

    # Output score to screen
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(str(score),True,BLACK)
    screen.blit(text, [5, 5])

    # Draw all the spites
    all_sprites_list.draw(screen)
    all_sprites_list.update()
    # good_block_list.update()
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()