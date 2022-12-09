import pygame as py
import sys
import time

import setup
import collision

def second_stage():
    py.init()
    
    # 인스턴스 생성 및 초기화
    Puang = setup.Character()

    # Puang.character = py.transform.scale(py.image.load("image\푸앙_사랑_look_right.png"), (Puang.width,Puang.height))
    bg_1 = setup.Background(py.image.load("image\stage1_bg.png"))
    bg_2 = setup.Background(py.image.load("image\stage2_bg.png"))
    bg_3 = setup.Background(py.image.load("image\stage3_bg.png"))

    setup.Obstacle.count = 0
    setup.Obstacle.obs_list = []
    # land_obs = setup.Obstacle(py.image.load("image\장애물_지상.png"),setup.screen_width*0.2)
    land_obs = setup.Obstacle(py.image.load("image\stage1_ob1.png"),setup.screen_width*1)
    land_obs_2 = setup.Obstacle(py.image.load("image\stage1_ob2.png"),setup.screen_width*2.3)
    # land_obs_3 = setup.Obstacle(py.image.load("image\stage1_ob2.png"),setup.screen_width*3)
 

    
    obs_list = setup.Obstacle.obs_list
    

    
    screen = setup.screen        # 사용자 모니터 해상도
    screen_width = setup.screen_width
    screen_height = setup.screen_height
    
    # py.display.set_caption("1st_Stage")
    to_x, to_y = 0,0

    
    clock = py.time.Clock()
    
    # bg_1 = setup.Background(py.image.load("image\stage1_bg.png"))
    # land_obs = setup.land_obs
    # land_obs_2 = setup.land_obs_2
    # Puang = setup.Character()
    bg = bg_2
    
    collision.is_Collision = False
    init_speed = 1
    count = 0
    distance = 0
    cross_leg = True
    temp_speed = 0
    
    running = True
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
            ground = screen_height - Puang.height
            Puang.posY -= speed
            if Puang.posY < ground - screen_height * 0.25:  # 점프 높이
                Puang.is_jumping = False

        # 높이를 지면에 고정(중력)
        if not Puang.is_jumping:
            Puang.posY += speed
            if Puang.posY > screen_height - Puang.height:
                Puang.posY = screen_height - Puang.height
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
                    collision.is_Collision = True
           
        if not collision.is_Collision:
            speed = temp_speed
                    
        if collision.is_Collision:
            # for i in range(0,int(int(obs_list[0].width) /dt)):
            speed = temp_speed
            speed *= 0.1
            collision.is_Collision = False
            
       
        
        
        if Puang.posX > 0:
            distance += to_x
        print('distance = ', distance)
        
        
        for i in (0,1,2,3,4):
            screen.blit(bg.background, (bg.posX + bg.width* i, 0))
        


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