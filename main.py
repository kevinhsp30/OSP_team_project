import pygame as py
import pyautogui

import start_menu
import setup
import collision

py.init()

# screen_width = M_size[0]
# screen_height = M_size[1] - 70
# screen = py.display.set_mode((screen_width, screen_height))
# background = py.image.load("흰색 이미지.png")

screen = setup.screen        # 사용자 모니터 해상도
screen_width = setup.screen_width
screen_height = setup.screen_height


# 시작 화면
start_menu.start_menu()


'''
class Character:
    size = py.image.load("image\푸앙_사랑_look_right.png").get_rect().size
    width = size[0] * screen_width/1290 * 0.7            
    height = size[1] * screen_height/730 * 0.7           # 유저 모니터 해상도에 따라 캐릭터 크기 조정
    character = py.transform.scale(py.image.load("image\푸앙_사랑_look_right.png"), (width,height))
    img_rPuang = py.transform.scale(py.image.load("image\푸앙_사랑_look_right.png"), (width,height))
    img_lPuang = py.transform.scale(py.image.load("image\푸앙_사랑.png"), (width,height))
    posX = (screen_width/2) - (width/2)
    posY = screen_height - height
    is_sight = "right"
    is_jumping = False
    is_running = True

    def trun_Char(self):
        if self.is_sight == "right":
            self.character =  self.img_lPuang # py.image.load("image\푸앙_사랑.png")
            self.is_sight = "left"
        elif self.is_sight == "left":
            self.character = self.img_rPuang # py.image.load("image\푸앙_사랑_look_right.png")
            self.is_sight = "right"
'''

'''
class Background:
    def __init__(self, image, posX = 0, upY = 0):
        self.size = image.get_rect().size
        self.width = self.size[0]* screen_width/1290 * 1.2
        self.height = self.size[1]* screen_height/730 * 1.2
        self.background = py.transform.scale(image, (self.width,self.height))
        self.size = self.background.get_rect().size
        self.posX = posX                                      # 왼쪽 끝에 맞춤
        self.posY = screen_height - self.height - upY         # 바닥에 맞춤
    # background = py.image.load("image\\68858716_p0.jpg")
'''
                           

"""
class Obstacle:
    count = 0
    def __init__(self, image, posX = 0, posY = 0): # 제 1사분면에서의 좌표값
        self.size = image.get_rect().size
        self.width = self.size[0]* screen_width/1600
        self.height = self.size[1]* screen_height/900
        self.obstacle = py.transform.scale(image, (self.width,self.height))
        self.size = self.obstacle.get_rect().size
        self.posX = posX
        self.posY = screen_height - self.height - posY
        Obstacle.count += 1
"""

    # obstacle = py.image.load("image\장애물_지상.png")
    # size = obstacle.get_rect().size
    # width = size[0]
    # height = size[1]
    # posX = screen_width - screen_width/8
    # posY = screen_height - height



# 인스턴스 생성
# Puang = Character()

# Puang.character = py.transform.scale(py.image.load("image\푸앙_사랑_look_right.png"), (Puang.width,Puang.height))
# bg_1st = setup.Background(py.image.load("image\stage1_bg.png"))
# bg_2st = setup.Background(py.image.load("image\stage2_bg.png"))
# bg_3st = setup.Background(py.image.load("image\stage3_bg.png"))


# land_obs = setup.Obstacle(py.image.load("image\장애물_지상.png"),screen_width*0.5)
# land_obs_2 = setup.Obstacle(py.image.load("image\장애물_지상.png"),screen_width*1.5)
# # land_obs.obstacle = py.image.load("image\장애물_지상.png")

Puang = setup.Character()
Puang = setup.Puang


bg_1st = setup.bg_1st
bg_2st = setup.bg_2st
bg_3st = setup.bg_3st

land_obs = setup.land_obs
land_obs_2 = setup.land_obs_2



py.display.set_caption("1st_Stage")
to_x, to_y = 0,0

bg = setup.bg_3st
clock = py.time.Clock()


init_speed = 1
count = 0
distance = 0
walk_interval = 0
cross_leg = True

# 이벤트 루프
running = True
while running:

    dt = clock.tick(200)

    # 속도 고정
    # 속도 변화 전처리 or 후처리 결정 필요
    if count < 20:
        temp_speed = init_speed
        temp_speed *= dt
        speed = temp_speed
        count += 1
    
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
        if Puang.posY < ground - screen_height * 0.17:
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



    ### 장애물 이동 (장애물 생성시 하나하나 작성해 주어야 함)
    if Puang.posX < (screen_width/2) - (Puang.width/2):
        bg.posX = 0
        Puang.posX += to_x
        land_obs.posX += to_x
        land_obs_2.posX += to_x




    # 배경과 장애물 이동
    # 원근감 표현
    bg.posX -= to_x/2
    land_obs.posX -= to_x
    land_obs_2.posX -= to_x


    # 충돌 확인
    # for i in range(0,len(setup.obs_list)):
    #     collision.check_collision(i)
    # if collision.is_Collision == True:
    #     break
    if Puang.posX > 0:
        distance += to_x
    print('distance = ', distance)
    
    
    for i in (0,1,2,3,4):
        screen.blit(bg.background, (bg.posX + bg.width* i, 0))
    

    temp_distance = distance
    if temp_distance%speed !=0:
        temp_distance -= temp_distance%speed
        
    if temp_distance%(speed*25) == 0:
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
        
        
    screen.blit(Puang.character, (Puang.posX, Puang.posY))
    screen.blit(land_obs.obstacle, (land_obs.posX, land_obs.posY))
    screen.blit(land_obs_2.obstacle, (land_obs_2.posX, land_obs_2.posY))
    py.display.update()


py.quit()