import pygame as py
import pyautogui

import start_menu
import setup
import collision
import first_stage


# screen_width = M_size[0]
# screen_height = M_size[1] - 70
# screen = py.display.set_mode((screen_width, screen_height))
# background = py.image.load("흰색 이미지.png")

# screen = setup.screen        # 사용자 모니터 해상도
# screen_width = setup.screen_width
# screen_height = setup.screen_height


# 시작 화면
start_menu.start_menu()


# Puang = setup.Character()
# Puang = setup.Puang


# bg_1 = setup.bg_1
# bg_2 = setup.bg_2
# bg_3 = setup.bg_3


# land_obs = setup.land_obs
# land_obs_2 = setup.land_obs_2
# is_Collision = False
first_c = 0



# 첫번째 스테이지

while first_c == 0 or collision.is_Collision:
    
    first_stage.first_stage()
    
    first_c +=1
    
