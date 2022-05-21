import random
import pygame
import pygame.sprite as sprite
import pygame.rect as Rect
from game.constants import SQUARE_SIZE, WIDTH


class Player():
    def __init__(self, image, playerNum, pos_X, pos_Y):
        self.image = image
        self.playerNum = playerNum
        self.rect = self.image.get_rect()
        self.rect.center = ((pos_X+SQUARE_SIZE / 2),(pos_Y + SQUARE_SIZE / 2))
        self.inventory = []
        self.velX = 0
        self.velY = 0
        self.endX = 0
        self.endY = 0
        self.evenY = [0+5, 140+5, 280+5, 420+5, 560+5]
        self.oddY = [70+5, 210+5, 350+5, 490+5, 630+5]
        self.rolled = False

        # Controllers for player movement
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        self.currentRow = 9
        self.speed = 5
        self.rolledNumber = 0
        self.isMoving = False

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

    def draw(self, win):
        win.blit(self.image, self.rect)

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

            if self.rect.y in self.evenY:
                self.currentRow -= 1

                # Recalculate endX when changing rows
                self.endX = WIDTH - (abs(self.endX - WIDTH) + SQUARE_SIZE)
            if self.rect.x >= 9*SQUARE_SIZE - 5:
                self.moveUp = True
                self.moveRight = False
                
        # Change direction if row is even-numbered
        if self.currentRow % 2 == 0:
            # print(f'Current x-coord is: {self.rect.x}')
            # print(f'Next x-coord is: {self.endX}')
            self.moveUp = False
            self.moveRight = False
            self.moveLeft = True
            
            if self.rect.y in self.oddY:
                self.currentRow -= 1

                # Recalculate endX when changing rows
                self.endX = abs(self.endX - 0) - SQUARE_SIZE
            if self.rect.x <= 0 + 5:
                self.moveUp = True  
                self.moveLeft = False

        if self.currentRow % 2 == 1:
            if self.rect.x < self.endX:
                self.rect.x += self.velX
                self.rect.y += self.velY
            else:
                self.isMoving = False
        elif self.currentRow % 2 == 0:
            if self.rect.x > self.endX:
                self.rect.x += self.velX
                self.rect.y += self.velY
            else:
                self.isMoving = False