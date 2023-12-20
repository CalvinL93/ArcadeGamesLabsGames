import pygame
import random
import block_library

class BadBlock(block_library.Block):
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