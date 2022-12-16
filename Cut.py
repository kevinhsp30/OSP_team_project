from cut_source import *
import setup

bg_fire = setup.Scene(pygame.image.load('image\stage_3\stage3_hd_32_2.png'))


#컷 1 함수 (stage 1 시작전)
def cut1():
    global w_count, k_space, k_click, d_sound
    w_count = 0
    while True:
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
        while w_count == 0:
            sleep()
            time.sleep(3)
            w_count +=1
        if w_count ==1:
            room1()
            if k_click or k_space:
                w_count =2
                k_click = False
                k_space = False
                d_sound = True
        if w_count==2:
            room2()
            w_count=3
        if w_count ==3:
            d1()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 4
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==4:
            d2()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 5
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==5:
            d3()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 6
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==6:
            d4()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 7
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==7:
            d5()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 8
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==8:
            d6()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                k_click = False
                k_space = False
                t_sound.stop()
                break                                      #-> stage 1 시작
            
            
#컷 2 함수 (stage 2 시작전)
def cut2():
    global k_click, k_space, w_count
    w_count = 0
    while True:
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
        if w_count == 0:
            sleep()
            if k_click or k_space:
                w_count = 1
                k_click = False
                k_space = False
                d_sound = True
        if w_count ==1:
            d21()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 2
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==2:
            d22()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 3
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==3:
            d23()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 4
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==4:
            d24()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 5
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==5:
            d25()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 6
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==6:
            d26()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 7
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==7:
            d27()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                k_click = False
                k_space = False
                t_sound.stop()
                break                                       #-> stage 2 시작
#컷 3 함수 (stage 3 시작전)
def cut3():
    global w_count, k_click, k_space
    w_count = -1
    ns_sound.play()
    while True:
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
                    
        if w_count == -1:
            ns()
            if k_click or k_space:
                w_count = 0
                k_click = False
                k_space = False
                ns_sound.stop()
        if w_count == 0:
            sleep2()
            if k_click or k_space:
                w_count = 1
                k_click = False
                k_space = False
                d_sound = True
        if w_count ==1:
            d31()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 2
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==2:
            d32()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                w_count = 3
                k_click = False
                k_space = False
                d_sound = True
                t_sound.stop()
        if w_count ==3:
            d33()
            if d_sound:
                t_sound.play()
                d_sound = False
            if k_click or k_space:
                k_click = False
                k_space = False
                t_sound.stop()
                break                                       #-> stage 3 시작
#엔딩 컷
def cut_end():
    global w_count, k_click, k_space
    w_count = 0
    car_sound.play()
    while True:
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
        if w_count == 0:
            end1()
            if k_click or k_space:
                w_count = 1
                k_click = False
                k_space = False
        if w_count == 1:
            end2()
            if k_click or k_space:
                w_count = 2
                k_click = False
                k_space = False
        if w_count == 2:
            end3()
            if k_click or k_space:
                k_click = False
                k_space = False
                break                                       #->엔딩 종료화면

#히든 엔딩컷
def hid_end_cut():
    global k_click, k_space
    w_count = -2
    ns_sound.play()
    while True:
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
                    
        if w_count == -2:
            screen.blit(bg_fire.scene,(0,0))
            if k_click or k_space:
                w_count += 1
                k_click = False
                k_space = False

        elif w_count == -1:
            ns()
            if k_click or k_space:
                w_count += 1
                k_click = False
                k_space = False
                ns_sound.stop()
                end_sound.play()
        elif w_count == 0:
            hid_end1()
            time.sleep(2)
            hid_end2()
            time.sleep(2)
            break                                     #-> 히든엔딩 종료화면
        pygame.display.update()

# cut1()
# cut2()
# cut3()
# cut_end()
# hid_end_cut()