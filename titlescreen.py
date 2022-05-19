# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:05:24 2022

@author: PRINCE JIMENEZ
"""

import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snakes N Ladders")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/KB3BusRoute123.ttf", size)
def get_font2(size):
    return pygame.font.Font("assets/Kumadinya.ttf", size)
def get_font3(size):
    return pygame.font.Font("assets/KB3BusRoute123.ttf", size)
    
def play():
    pygame.display.set_caption("Play")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        PLAY_TEXT = get_font(50).render("PLAY screen", True, "green")
        PLAY_OB = PLAY_TEXT.get_rect(center=(640,260))
        SCREEN.blit(PLAY_TEXT, PLAY_OB)

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(50), base_color="brown", hovering_color="red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    game_title()
                
        pygame.display.update()
    
def rules():
    pygame.display.set_caption("Rules")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        RULES_MOUSE_POS = pygame.mouse.get_pos()

        text= "Rules"
        text1='1. Initally both the players are at starting position.'
        text2='2. Take it in turns to roll the dice.'
        text3='3. Move forward the number of spaces shown on the dice.'
        text4='4. If you land at the bottom of a ladder, you can move up to the top of the ladder.'
        text5='5. If you land on the head of a snake, you must slide down to the bottom of the snake.'
        text6='6. The first player to get to the FINAL position is the winner.'
        text7='7. Hit enter to roll the dice.'
        
        RULES_TEXT = get_font(50).render(text, True, "orange")
        RULES_OB = RULES_TEXT.get_rect(center=(630, 130))
        SCREEN.blit(RULES_TEXT, RULES_OB)
        RULES_TEXT1 = get_font2(30).render(text1, True, "white")
        RULES_OB = RULES_TEXT1.get_rect(center=(440, 200))
        SCREEN.blit(RULES_TEXT1, RULES_OB)
        RULES_TEXT2 = get_font2(30).render(text2, True, "white")
        RULES_OB = RULES_TEXT2.get_rect(center=(350, 250))
        SCREEN.blit(RULES_TEXT2, RULES_OB)
        RULES_TEXT3 = get_font2(30).render(text3, True, "white")
        RULES_OB = RULES_TEXT3.get_rect(center=(485, 300))
        SCREEN.blit(RULES_TEXT3, RULES_OB)
        RULES_TEXT4 = get_font2(30).render(text4, True, "white")
        RULES_OB = RULES_TEXT4.get_rect(center=(630, 350))
        SCREEN.blit(RULES_TEXT4, RULES_OB)
        RULES_TEXT5 = get_font2(30).render(text5, True, "white")
        RULES_OB = RULES_TEXT5.get_rect(center=(645, 400))
        SCREEN.blit(RULES_TEXT5, RULES_OB)
        RULES_TEXT6= get_font2(30).render(text6, True, "white")
        RULES_OB = RULES_TEXT6.get_rect(center=(510, 450))
        SCREEN.blit(RULES_TEXT6, RULES_OB)
        RULES_TEXT7= get_font2(30).render(text7, True, "white")
        RULES_OB = RULES_TEXT7.get_rect(center=(320, 500))
        SCREEN.blit(RULES_TEXT7, RULES_OB)

        RULES_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(50), base_color="orange", hovering_color="red")

        RULES_BACK.changeColor(RULES_MOUSE_POS)
        RULES_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                    game_title()

        pygame.display.update()

def game_title():
    while True:
        SCREEN.blit(BG, (0, 0))

        GT_MOUSE_POS = pygame.mouse.get_pos()

        GT1_TEXT = get_font(75).render("SNAKES N LADDERS", True, "green")
        GT1_RECT = GT1_TEXT.get_rect(center=(640, 150))
        GT2_TEXT = get_font(75).render("Powered Up", True, "blue")
        GT2_RECT = GT2_TEXT.get_rect(center=(640, 240))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Ob.png"), pos=(640, 360), 
                            text_input="PLAY", font=get_font3(70), base_color="white", hovering_color="green")
        RULES_BUTTON = Button(image=pygame.image.load("assets/Rules Ob.png"), pos=(640, 470), 
                            text_input="RULES", font=get_font3(70), base_color="white", hovering_color="blue")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Ob.png"), pos=(640,580), 
                            text_input="QUIT", font=get_font3(70), base_color="white", hovering_color="red")

        SCREEN.blit(GT1_TEXT, GT1_RECT)
        SCREEN.blit(GT2_TEXT, GT2_RECT)

        for button in [PLAY_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
            button.changeColor(GT_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(GT_MOUSE_POS):
                    play()
                if RULES_BUTTON.checkForInput(GT_MOUSE_POS):
                    rules()
                if QUIT_BUTTON.checkForInput(GT_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

game_title()