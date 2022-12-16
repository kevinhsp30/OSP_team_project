import pygame as py
import sys
import time
import random

import setup
import play_val
import cut_source

################### 세 번째 스테이지 파일 ###################


screen = setup.screen        # 사용자 모니터 해상도
screen_width = setup.screen_width
screen_height = setup.screen_height



def third_stage():
    py.init()
    
    # 인스턴스 생성 및 초기화
    Puang = setup.Character()

    # Puang.character = py.transform.scale(py.image.load("image\푸앙_사랑_look_right.png"), (Puang.width,Puang.height))
    bg_1 = setup.Background(py.image.load("image\stage1_bg.png"))
    bg_2 = setup.Background(py.image.load("image\stage2_bg.png"))
    bg_3 = setup.Background(py.image.load("image\stage3_bg.png"))
    bg_3_fire = setup.Background(py.image.load("image\BG_3rd_fire.png"))
    
    setup.Obstacle.count = 0
    setup.Obstacle.obs_list = []

    # 장애물 랜덤 생성
    ob_1 = "image\stage_3\stage3_ob1.png"
    ob_2 = "image\stage_3\stage3_ob2.png"
    ob_3 = "image\stage_3\stage3_ob3.png"
    ob_4 = "image\stage_3\stage3_ob4.png"
    
    effect = setup.Scene(py.image.load("image\stage_3\stage3_paang.png"))
    

    bubble1 = setup.Scene(py.image.load("image\stage_3\stage3_bubble1.png"))
    bubble2 = setup.Scene(py.image.load("image\stage_3\stage3_bubble2.png"))
    bubble3 = setup.Scene(py.image.load("image\stage_3\stage3_bubble3.png"))
    bub1_time = 0
    bub2_time = 0
    bub3_time = 0

    type_obs = [ob_1,ob_2,ob_3,ob_4]

    land_obs = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*0.6)
    land_obs_2 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*1)

    land_obs_3 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*1.6)
    land_obs_4 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*2.1)

    land_obs_5 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*2.5)
    land_obs_6 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*3)

    land_obs_7 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*3.6)
    land_obs_8 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*4)

    land_obs_9 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*4.4)
    land_obs_10 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*4.9)

    land_obs_11 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*5.3)
    land_obs_12 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,4)]),screen_width*5.6)
    
    ob_truck = setup.Obstacle(py.image.load("image\\truck_2.png"),screen_width*7)
    
    obs_list = setup.Obstacle.obs_list
    

    

    
    # py.display.set_caption("1st_Stage")
    to_x, to_y = 0,0

    
    clock = py.time.Clock()
    
    # bg_1 = setup.Background(py.image.load("image\stage1_bg.png"))
    # land_obs = setup.land_obs
    # land_obs_2 = setup.land_obs_2
    # Puang = setup.Character()
    bg = bg_3
    
    play_val.is_Collision = False
    init_speed = 1
    count = 0
    distance = 0
    cross_leg = True
    temp_speed = 0
    ground = screen_height - Puang.posY    
    running = True
    global is_coll_truck
    is_coll_truck = False
    temp_t = 0
    
    while running:
        
        
        dt = clock.tick(15)
    
        # 속도 고정
        # 속도 변화 전처리 or 후처리 결정 필요
        if count < 20:
            temp_speed = init_speed
            temp_speed *= dt
            speed = temp_speed
            count += 1
        
        print(obs_list[1].posX, Puang.posX)
        print("land_obs.count :",land_obs.count, obs_list[1].posX)
        print("Fps :", str(clock.get_fps()), "speed :", speed,", ", to_x)



        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    to_x -= speed
                    if Puang.is_sight == "right":
                        Puang.trun_Char()

                elif event.key == py.K_RIGHT:
                    to_x += speed
                    if Puang.is_sight == "left":
                        Puang.trun_Char()

                # elif event.key == py.K_UP:
                #     to_y -= speed
                # elif event.key == py.K_DOWN:
                #     to_y += speed

                elif event.key == py.K_SPACE and Puang.is_running:
                    Puang.is_jumping = True
                    Puang.is_running = False


            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                    to_x = 0
                    if py.key.get_pressed()[py.K_LEFT]:
                        to_x -= speed

                    if py.key.get_pressed()[py.K_RIGHT]:
                        to_x += speed

                # elif event.key == py.K_UP or event.key == py.K_DOWN:
                #     to_y = 0
                #     if py.key.get_pressed()[py.K_UP]:
                #         to_y -= speed
                #     if py.key.get_pressed()[py.K_DOWN]:
                #         to_y += speed


        
        
        # 속도 제한
        if to_x > speed:
            to_x = speed
        if to_x < -speed:
            to_x = -speed



        # 방향 재확인
        if to_x < 0 and Puang.is_sight == "right":
            Puang.trun_Char()
        if to_x > 0 and Puang.is_sight == "left":
            Puang.trun_Char()


        # 점프
        if Puang.is_jumping:
            Puang.posY -= speed
            if Puang.posY < ground/   0.4 :  # 점프 높이
                Puang.is_jumping = False
                
        # 높이를 지면에 고정(중력)
        if not Puang.is_jumping:
            Puang.posY += speed
            if Puang.posY > screen_height - Puang.height - screen_height*0.1:
                Puang.posY = screen_height - Puang.height - screen_height*0.1
                Puang.is_running = True


        # 맵 왼쪽 끝 부분에서의 배경 및 물체 컨트롤
        if bg.posX > 0:
            bg.posX = 0
            Puang.posX += to_x
            
        if Puang.posX < 0:
            Puang.posX = 0
            to_x = 0



        ### 장애물 이동
        if Puang.posX < (screen_width/2) - (Puang.width/2):
            
            bg.posX = 0
            Puang.posX += to_x
            for i in range(0,len(obs_list)):
                obs_list[i].posX += to_x
            # land_obs.posX += to_x
            # land_obs_2.posX += to_x



    
        # 배경과 장애물 이동
        # 원근감 표현
        bg.posX -= to_x/2
        for i in range(0,len(obs_list)):
            obs_list[i].posX -= to_x
            
        # land_obs.posX -= to_x
        # land_obs_2.posX -= to_x
        
        
        # 충돌 확인
        for i in range(0,len(obs_list)):
            temp = False
            if Puang.posX  < (obs_list[i].posX + obs_list[i].width)- obs_list[i].width*0.2 and Puang.posX + Puang.width > obs_list[i].posX + obs_list[i].width*0.2:
                if i != len(obs_list)-1:
                    if random.randrange(1,15) == 1 and i != 12:
                        temp = True
                
                if Puang.posY + Puang.height > obs_list[i].posY + obs_list[i].height*0.2 or temp:
                    play_val.is_Collision = True
                    play_val.third_coll_num = i
                    obs_list[i].is_coll = True
                    temp = False
                    if i == 12:
                        is_coll_truck = True


        # 트럭 충돌
        if obs_list[len(obs_list)-2].posX + Puang.width*6 <= Puang.posX:
            ob_truck.posX -= speed*1.5
            if ob_truck.posX+ob_truck.width <= Puang.posX:
                ob_truck.posX -= speed*1.5


        # 트럭 충돌 시
        if is_coll_truck:
            
            
            break
        
        # 트럭 회피 시
        if  Puang.posX >= ob_truck.posX and Puang.posY == screen_height - Puang.height - screen_height*0.1: # 바닥
            temp_t += 1
            if temp_t >= 2:
                
                is_coll_truck = False
                break
            


        if bub1_time == 30 or bub2_time == 30 or bub3_time == 30:

            play_val.is_Collision = False
            if bub1_time == 30:
                bub1_time+=1
            elif bub2_time == 30:
                bub2_time+=1
            elif bub3_time == 30:
                bub3_time+=1

        
        if Puang.posX > 0:
            distance += to_x
        print('distance = ', distance)
        
        
        # 배경 그리는 부분
        for i in (0,1,2,3,4,5):
            screen.blit(bg.background, (bg.posX + bg.width* i, -screen_height*0.06))
        bg_3_fire.posX = bg.posX
        screen.blit(bg_3_fire.background, (bg_3_fire.posX + bg_3_fire.width* 2, -screen_height*0.06))


        # 걷기 모션
        temp_distance = distance
        if temp_distance%speed !=0:
            temp_distance -= temp_distance%speed
            
        if temp_distance%(speed*2) == 0:
            cross_leg = not cross_leg

        if to_x < 0 and Puang.is_running:
            if cross_leg:
                Puang.character = Puang.img_lPuang_std
                
            else:
                Puang.character = Puang.img_lPuang_walk
            
        elif to_x > 0 and Puang.is_running:
            if cross_leg:
                Puang.character = Puang.img_rPuang_std
                
            else:
                Puang.character = Puang.img_rPuang_walk
                
        elif to_x == 0:
            if Puang.is_sight == 'left':
                Puang.character = Puang.img_lPuang_std
            else:
                Puang.character = Puang.img_rPuang_std
            
        
        
        
        # 캐릭터와 장애물 그리는 부분
        screen.blit(Puang.character, (Puang.posX, Puang.posY))
        for i in range(0,setup.Obstacle.count):
            if not obs_list[i].is_coll:
                screen.blit(obs_list[i].obstacle, (obs_list[i].posX, obs_list[i].posY))
            elif obs_list[i].is_coll and obs_list[i].sus_count < 15:
                screen.blit(effect.scene, (obs_list[i].posX, obs_list[i].posY))
                obs_list[i].sus_count += 1


        if play_val.is_Collision:
            if Puang.posX > obs_list[play_val.third_coll_num].posX and bub1_time < 30:
                screen.blit(bubble1.scene,(Puang.posX + Puang.width*0.7, Puang.posY - bubble1.height))
                bub1_time += 1


            elif Puang.posX > obs_list[play_val.third_coll_num].posX and bub2_time < 30:
                screen.blit(bubble2.scene,(Puang.posX + Puang.width*0.7, Puang.posY - bubble2.height))
                bub2_time += 1
                

            elif Puang.posX > obs_list[play_val.third_coll_num].posX and bub3_time < 30:
                screen.blit(bubble3.scene,(Puang.posX + Puang.width*0.7, Puang.posY - bubble3.height))
                bub3_time += 1

        
        
        py.display.update()
        
        

