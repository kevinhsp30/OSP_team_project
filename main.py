import pygame as py
import pyautogui

import start_menu
import setup
import collision
import first_stage
import second_stage

first_c = 0

# 시작 화면
start_menu.start_menu()


# 첫번째 스테이지
while first_c == 0 or collision.is_Collision:
    
    first_stage.first_stage()
    
    first_c +=1
    
# 두번째 스테이지
second_stage.second_stage()