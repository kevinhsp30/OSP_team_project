import pygame
import setup

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
                break                                                                                    #다시시작 
            
        else:
            screen.blit(bt_restart.scene,(SCREEN_WIDTH*0.3 , SCREEN_HEIGHT*0.65))
            
        #end
        if bt_exit.posX < pygame.mouse.get_pos()[0]< bt_exit.posX + bt_exit.width and  bt_exit.posY < pygame.mouse.get_pos()[1]< bt_exit.posY + bt_exit.height:

            center_X = bt_exit.posX + bt_exit.width/2
            center_Y = bt_exit.posY + bt_exit.height/2
            screen.blit(pygame.transform.scale(bt_exit.scene,(bt_exit.width*1.2,bt_exit.height*1.2)),(center_X- bt_exit.width*1.2/2,center_Y - bt_exit.height*1.2/2))
            
            if k_click:                                                                                     #종료
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
                break                                                                                    #다시시작 
            
        else:
            screen.blit(bt_restart.scene,(SCREEN_WIDTH*0.3 , SCREEN_HEIGHT*0.65))
        #end
        if bt_exit.posX < pygame.mouse.get_pos()[0]< bt_exit.posX + bt_exit.width and  bt_exit.posY < pygame.mouse.get_pos()[1]< bt_exit.posY + bt_exit.height:

            center_X = bt_exit.posX + bt_exit.width/2
            center_Y = bt_exit.posY + bt_exit.height/2
            screen.blit(pygame.transform.scale(bt_exit.scene,(bt_exit.width*1.2,bt_exit.height*1.2)),(center_X- bt_exit.width*1.2/2,center_Y - bt_exit.height*1.2/2))
            
            if k_click:                                                                                     #종료
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
    


'''
#히든 엔딩 -> hid_ending()
def hid_ending():
    pygame.init()
    screen = setup.screen
    global end_bg_y, end_bg2_y, k_space, end_bg, end_bg2, end_text_end, end_text_re, re_size, re_xy, end_size, end_xy, k_click
    while True:
        end_text_re = pygame.image.load("image/re_t.png")
        end_text_end = pygame.image.load('image/end_t.png')
        #print(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        end_text_re = pygame.transform.scale(end_text_re,re_size)
        end_text_end = pygame.transform.scale(end_text_end,end_size)
        screen.fill(black)
        screen.blit(end_bg,(0,end_bg_y))
        screen.blit(end_bg2,(0,end_bg2_y))
        screen.blit(end_text_re,re_xy)
        screen.blit(end_text_end,end_xy)
        end_bg_y +=1
        end_bg2_y +=1
        if end_bg_y == 720:
            end_bg_y = -720
        if end_bg2_y == 720:
            end_bg2_y = -720
        screen.blit(END_text,(310,120))
        screen.blit(sub_text2,(380,370))
        #re
        if 350 < pygame.mouse.get_pos()[0]< 520 and  450 < pygame.mouse.get_pos()[1]< 550:
            re_size = (200,145)
            re_xy = (340,442)
            if k_click:
                break                                                                            #다시시작 
        else:
            re_size = (179,130)
            re_xy = (350,450)
        #end
        if 757 < pygame.mouse.get_pos()[0]< 930 and  464 < pygame.mouse.get_pos()[1]< 560:
            end_size = (200,116)
            end_xy = (745,457)
            if k_click:                                                                             #종료
                break
        else:
            end_size = (177,103)
            end_xy = (757,464)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                k_click = True
            else:
                k_click = False
        pygame.display.flip()

'''