def draw_text(num):
    py.init()
    
    running = True

    stg3_D1 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_1.png"))
    stg3_D2 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_2.png"))
    stg3_D3 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_3.png"))
    stg3_D4 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_4.png"))
    stg3_D5 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_5.png"))
    stg3_D6 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_6.png"))
    stg3_D7 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_7.png"))
    stg3_D8 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_8.png"))
    stg3_D9 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_9.png"))
    stg3_D10 = setup.Scene(py.image.load("image\stage_3\stage3_hd_32_1_10.png"))
    
    if num != 1:
        cut_source.t_sound.play()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

            if event.type == py.KEYDOWN:

                if event.key == py.K_SPACE:
                    running = False

        if num == 1:
            screen.blit(stg3_D1.scene,(0,0))
            time.sleep(0.5)
        elif num == 2:
            screen.blit(stg3_D2.scene,(0,0))
            
        elif num == 3:
            screen.blit(stg3_D3.scene,(0,0))
        
        elif num == 4:
            screen.blit(stg3_D4.scene,(0,0))
            
        elif num == 5:
            screen.blit(stg3_D5.scene,(0,0))
        
        elif num == 6:
            screen.blit(stg3_D6.scene,(0,0))
            
        elif num == 7:
            screen.blit(stg3_D7.scene,(0,0))
        
        elif num == 8:
            screen.blit(stg3_D8.scene,(0,0))
            
        elif num == 9:
            screen.blit(stg3_D9.scene,(0,0))
        
        elif num == 10:
            screen.blit(stg3_D10.scene,(0,0))
        py.display.update()
