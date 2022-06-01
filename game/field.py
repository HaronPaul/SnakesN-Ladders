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
    powerUpFileNames = ['minus3.png', 'minus2.png', 'minus1.png', 'plus1.png', 'plus2.png', 'plus3.png']
    powerUpNumbers = [-3,-2,-1,1,2,3]
    i = 0

    # 6 power ups in total
    while i < 6:
        powerUpRow = np.random.randint(0,10)
        powerUpColumn = np.random.randint(0,10)

        # powerUpRow = 9
        # powerUpColumn = i+2

        # Check if randomized tile is already a snake/ladder or if it is on number1 tile
        if field[powerUpRow][powerUpColumn] != 0 or (powerUpRow == 9 and powerUpColumn == 0):
            continue
        field[powerUpRow][powerUpColumn] = 2
        
        # Details of the powerup
        # Path of the image
        picPath = os.path.join(os.path.dirname(__file__), '..', 'assets', f"{powerUpFileNames[i]}") 

        # Pixel location of the power-up
        powerUpLocationX = SQUARE_SIZE*powerUpColumn
        powerUpLocationY =  SQUARE_SIZE*powerUpRow

        # Add a new instance of power up to the powerUps list
        powerUps.append(PowerUp(picPath, powerUpNumbers[i], powerUpRow, powerUpColumn, powerUpLocationX, powerUpLocationY))
        i += 1
    print(field)

class Field:
    # Constructor for creating a Field instance
    def __init__(self):
        self.snakeStart = [(630, 490), (420, 350), (280, 280), (490,140), (70,70), (140, 0)]
        self.snakeEnd = [(420, 630), (350, 560), (70, 560), (630,280), (70, 350), (350,280)]
        self.ladderStart = [(210, 630), (0,490), (560,490), (140,350), (140,210), (630,140)]
        self.ladderEnd = [(280, 490), (70,420), (420,140), (280,140), (0,140), (560,70)]
        self.powerUps = []  # This list contains the tiles for the powerUps
        generateField(self.powerUps)    # Generate the field containing snakes, ladders, and power ups

    # Function for drawing each squares, snakes, and ladders 
    # in the board
    def draw_squares(self, win):
        # Load ladder image files
        ladder1 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder1.png'))
        ladder2 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder2.png'))
        ladder3 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder3.png'))
        ladder4 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder4.png'))
        ladder5 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder5.png'))
        ladder6 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ladder6.png'))

        # Load snake image files
        snake1 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake1.png'))
        snake2 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake2.png'))
        snake3 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake3.png'))
        snake4 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake4.png'))
        snake5 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake5.png'))
        snake6 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake6.png'))
        snake7 = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'snake7.png'))

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
        win.blit(snake1, (430,530))
        win.blit(snake2, (253,353))
        win.blit(snake3, (503,130))
        win.blit(snake4, (76,320))
        win.blit(snake5, (83,86))
        win.blit(snake6, (130,10))
        win.blit(snake7, (357,25))
        
        # Drawing ladders
        win.blit(ladder1, (250,490))
        win.blit(ladder2, (456,165))
        win.blit(ladder3, (25, 160))
        win.blit(ladder4, (165, 165))
        win.blit(ladder5, (580, 85))
        win.blit(ladder6, (25, 445))

        # Draw the power-ups as a group