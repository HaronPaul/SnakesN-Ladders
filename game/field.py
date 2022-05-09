import pygame
import numpy as np
import os
from game.constants import VIOLET, YELLOW, BLACK, ROWS, COLS, SQUARE_SIZE
from game.powerUp import PowerUp

# This function creates the field that contains the snake tiles, ladder tiles,
# and power-up and power-downs tiles. This returns a matrix.
# 1 -> Ladder
# -1 -> Snake
# 0 -> Normal Tile
# 2 -> Power=up tile
def generateField(powerUps):
    # List for the snake tiles and ladder tiles
    snakeTiles = [(7,9), (5,6), (4,4), (2,7), (1,1)]
    ladderTiles = [(9,1), (7,8), (5,2), (3,2), (2,9)]

    # Generate the field as a matrix filled with zeros
    field = np.zeros([10,10], dtype=int)

    # Fill the snake tile with -1
    for tile in snakeTiles:
        field[tile[0]][tile[1]] = -1
    
    # Fill the ladder tile with 1
    for tile in ladderTiles:
        field[tile[0]][tile[1]] = 1

    # Generate power up tiles
    powerUpFileNames = ['plus1.png', 'plus2.png', 'plus3.png', 'minus1.png', 'minus2.png', 'minus3.png']
    powerUpNumbers = [-3,-2,-1,1,2,3]
    i = 0
    # 6 power ups in total
    while i < 6:
        powerUpRow = np.random.randint(0,10)
        powerUpColumn = np.random.randint(0,10)

        # Check if randomized tile is already a snake/ladder or if it is on number1 tile
        if field[powerUpRow][powerUpColumn] != 0 or (powerUpRow == 9 and powerUpColumn == 0):
            continue
        field[powerUpRow][powerUpColumn] = 2
        
        # Details of the powerup
        picPath = os.path.join(os.path.dirname(__file__), '..', 'assets', f"{powerUpFileNames[i]}") # Import the image using its path
        
        # Type of power-up, either plus or minus
        if powerUpNumbers[i] > 0: powerUpType = 'Plus'
        else: powerUpType = 'Minus'

        # Pixel location of the power-up
        powerUpLocationX = SQUARE_SIZE*powerUpColumn
        powerUpLocationY =  SQUARE_SIZE*powerUpRow

        # Add a new instance of power up to the powerUps list
        powerUps.append(PowerUp(picPath, powerUpType, powerUpNumbers[i], powerUpRow, powerUpColumn, powerUpLocationX, powerUpLocationY))
        i += 1
    print(field)

class Field:
    # Constructor for creating a Field instance
    def __init__(self):
        self.powerUps = []  # This list contains the tiles for the powerUps
        generateField(self.powerUps)    # Generate the field containing snakes, ladders, and power ups
        print(self.powerUps)


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
                # Draw the rectangle on Win using color and dimensions
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

        # Draw the power-ups as a group
        powerUpGroups = pygame.sprite.Group()
        for p in self.powerUps:
            powerUpGroups.add(p)
        powerUpGroups.draw(win)
