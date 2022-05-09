# To install pygame, simply use the command 'pip install pygame'
from dataclasses import field
import pygame
from game.constants import WIDTH, HEIGHT
from game.field import Field

pygame.init()

# Set the window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snakes N\' Ladders')

# Frame rate for the game
FPS = 60
clock = pygame.time.Clock()

def main():
    field = Field()

    # Call the draw_squares function of the field instance  
    field.draw_squares(WIN)
    clock.tick(FPS)
    run = True

    while run:

        # Loop through all the events happening
        # May be a mouse click/key press
        for event in pygame.event.get():

            # When user clicks the close button of the window
            # equate run to False
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()

