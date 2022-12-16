import pygame as py
import pyautogui


# if __name__ == "__main__":


############### 화면 크기 조정 및 각종 클래스 정의 파일 ###################



# 사용자 모니터 크기 가져오기
M_size = pyautogui.size()
screen_width = M_size[0]
screen_height = M_size[1] - 70

# 화면 생성
screen = py.display.set_mode((screen_width, screen_height))



class Character:
    size = py.image.load("image\푸앙_사랑_look_right.png").get_rect().size
    width = size[0] * screen_width/1600 * 0.5            
    height = size[1] * screen_height/900 * 0.5           # 유저 모니터 해상도에 따라 캐릭터 크기 조정
    character = py.transform.scale(py.image.load("image\walk_1_r.png"), (width,height))
    img_rPuang_std = py.transform.scale(py.image.load("image\walk_1_r.png"), (width,height))
    img_rPuang_walk = py.transform.scale(py.image.load("image\walk2_r.png"), (width,height))
    img_lPuang_std = py.transform.scale(py.image.load("image\walk_1.png"), (width,height))
    img_lPuang_walk = py.transform.scale(py.image.load("image\walk2.png"), (width,height))
    posX = (screen_width/2) - (width/2)
    posY = screen_height - height - screen_height*0.1
    is_sight = "right"
    is_jumping = False
    is_running = True
    

    def trun_Char(self):
        if self.is_sight == "right":
            self.character =  self.img_lPuang_std # py.image.load("image\푸앙_사랑.png")
            self.is_sight = "left"
        elif self.is_sight == "left":
            self.character = self.img_rPuang_std # py.image.load("image\푸앙_사랑_look_right.png")
            self.is_sight = "right"

class Background:
    def __init__(self, image, posX = 0, upY = 0):
        self.size = image.get_rect().size
        self.width = self.size[0]* screen_width/1290 * 1.2
        self.height = self.size[1]* screen_height/730 * 1.2
        self.background = py.transform.scale(image, (self.width,self.height))
        self.size = self.background.get_rect().size
        self.posX = posX                                      # 왼쪽 끝에 맞춤
        self.posY = screen_height - self.height - upY    # 바닥에 맞춤
    # background = py.image.load("image\\68858716_p0.jpg")
              

class Obstacle:
    count = 0
    obs_list = []
    
    def __init__(self, image, posX = 0, posY = 0): # 제 1사분면에서의 좌표값
        self.size = image.get_rect().size
        self.width = self.size[0]* screen_width/1600
        self.height = self.size[1]* screen_height/900
        self.obstacle = py.transform.scale(image, (self.width,self.height))
        self.size = self.obstacle.get_rect().size
        self.posX = posX
        self.posY = screen_height - self.height - posY - screen_height*0.08
        Obstacle.count += 1
        self.obs_list.append(self)
        self.is_coll = False
        self.sus_count = 0
        

class Scene:
    def __init__(self, image, posx = 0, posy = 0):
        self.size = image.get_rect().size
        self.width = self.size[0]* screen_width/1290
        self.height = self.size[1]* screen_height/730
        self.scene = py.transform.scale(image, (self.width,self.height))
        self.size = self.scene.get_rect().size
        self.posX = posx   
        self.posY = posy

      
