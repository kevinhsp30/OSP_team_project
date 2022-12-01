import pygame as py
import pyautogui

# if __name__ == "__main__":

# 사용자 모니터 크기 가져오기
M_size = pyautogui.size()
screen_width = M_size[0]
screen_height = M_size[1] - 60

# 화면 생성
screen = py.display.set_mode((screen_width, screen_height))


class Character:
    character = py.image.load("image\푸앙_사랑_look_right.png")
    size = character.get_rect().size
    width = size[0]
    height = size[1]
    posX = (screen_width/2) - (width/2)
    posY = screen_height - height
    is_sight = "right"
    is_jumping = False
    is_running = True

    def trun_Char(self):
        if self.is_sight == "right":
            self.character = py.image.load("image\푸앙_사랑.png")
            self.is_sight = "left"
        elif self.is_sight == "left":
            self.character = py.image.load("image\푸앙_사랑_look_right.png")
            self.is_sight = "right"
            

class Background:
    def __init__(self, image, posX = 0, upY = 0):
        self.background = image
        self.size = self.background.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.posX = posX                                      # 왼쪽 끝에 맞춤
        self.posY = screen_height - self.height - upY         # 바닥에 맞춤
    # background = py.image.load("image\\68858716_p0.jpg")
    
                           

class Obstacle:
    obstacle = py.image.load("image\장애물_지상.png")
    size = obstacle.get_rect().size
    width = size[0]
    height = size[1]
    posX = screen_width - screen_width/8
    posY = screen_height - height

