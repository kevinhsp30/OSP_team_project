import pygame as py
import sys
import time
import random

import setup
import play_val
import cut_source

count_coll = 0

screen = setup.screen        # 사용자 모니터 해상도
screen_width = setup.screen_width
screen_height = setup.screen_height

def first_stage():
    py.init()
    global end
    end = False
    screen = setup.screen        # 사용자 모니터 해상도
    screen_width = setup.screen_width
    screen_height = setup.screen_height
    # 인스턴스 생성 및 초기화
    Puang = setup.Character()

    # Puang.character = py.transform.scale(py.image.load("image\푸앙_사랑_look_right.png"), (Puang.width,Puang.height))
    bg_1 = setup.Background(py.image.load("image\stage1_bg.jpg"))
    bg_2 = setup.Background(py.image.load("image\stage2_bg.jpg"))
    bg_3 = setup.Background(py.image.load("image\stage3_bg.png"))

    bg = bg_1

    setup.Obstacle.count = 0
    setup.Obstacle.obs_list = []

    
    # 장애물 랜덤 생성
    ob_1 = "image\stage1_ob1.png"
    ob_2 = "image\stage1_ob2.png"
    ob_3 = "image\stage1_ob3.png"
    ob_4 = "image\stage1_ob4.png"
    ob_5 = "image\stage1_ob5.png"
    ob_6 = "image\stage1_ob6.png"
    type_obs = [ob_1,ob_2,ob_3,ob_4,ob_5,ob_6]
    # land_obs = setup.Obstacle(py.image.load("image\stage1_ob1.png"),setup.screen_width*1.3)
    # land_obs_2 = setup.Obstacle(py.image.load("image\stage1_ob2.png"),setup.screen_width*2)
    # land_obs_3 = setup.Obstacle(py.image.load("image\stage1_ob2.png"),setup.screen_width*3)
    land_obs = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*0.6)
    land_obs_2 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*1)

    land_obs_3 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*1.6)
    land_obs_4 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*2.1)

    land_obs_5 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*2.5)
    land_obs_6 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*3)

    land_obs_7 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*3.6)
    land_obs_8 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*4)

    land_obs_9 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*4.4)
    land_obs_10 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*4.9)

    land_obs_11 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*5.3)
    land_obs_12 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*5.6)
    
    ob_truck = setup.Obstacle(py.image.load("image\\truck.png"),screen_width*7)
    
    obs_list = setup.Obstacle.obs_list
    
    
    sc_con = setup.Scene(py.image.load("image\stg_1_con.png"))

    
    # py.display.set_caption("1st_Stage")
    to_x, to_y = 0,0

    
    clock = py.time.Clock()


    
    play_val.is_Collision = False
    init_speed = 1
    count = 0
    distance = 0
    cross_leg = True
    ground = screen_height - Puang.posY
    
    running = True
    while running:

        dt = clock.tick(15)
    
        # 속도 고정, 속도 오류 방지
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
                quit()

            if event.type == py.KEYDOWN and not end:
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

                elif event.key == py.K_SPACE and Puang.is_running and not end:
                    Puang.is_jumping = True
                    Puang.is_running = False


            if event.type == py.KEYUP and not end:
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
            if Puang.posY < ground/   0.47 :  # 점프 높이
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
      
            if Puang.posX  < (obs_list[i].posX + obs_list[i].width)- obs_list[i].width*0.2 and Puang.posX + Puang.width > obs_list[i].posX + obs_list[i].width*0.2:
                if Puang.posY + Puang.height > obs_list[i].posY + obs_list[i].height*0.2:
                    play_val.is_Collision = True
        if play_val.is_Collision == True:
            play_val.coll_sound.play()
            break

            
        # 트럭 충돌
        if obs_list[len(obs_list)-2].posX + Puang.width*6 <= Puang.posX:
            end = True
            Puang.posX += speed/2
            ob_truck.posX -= speed*4
            
            
        
        if Puang.posX > 0:
            distance += to_x
        print('distance = ', distance)
        
        
        # 배경 그리는 부분
        for i in (0,1,2,3,4,5):
            screen.blit(bg.background, (bg.posX + bg.width* i, -screen_height*0.06))
        
        # 조작 방법 창 그리기
        if play_val.first_stg_count < 60:
            screen.blit(sc_con.scene,(0,0))
            play_val.first_stg_count += 1
        
        
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
            
        
        # 캐릭터와 장해물 그리는 부분
        screen.blit(Puang.character, (Puang.posX, Puang.posY))
        for i in range(0,setup.Obstacle.count):
            screen.blit(obs_list[i].obstacle, (obs_list[i].posX, obs_list[i].posY))    
        # screen.blit(land_obs.obstacle, (land_obs.posX, land_obs.posY))
        # screen.blit(land_obs_2.obstacle, (land_obs_2.posX, land_obs_2.posY))
        py.display.update()




def coll_1():

    py.init()
    running = True
    stg1_D1 = setup.Scene(py.image.load("image\stg1_D1.png"))
    cut_source.t_sound.play()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

            if event.type == py.KEYDOWN:

                if event.key == py.K_SPACE:
                    running = False

    
    
        screen.blit(stg1_D1.scene,(0,0))
        py.display.update()
    

def coll_2():

    py.init()
    running = True
    stg1_D1 = setup.Scene(py.image.load("image\stg1_D2.png"))
    cut_source.t_sound.play()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

            if event.type == py.KEYDOWN:

                if event.key == py.K_SPACE:
                    running = False

    
    
        screen.blit(stg1_D1.scene,(0,0))
        py.display.update()
    

def coll_3():

    py.init()
    running = True
    stg1_D1 = setup.Scene(py.image.load("image\stg1_D3.png"))
    cut_source.t_sound.play()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

            if event.type == py.KEYDOWN:

                if event.key == py.K_SPACE:
                    running = False

    
    
        screen.blit(stg1_D1.scene,(0,0))
        py.display.update()
    

def coll_truck():
    
    py.init()
    running = True
    img = setup.Scene(py.image.load("image\stg1_D4_0.png"))
    cut_source.car_sound.play()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

            if event.type == py.KEYDOWN:

                if event.key == py.K_SPACE:
                    running = False

    

        screen.blit(img.scene,(0,0))
        py.display.update()

