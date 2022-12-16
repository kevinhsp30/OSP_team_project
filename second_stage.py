import pygame as py
import sys
import time
import random

import setup
import play_val
import cut_source


################### 두 번째 스테이지 파일 ###################


screen = setup.screen        # 사용자 모니터 해상도
screen_width = setup.screen_width
screen_height = setup.screen_height


def second_stage():
    py.init()
    global end
    end = False
    pass_9th_ob = False
    pass9 = 0
    temp_pass9 = 0
    screen = setup.screen        # 사용자 모니터 해상도
    screen_width = setup.screen_width
    screen_height = setup.screen_height
    
    # 인스턴스 생성 및 초기화
    Puang = setup.Character()

    # Puang.character = py.transform.scale(py.image.load("image\푸앙_사랑_look_right.png"), (Puang.width,Puang.height))
    bg_1 = setup.Background(py.image.load("image\stage1_bg.jpg"))
    bg_2 = setup.Background(py.image.load("image\stage2_bg.jpg"))
    bg_3 = setup.Background(py.image.load("image\stage3_bg.png"))

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
    land_obs = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*0.6 + screen_width)
    land_obs_2 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*1 + screen_width)

    land_obs_3 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*1.6 + screen_width)
    land_obs_4 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*2.1 + screen_width)

    land_obs_5 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*2.5 + screen_width)
    land_obs_6 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*3 + screen_width)

    land_obs_7 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*3.6 + screen_width)
    land_obs_8 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*4 + screen_width)

    land_obs_9 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*4.4 + screen_width)
    land_obs_10 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*4.9 + screen_width)

    land_obs_11 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*5.3 + screen_width)
    land_obs_12 = setup.Obstacle(py.image.load(type_obs[random.randrange(0,6)]),screen_width*5.6 + screen_width)
    
    ob_truck = setup.Obstacle(py.image.load("image\\truck_2.png"),screen_width*7 + screen_width)
    
    obs_list = setup.Obstacle.obs_list
    
    bubble1 = setup.Scene(py.image.load("image\stage2_bubble1.png"))
    bubble2 = setup.Scene(py.image.load("image\stage2_bubble2.png"))
    bubble3 = setup.Scene(py.image.load("image\stage2_bubble3.png"))
    bub1_time = 0
    bub2_time = 0
    bub3_time = 0


    # py.display.set_caption("1st_Stage")
    to_x, to_y = 0,0

    
    clock = py.time.Clock()
    
    # bg_1 = setup.Background(py.image.load("image\stage1_bg.png"))
    # land_obs = setup.land_obs
    # land_obs_2 = setup.land_obs_2
    # Puang = setup.Character()
    bg = bg_2
    
    play_val.is_Collision = False
    init_speed = 1
    count = 0
    distance = 0
    cross_leg = True
    temp_speed = 0
    ground = screen_height - Puang.posY
    running = True
    sound_count = 0
    
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
                quit()

            if event.type == py.KEYDOWN and not pass_9th_ob:
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


            if event.type == py.KEYUP and not pass_9th_ob:
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
      
            if Puang.posX  < (obs_list[i].posX + obs_list[i].width)- obs_list[i].width*0.2 and Puang.posX + Puang.width > obs_list[i].posX + obs_list[i].width*0.2:
                if Puang.posY + Puang.height > obs_list[i].posY + obs_list[i].height*0.2:
                    play_val.is_Collision = True
                    sound_count += 1
                    if i == 12:
                        end = True
                        
        # 충돌 사운드
        if sound_count%10 == 0 and play_val.is_Collision:
            play_val.coll_sound.play()
            
           
        if not play_val.is_Collision:
            speed = temp_speed
    
        if play_val.is_Collision:
            # for i in range(0,int(int(obs_list[0].width) /dt)):
            speed = temp_speed
            speed *= 0.1
            play_val.is_Collision = False
        

        # 9번째 장애물 확정 충돌
        if play_val.second_stg_count == 0:
            if obs_list[7].posX + obs_list[7].width < Puang.posX < obs_list[8].posX + obs_list[8].width and pass9 == 0:
                pass_9th_ob = True
                to_x += speed
                pass9 += 1
                
                temp_pass9 = pass9
            elif Puang.posX >= obs_list[8].posX + obs_list[8].width and temp_pass9 == pass9:
                pass_9th_ob = False
                draw_text(1)
                
                temp_pass9 += 1
            elif temp_pass9 == pass9+1:
                draw_text(2)
                
                temp_pass9 += 1
            elif temp_pass9 == pass9+2:
                draw_text(3)
                
                temp_pass9 += 1
            
            
        # 트럭 충돌
        if obs_list[len(obs_list)-2].posX + Puang.width*6 <= Puang.posX:
            ob_truck.posX -= speed
            if ob_truck.posX+ob_truck.width <= Puang.posX:
                ob_truck.posX -= speed
        
        
        # 트럭 충돌 시
        if end:
            coll_truck()
            time.sleep(0.5)
            break
        
        # 트럭 회피 시
        if ob_truck.posX+ob_truck.width < 0 and Puang.posY == screen_height - Puang.height - screen_height*0.1 and (-bg.posX) % bg.width <= speed : # 바닥:
            
            end = False
            break

        
    
        if Puang.posX > 0:
            distance += to_x
        print('distance = ', distance)
        
        
        for i in (0,1,2,3,4,5):
            screen.blit(bg.background, (bg.posX + bg.width* i, -screen_height*0.06))
        


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

        # 말풍선 생성
        if play_val.second_stg_count == 0:
            if Puang.posX > obs_list[1].posX and bub1_time < 45:
                screen.blit(bubble1.scene,(Puang.posX + Puang.width*0.7, Puang.posY - bubble1.height))
                bub1_time += 1


            if Puang.posX > obs_list[4].posX and bub2_time < 45:
                screen.blit(bubble2.scene,(Puang.posX + Puang.width*0.7, Puang.posY - bubble2.height))
                bub2_time += 1
                

            if Puang.posX > obs_list[7].posX and bub3_time < 45:
                screen.blit(bubble3.scene,(Puang.posX + Puang.width*0.7, Puang.posY - bubble3.height))
                bub3_time += 1


        py.display.update()
        
