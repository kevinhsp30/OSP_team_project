from pickle import TRUE
import pygame
import sys
import time
import threading

import setup

bg = setup.Background(pygame.image.load('BG.png'))
SCREEN_WIDTH = setup.screen_width
print(SCREEN_WIDTH)
SCREEN_HEIGHT = setup.screen_height
adj_X = SCREEN_WIDTH / 1280
adj_Y = SCREEN_HEIGHT / 720
def start_menu():
    num = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    k_space = False
    k_stg = False
    k_click = False
    main_pos = False
    stg_num = 0
    main_size = [150]
    main_x = 380 
    main_y = 250 
    blink = [1]
    background_x = 0
    background2_x = bg.width
    sg_x,sg_y = 50 *adj_X , 610 *adj_Y
    sg_size = 50
    pygame.init()
    # pygame.display.set_caption("start menu")
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = setup.screen
    main_bgm = pygame.mixer.Sound('main_bgm.mp3')
    start_sound = pygame.mixer.Sound('start.mp3')
    stg_sound = pygame.mixer.Sound('stg.wav')
    # def playing_main_bgm():
    #     main_bgm.play()
    #     threading.Timer(41, playing_main_bgm).start()
    # playing_main_bgm()
    #print(pygame.font.get_fonts())
    # def blinking(blink):
    #         blink[0] += 1
    #         threading.Timer(0.6, blinking,[blink]).start()

    # blinking(blink)
    while True:
        #print(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        screen.fill(black)
        background = pygame.image.load('BG.png')
        background = bg.background
        count = 1
        # if bg.posX % bg.width == 0:
        #     screen.blit(bg.background, (bg.posX + bg.width* count, 0))
        #     count += 1
        background2 = background.copy()
        background_x -= 2
        background2_x -= 2 #bg.width/8
        if background_x == - bg.width:
            background_x = bg.width
        if background2_x == -bg.width:
            background2_x = bg.width
            
        screen.blit(background,(background_x,0))
        screen.blit(background,(background2_x,0))
        
        
        # bg.posX -= 40 *adj_X 
        # screen.blit(background,(background_x,0))
        
        font = pygame.font.SysFont('franklingothicmedium',30,True,False)
        main_font = pygame.font.SysFont('inkfree',main_size[0],True,False)
        stage_font = pygame.font.SysFont('inkfree',sg_size,True,False)
        main_text = main_font.render("START",True,white)
        start_space = font.render("press space or click to start",True,(255, 143, 177))
        stage_text = stage_font.render("Stages",True,white)
        screen.blit(main_text,(main_x *adj_X * 0.65,main_y*adj_Y * 0.65))
        screen.blit(stage_text,(sg_x,sg_y))
        if 392 *adj_X< pygame.mouse.get_pos()[0]< 916 *adj_X and  284 *adj_Y < pygame.mouse.get_pos()[1]< 379  *adj_Y:
            main_size[0] = 200
            main_x = 300 *adj_X * 1.16
            main_y = 220 *adj_Y * 1.07
            main_pos = True
        elif 55*adj_X < pygame.mouse.get_pos()[0] < 222*adj_X and 623 *adj_Y < pygame.mouse.get_pos()[1] < 655 *adj_Y:
            sg_x,sg_y = 30 *adj_X, 600 *adj_Y
            sg_size = 70
            k_stg = True
        else:
            main_size[0] = 150
            main_x = 380 *adj_X
            main_y = 250 *adj_Y
            main_pos = False
            sg_x,sg_y = 50 *adj_X, 610 *adj_Y
            sg_size = 50
            k_stg = False
    #start,bliking
        if blink[0] % 2 == 0:
            screen.blit(start_space,(420*adj_X,620 *adj_Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    k_space = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    k_space = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                k_click = True
                if k_stg:
                    stg_num +=1
                    stg_sound.play()

            else:
                k_click = False
        if k_space:
            break
        if main_pos and k_click:
            break
        if stg_num % 2 == 1:
            pygame.draw.rect(screen,(82, 5, 86),[150,155,980,410])
            pygame.draw.rect(screen,(241, 144, 183),[155,160,970,400])
        pygame.display.flip()

        start_sound.play()          
        pygame.display.flip()
        
        
    
# start_menu()

