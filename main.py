import pygame as py
import pyautogui
import time

import start_menu
import end
import setup
import collision
import first_stage
import second_stage

first_c = 0
second_c = 0
# 시작 화면
start_menu.start_menu()


## 첫번째 스테이지
while first_c == 0 or collision.is_Collision:
    
    if first_stage.count_coll == 1 and not first_stage.end:
        first_stage.coll_1()            # 대사
        time.sleep(0.3)
    elif first_stage.count_coll == 2 and not first_stage.end:
        first_stage.coll_2()            # 대사
    elif first_stage.count_coll == 3 and not first_stage.end:
        first_stage.coll_3()            # 대사
        
    first_stage.first_stage()

    if first_stage.end:
        first_stage.coll_truck()        # 대사
        time.sleep(0.3)
        break
    first_stage.count_coll+=1
    first_c +=1
    
    
##두번째 스테이지

# 콘티 10 ~ 13번 삽입
while second_c == 0 or not second_stage.end:
    second_stage.second_stage()
    
    if second_stage.end:
        break

    if second_c == 0:
        second_stage.draw_text(4)           # 대사
        collision.second_stg_count += 1
    elif second_c == 1:
        second_stage.draw_text(5)           # 대사
        collision.second_stg_count += 1
    elif second_c == 2:
        second_stage.draw_text(6)           # 대사
        collision.second_stg_count += 1
    second_c += 1


## 세번째 스테이지

# 콘티 24 ~ 25번 삽입





end.ending()