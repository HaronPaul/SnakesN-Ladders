import random
from shutil import move
import pygame
from game.constants import SQUARE_SIZE, WIDTH


class Player():
    def __init__(self, image, playerNum, pos_X, pos_Y, field):
        self.image = image
        self.playerNum = playerNum
        self.rect = self.image.get_rect()
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]
        self.rect.center = ((pos_X+SQUARE_SIZE / 2),(pos_Y + SQUARE_SIZE / 2))
        self.inventory = []
        self.velX = 0
        self.velY = 0
        self.endX = 0
        self.endY = 0
        self.evenY = [0, 140, 280, 420, 560]
        self.oddY = [70, 210, 350, 490, 630]
        self.rolled = False
        self.field = field

        # Controllers for player movement
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        self.currentRow = 9
        self.currentCol = 0
        self.speed = 5
        self.rolledNumber = 0
        self.isMoving = False
        self.isWaiting = True

    def rollDice(self):
        self.rolled = True
        self.rolledNumber = random.randint(1,6)
        if(self.currentRow % 2 == 1):
            self.endX = self.rect.x + self.rolledNumber*SQUARE_SIZE
        else:
            self.endX = self.rect.x - self.rolledNumber*SQUARE_SIZE
        print('----------------')
        print(f'Start x is {self.rect.x}')
        print(f'End x is {self.endX}')
        print('----------------')

    def realign(self):
        x = self.rect.center[0]
        y = self.rect.center[1]
        pos_x = x // SQUARE_SIZE
        pos_y = y // SQUARE_SIZE
        self.currentCol = pos_x
        self.currentRow = pos_y
        self.rect.x = pos_x * SQUARE_SIZE
        self.rect.y = pos_y * SQUARE_SIZE
        self.aligned = False

    def draw(self, win):
        win.blit(self.image, self.rect)

    def stop(self):
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

    def checkTile(self):
        ladderStart = self.field.ladderStart
        ladderEnd = self.field.ladderEnd
        snakeStart = self.field.snakeStart
        snakeEnd = self.field.snakeEnd
        powerUpTiles = self.field.powerUps

        # Check if tile is ladder
        for i in range(len(ladderStart)):
            if (self.rect.x + self.width//2) in range(ladderStart[i][0], ladderStart[i][0]+SQUARE_SIZE) and (self.rect.y + self.height // 2) in range(ladderStart[i][1], ladderStart[i][1]+SQUARE_SIZE):
                self.endX = self.rect.x = ladderEnd[i][0]
                self.rect.y = ladderEnd[i][1]
                self.currentRow = ladderEnd[i][1] // SQUARE_SIZE
                self.currentCol = ladderEnd[i][0] // SQUARE_SIZE
                break
                
        # Check if tile is snake
        for i in range(len(snakeStart)):
             if (self.rect.x + self.width//2) in range(snakeStart[i][0], snakeStart[i][0]+SQUARE_SIZE) and (self.rect.y + self.height // 2) in range(snakeStart[i][1], snakeStart[i][1]+SQUARE_SIZE):
                self.endX = self.rect.x = snakeEnd[i][0]
                self.rect.y = snakeEnd[i][1]
                self.currentRow = snakeEnd[i][1] // SQUARE_SIZE
                self.currentCol = snakeEnd[i][0] // SQUARE_SIZE
                break
        
        # Check if tile is power-up
        for i in range(len(powerUpTiles)):
              if(self.rect.x + self.width//2) in range(powerUpTiles[i].pos[0], powerUpTiles[i].pos[0]+SQUARE_SIZE) and (self.rect.y + self.height // 2) in range(powerUpTiles[i].pos[1], powerUpTiles[i].pos[1]+SQUARE_SIZE):
                  if powerUpTiles[i].consumed == False:
                    powerUpTiles[i].consumed = True
                    self.inventory.append(powerUpTiles[i])

    def calculateJumpTile(self, keyPressed):
        index = 0
        if keyPressed == 49: index = 1
        elif keyPressed == 50: index = 2
        elif keyPressed == 51: index = 3
        print('Calculate the number of tiles to be moved here')

        if index > len(self.inventory):
            return

        powerUp = self.inventory[index-1]

        powerUpValue = powerUp.number
        movement = SQUARE_SIZE * powerUpValue
        print(f'Move to x = {self.rect.x + movement}')

        # Check what row is the player currently on
        nextX = 0

        # When player is in an odd-numbered row
        if self.currentRow % 2 == 1:
            nextX = self.rect.x + movement
            if nextX >= 700:
                excess = nextX - 700
                self.rect.y -= SQUARE_SIZE
                self.rect.x = 700 - (excess + SQUARE_SIZE)
            elif nextX <= 0:    
                excess = abs(nextX)
                self.rect.y += SQUARE_SIZE
                self.rect.x = excess - SQUARE_SIZE
            else:
                self.rect.x = nextX
            self.endX = self.rect.x
        
        else:
            nextX = self.rect.x - movement
            if nextX <= 0:
                excess = abs(nextX)
                self.rect.x = excess - SQUARE_SIZE
                self.rect.y -= SQUARE_SIZE
            elif nextX >= 700:
                excess = nextX - 700
                self.rect.y += SQUARE_SIZE
                self.rect.x = excess - SQUARE_SIZE
            else:
                self.rect.x = nextX
            self.endX = self.rect.x

        self.realign()

        # Remove the power-up in the inventory
        self.inventory.remove(powerUp)

    def update(self):
        self.isMoving = True
        self.velX = 0
        self.velY = 0
        if self.moveRight: self.velX = self.speed
        if self.moveLeft: self.velX = -self.speed
        if self.moveUp: self.velY = -self.speed
        if self.moveDown: self.velY = self.speed

        # Change direction if row is odd-numbered
        if self.currentRow % 2 == 1:
            self.moveUp = False
            self.moveLeft = False
            self.moveRight = True

            # if self.rect.y in self.evenY:
            for evenY in self.evenY:
                if self.rect.y in range(evenY, evenY+(SQUARE_SIZE//8)):
                    self.currentRow -= 1

                # Recalculate endX when changing rows
                    self.endX = 700 - (abs(self.endX - 700) + SQUARE_SIZE)
            if self.rect.x >= 9*SQUARE_SIZE - 5:
                self.moveUp = True
                self.moveRight = False
                
        # Change direction if row is even-numbered
        if self.currentRow % 2 == 0:
            self.moveUp = False
            self.moveRight = False
            self.moveLeft = True
            
            for oddY in self.oddY:
                if self.rect.y in range(oddY, oddY+(SQUARE_SIZE//8)):
                    self.currentRow -= 1
                    
                    # Recalculate endX when changing rows
                    self.endX = abs(self.endX - 0) - SQUARE_SIZE
            if self.rect.x <= 0:
                self.moveUp = True  
                self.moveLeft = False

        if self.currentRow % 2 == 1:
            if self.rect.x < self.endX:
                self.rect.x += self.velX
                self.rect.y += self.velY
            else:
                self.realign()
                if len(self.inventory) > 0 and self.isWaiting and self.rolled:
                    print('Waiting for power play')
                    self.aligned = True
                else:  
                    self.isMoving = False
                    return
        elif self.currentRow % 2 == 0:
            if self.rect.x > self.endX:
                self.rect.x += self.velX
                self.rect.y += self.velY
            else:
                self.realign()
                if len(self.inventory) > 0 and self.isWaiting and self.rolled:
                    print('Waiting for power play')
                    self.aligned = True
                else:                  
                    self.isMoving = False
                    return

        