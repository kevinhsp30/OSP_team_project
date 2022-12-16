import pygame
import setup
import play_val

SCREEN_WIDTH = setup.screen_width
SCREEN_HEIGHT = setup.screen_height

bg_ed_true_back = setup.Scene(pygame.image.load("image\\trueback.png"))
bg_ed_normal_back = setup.Scene(pygame.image.load("image\\normalback.png"))

bt_restart = setup.Scene(pygame.image.load("image\다시시작.png"),SCREEN_WIDTH*0.3 , SCREEN_HEIGHT*0.65)
bt_exit = setup.Scene(pygame.image.load("image\게임종료2.png"))
bt_exit = setup.Scene(pygame.image.load("image\게임종료2.png"),SCREEN_WIDTH*0.7-bt_exit.width , SCREEN_HEIGHT*0.67)

#엔딩 -> ending()
def ending():
    pygame.init()
    k_click = False
    screen = setup.screen
    
    while True:
    
        screen.blit(bg_ed_normal_back.scene,(0,0))
        
        
        #re
        if bt_restart.posX < pygame.mouse.get_pos()[0]< bt_restart.posX + bt_restart.width and  bt_restart.posY < pygame.mouse.get_pos()[1]< bt_restart.posY + bt_restart.height:
            center_X = bt_restart.posX + bt_restart.width/2
            center_Y = bt_restart.posY + bt_restart.height/2
            screen.blit(pygame.transform.scale(bt_restart.scene,(bt_restart.width*1.2,bt_restart.height*1.2)),(center_X - bt_restart.width*1.2/2,center_Y - bt_restart.height*1.2/2))
            
            if k_click:
                play_val.end_restart = True
                break                                                                                    #다시시작 
            
        else:
            screen.blit(bt_restart.scene,(SCREEN_WIDTH*0.3 , SCREEN_HEIGHT*0.65))
            
        #end
        if bt_exit.posX < pygame.mouse.get_pos()[0]< bt_exit.posX + bt_exit.width and  bt_exit.posY < pygame.mouse.get_pos()[1]< bt_exit.posY + bt_exit.height:

            center_X = bt_exit.posX + bt_exit.width/2
            center_Y = bt_exit.posY + bt_exit.height/2
            screen.blit(pygame.transform.scale(bt_exit.scene,(bt_exit.width*1.2,bt_exit.height*1.2)),(center_X- bt_exit.width*1.2/2,center_Y - bt_exit.height*1.2/2))
            
            if k_click:                                                                                     #종료
                play_val.end_exit = True
                break
            
        else:
            screen.blit(bt_exit.scene,(SCREEN_WIDTH*0.7-bt_exit.width , SCREEN_HEIGHT*0.67))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                k_click = True
            else:
                k_click = False
        pygame.display.flip()
    


def hid_ending():
    pygame.init()
    k_click = False
    screen = setup.screen
    
    while True:
    
        screen.blit(bg_ed_true_back.scene,(0,0))
        
        
        #re
        if bt_restart.posX < pygame.mouse.get_pos()[0]< bt_restart.posX + bt_restart.width and  bt_restart.posY < pygame.mouse.get_pos()[1]< bt_restart.posY + bt_restart.height:
            center_X = bt_restart.posX + bt_restart.width/2
            center_Y = bt_restart.posY + bt_restart.height/2
            screen.blit(pygame.transform.scale(bt_restart.scene,(bt_restart.width*1.2,bt_restart.height*1.2)),(center_X - bt_restart.width*1.2/2,center_Y - bt_restart.height*1.2/2))
            
            if k_click:
                play_val.end_restart = True
                break                                                                                    #다시시작 
            
        else:
            screen.blit(bt_restart.scene,(SCREEN_WIDTH*0.3 , SCREEN_HEIGHT*0.65))
            
        #end
        if bt_exit.posX < pygame.mouse.get_pos()[0]< bt_exit.posX + bt_exit.width and  bt_exit.posY < pygame.mouse.get_pos()[1]< bt_exit.posY + bt_exit.height:

            center_X = bt_exit.posX + bt_exit.width/2
            center_Y = bt_exit.posY + bt_exit.height/2
            screen.blit(pygame.transform.scale(bt_exit.scene,(bt_exit.width*1.2,bt_exit.height*1.2)),(center_X- bt_exit.width*1.2/2,center_Y - bt_exit.height*1.2/2))
            
            if k_click:                                                                                     #종료
                play_val.end_exit = True
                break
            
        else:
            screen.blit(bt_exit.scene,(SCREEN_WIDTH*0.7-bt_exit.width , SCREEN_HEIGHT*0.67))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                k_click = True
            else:
                k_click = False
        pygame.display.flip()
    

