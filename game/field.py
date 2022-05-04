import pygame
import numpy as np
import os
from game.constants import VIOLET, YELLOW, BLACK, ROWS, COLS, SQUARE_SIZE

class Field:
    # Constructor for creating a Field instance
    def __init__(self):
        print('Wew')

    
    # Function for drawing each squares, snakes, and ladders 
    # in the board
    def draw_squares(self, win):
        # Load ladder image files
        ladder1 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder1.png'))
        ladder2 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder2.png'))
        ladder3 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder3.png'))
        ladder4 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder4.png'))
        ladder5 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder5.png'))

        # Load snake image files
        snake1 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake1.png'))
        snake2 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake2.png'))
        snake3 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake3.png'))
        snake4 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake4.png'))
        snake5 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake5.png'))

        color1 = VIOLET  # Color variable alternates to yellow/violet
        color2 = YELLOW

        # Numbers on the leftmost tile
        leftNumbers = [100,81,80,61,60,41,40,21,20,1]
        
        myFont = pygame.font.SysFont('Arial', 20)

        for i in range(ROWS):
            # Get the number to the corresponding row. 1st row contains 100
            renderTile = leftNumbers[i]
            for j in range(COLS):
                # Draw the rectangle on win using color and dimensions
                if j%2 ==    0:
                    pygame.draw.rect(win, color1, (j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, color2, (j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                text = myFont.render(str(renderTile), True, BLACK)
                win.blit(text, (j*SQUARE_SIZE + 5, i*SQUARE_SIZE + 5))
                
                # Decrement or increment the text number on the tile depending on what row
                if(i % 2 == 0): renderTile -= 1
                else: renderTile +=1

            # Change the beginning color for the next row
            color1 = YELLOW if color1 == VIOLET else VIOLET
            color2 = VIOLET if color2 == YELLOW else YELLOW
        
        # Drawing snakes
        win.blit(snake1, (510,590))
        win.blit(snake2, (283,391))
        win.blit(snake3, (563,170))
        win.blit(snake4, (65,350))
        win.blit(snake5, (87,85))
        
        # Drawing ladders
        win.blit(ladder1, (100,500))
        win.blit(ladder2, (514,195))
        win.blit(ladder3, (25, 180))
        win.blit(ladder4, (177, 175))
        win.blit(ladder5, (656, 92))

        

       

      
