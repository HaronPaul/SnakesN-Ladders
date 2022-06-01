from xml.etree.ElementTree import tostring
import pygame
import os

from game.powerUp import PowerUp

def get_font(size):
    fontPath = os.path.join(os.path.dirname(__file__), '..', 'assets', "KB3BusRoute123.ttf") 
    return pygame.font.Font(fontPath, size)

def renderExtras(WIN, currentPlayer):
    WIN.fill(pygame.Color('black'))

    # Render current player text
    text1 = 'Player'
    PLAYER_TEXT = get_font(20).render(text1, True, 'white')
    PLAYER_TEXT_POS = PLAYER_TEXT.get_rect(center=(((700+800) / 2), 30))
    WIN.blit(PLAYER_TEXT, PLAYER_TEXT_POS)    

    CURRENT_PLAYER_TEXT = get_font(50).render(str(currentPlayer), True, 'white')
    CURRENT_PLAYER_TEXT_POS = CURRENT_PLAYER_TEXT.get_rect(center=(((700+800) / 2), 100))
    WIN.blit(CURRENT_PLAYER_TEXT, CURRENT_PLAYER_TEXT_POS)

    text2 = 'Dice'
    DICE_TEXT = get_font(25).render(text2, True, 'white')
    DICE_TEXT_POS = DICE_TEXT.get_rect(center=(((700+800) / 2), 170))
    WIN.blit(DICE_TEXT, DICE_TEXT_POS)

    text3 = 'Rolled'
    ROLLED_TEXT = get_font(25).render(text3, True, 'white')
    ROLLED_TEXT_POS = ROLLED_TEXT.get_rect(center=(((700+800) / 2), 200))
    WIN.blit(ROLLED_TEXT, ROLLED_TEXT_POS)

    text4 = 'Power'
    POWER_TEXT = get_font(25).render(text4, True, 'white')
    POWER_TEXT_POS = POWER_TEXT.get_rect(center=(((700+800) / 2), 350))
    WIN.blit(POWER_TEXT, POWER_TEXT_POS)

    text5 = 'Ups'
    UPS_TEXT = get_font(25).render(text5, True, 'white')
    UPS_TEXT_POS = UPS_TEXT.get_rect(center=(((700+800) / 2), 380))
    WIN.blit(UPS_TEXT, UPS_TEXT_POS)

    # # Render UPS-ups textt
    # power_ups_text = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'power_ups_text.png'))
    # WIN.blit(power_ups_text, (200, 800))

def renderDiceNumber(WIN, diceNumber):
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect(700,220,100,100))

    picPath =  os.path.join(os.path.dirname(__file__), '..', 'assets', f'{diceNumber}.png')
    diceImage = pygame.image.load(picPath)

    # DICE_NUMBER_TEXT = get_font(70).render(str(diceNumber), True, 'white')
    # DICE_NUMBER_TEXT_POS = DICE_NUMBER_TEXT.get_rect(center=(((700+800) / 2), 250))
    # WIN.blit(DICE_NUMBER_TEXT, DICE_NUMBER_TEXT_POS)
    WIN.blit(diceImage, (700, 220))

def renderPlayerInventory(WIN, player):
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect(700,400,100,450))

    start = 410
    for powerUp in player.inventory:
        drawX = ((700 + 800) // 2) - (powerUp.image.get_size()[0] // 2)
        WIN.blit(powerUp.image, (drawX, start))
        start += 80

        
def renderWaitingText(WIN):
    text = 'Waiting'
    WAIT_TEXT = get_font(18).render(text, True, 'white')
    WAIT_TEXT_POS = WAIT_TEXT.get_rect(center=(((700+800) / 2), 630))
    WIN.blit(WAIT_TEXT, WAIT_TEXT_POS)

