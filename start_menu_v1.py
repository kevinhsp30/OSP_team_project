import pygame
import sys
import time

import setup

screen = setup.screen
screen_width = setup.screen_width
screen_height = setup.screen_height

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

def start_menu():
    white = (255, 255, 255)
    black = (0, 0, 0)
    k_space = False
    k_s = False
    pygame.display.set_caption("start menu")
    screen = pygame.display.set_mode((screen_width, screen_height))
    blink = False
    #print(pygame.font.get_fonts())
    
    running = True
    while running:
        screen.fill(black)
        font = pygame.font.Font(None,50)
        main_font = pygame.font.SysFont('segoeuisemibold',200,True,False)
        setting_font = pygame.font.SysFont('segoeuihistoric',50,True,True)
        main_text = main_font.render("GAME",True,white)
        main_text.get_rect().size
        setting = font.render("press     to change  ",True,(150,150,150))
        setting_bold = setting_font.render("s          setting",True,(160,160,160))
        setting_rect = setting.get_rect()
        setting_rect.center = (1220,50)
        start_space = font.render("press space to start",True,(0,200,80))
        start_space_b = font.render("press space to start",True,black)
        screen.blit(main_text,(450/1600*screen_width,200/900*screen_height))
        

        screen.blit(setting_bold,(1160/1900*screen_width,8/900*screen_height))
    
    #start,bliking
        if blink == False:
            screen.blit(start_space,(650,675))
            time.sleep(0.3)    
            blink = True
        elif blink == True:
            screen.blit(start_space_b,(650,675))
            time.sleep(0.1)
            blink = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    k_space = True
                elif event.key == pygame.K_s:
                    k_s = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    k_space = False
                elif event.key == pygame.K_s:
                    k_s = True
        if k_space:
            break
        if k_s==True:
            pygame.draw.rect(screen, (50,70,50), [150, 150, 1300, 600])
            setting_pop = setting_font.render("setting",True,white)
            screen.blit(setting_pop, (200,200))
            time.sleep(0.5)
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            k_s = False          
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_s:
                            k_s = False
        pygame.display.flip()