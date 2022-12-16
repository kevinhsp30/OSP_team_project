from pickle import TRUE
import pygame


import setup


################### 시작 메뉴 파일 ###################


SCREEN_WIDTH = setup.screen_width
SCREEN_HEIGHT = setup.screen_height

adj_X = SCREEN_WIDTH / 1290
adj_Y = SCREEN_HEIGHT / 730

bg = setup.Background(pygame.image.load('BG.png'))
titlename = setup.Background(pygame.image.load("image\\titlename.png"))
titlename.background = pygame.transform.scale(pygame.image.load("image\\titlename.png"),(SCREEN_WIDTH,SCREEN_HEIGHT))
bt_game_start = pygame.image.load("image\게임시작.png")
bt_game_start = pygame.transform.scale(bt_game_start,(bt_game_start.get_width()*adj_X,bt_game_start.get_height()*adj_Y))

bt_game_exit = pygame.image.load("image\게임종료.png")
bt_game_exit = pygame.transform.scale(bt_game_exit,(bt_game_exit.get_width()*adj_X,bt_game_exit.get_height()*adj_Y))

def start_menu():
    black = (0, 0, 0)
    k_space = False
    game_exit_pos = False
    k_click = False
    game_start_pos = False
    stg_num = 0
  
    background_x = 0
    background2_x = bg.width
    pygame.init()
    screen = setup.screen
    main_bgm = pygame.mixer.Sound('main_bgm.mp3')
    start_sound = pygame.mixer.Sound('start.mp3')

    while True:
        screen.fill(black)
        
        background = bg.background
        
        background_x -= 2
        background2_x -= 2 #bg.width/8
        if background_x == - bg.width:
            background_x = bg.width
        if background2_x == -bg.width:
            background2_x = bg.width
            
        # 배경, 제목, 버튼 그리는 부분
        screen.blit(background,(background_x,0))
        screen.blit(background,(background2_x,0))
        screen.blit(titlename.background,(titlename.posX,-SCREEN_HEIGHT*0.035))
        screen.blit(bt_game_start,( (SCREEN_WIDTH/2-SCREEN_WIDTH*0.1-bt_game_start.get_width())* 1.1 , (SCREEN_HEIGHT/2-bt_game_start.get_height())* 1.1 ))
        screen.blit(bt_game_exit,( SCREEN_WIDTH-((SCREEN_WIDTH/2-SCREEN_WIDTH*0.1-bt_game_start.get_width())* 1.1 + bt_game_exit.get_width() ) , (SCREEN_HEIGHT/2-bt_game_exit.get_height())* 1.1 ))
        bt_game_exit_posX = SCREEN_WIDTH-((SCREEN_WIDTH/2-SCREEN_WIDTH*0.1-bt_game_start.get_width())* 1.1 + bt_game_exit.get_width())
        bt_game_exit_posY = (SCREEN_HEIGHT/2-bt_game_exit.get_height())* 1.1
        
        
        # 마우스 위치와 클릭 여부
        if (SCREEN_WIDTH/2-SCREEN_WIDTH*0.1-bt_game_start.get_width())* 1.1 < pygame.mouse.get_pos()[0]< ((SCREEN_WIDTH/2-SCREEN_WIDTH*0.1-bt_game_start.get_width())* 1.1) + bt_game_start.get_width() and  (SCREEN_HEIGHT/2-bt_game_start.get_height())* 1.1 < pygame.mouse.get_pos()[1]< (SCREEN_HEIGHT/2-bt_game_start.get_height())* 1.1 + bt_game_start.get_height():
            

            game_start_pos = True
        elif bt_game_exit_posX < pygame.mouse.get_pos()[0] < bt_game_exit_posX + bt_game_exit.get_width() and bt_game_exit_posY < pygame.mouse.get_pos()[1] < bt_game_exit_posY + bt_game_exit.get_height():

            game_exit_pos = True
        else:
            

            game_start_pos = False

            game_exit_pos = False

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

            else:
                k_click = False
        if k_space:
            break
        if game_start_pos and k_click:
        
            break
        if game_exit_pos and k_click:
            pygame.quit()
            quit()
        if stg_num % 2 == 1:
            pygame.draw.rect(screen,(82, 5, 86),[150,155,980,410])
            pygame.draw.rect(screen,(241, 144, 183),[155,160,970,400])
        pygame.display.flip()

    start_sound.play()          
   