def draw_text(num):
    py.init()
    running = True
    # 9번째 장애물 후
    stg2_D1 = setup.Scene(py.image.load("image\Room2_3_D1.png"))
    stg2_D2 = setup.Scene(py.image.load("image\Room2_3_D2.png"))
    stg2_D3 = setup.Scene(py.image.load("image\Room2_3_D3.png"))
    
    # 트럭 회피 후
    stg2_D4 = setup.Scene(py.image.load("image\Room2_4_D1.png"))
    stg2_D5 = setup.Scene(py.image.load("image\Room2_4_D2.png"))
    stg2_D6 = setup.Scene(py.image.load("image\Room2_4_D3.png"))
    
    
    cut_source.t_sound.play()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

            if event.type == py.KEYDOWN:

                if event.key == py.K_SPACE:
                    running = False

        if num == 1:
            screen.blit(stg2_D1.scene,(0,0))
            time.sleep(0.3)
        elif num == 2:
            screen.blit(stg2_D2.scene,(0,0))
            
        elif num == 3:
            screen.blit(stg2_D3.scene,(0,0))
        
        
        elif num == 4:
            screen.blit(stg2_D4.scene,(0,0))
            
        elif num == 5:
            screen.blit(stg2_D5.scene,(0,0))
        
        elif num == 6:
            screen.blit(stg2_D6.scene,(0,0))
        py.display.update()

def coll_truck():
    
    py.init()
    running = True
    img = setup.Scene(py.image.load("image\Room2_5_D1.png"))
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
    

