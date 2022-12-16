import pygame as py
import pyautogui
import time

import start_menu
import end
import setup
import play_val
import first_stage
import second_stage
import third_stage
import Cut


################### 메인 실행 파일 ###################




# 시작 화면
start_menu.start_menu()

while True:
    first_c = 0
    second_c = 0
    play_val.first_stg_count = 0
    play_val.second_stg_count = 0
    play_val.end_restart = False
    play_val.end_exit = False
    first_stage.count_coll = 0
    
    
    
    
    # collision.bgm.play()          배경음악
    
    Cut.cut1()

    ## 첫 번째 스테이지

    while first_c == 0 or play_val.is_Collision:
        
        if first_stage.count_coll == 1 and not first_stage.end:
            first_stage.coll_1()            # 대사
            time.sleep(0.5)
        elif first_stage.count_coll == 2 and not first_stage.end:
            first_stage.coll_2()            # 대사
        elif first_stage.count_coll == 3 and not first_stage.end:
            first_stage.coll_3()            # 대사
            
        first_stage.first_stage()

        if first_stage.end:
            first_stage.coll_truck()        # 대사
            time.sleep(2)
            break
        first_stage.count_coll+=1
        first_c +=1


        
    ## 두 번째 스테이지

    # 콘티 10 ~ 13번
    Cut.cut2()

    while second_c == 0 or not second_stage.end:
        second_stage.second_stage()
        
        if second_stage.end:
            break

        if second_c == 0:
            second_stage.draw_text(4)           # 대사
            play_val.second_stg_count += 1
        elif second_c == 1:
            second_stage.draw_text(5)           # 대사
            play_val.second_stg_count += 1
        elif second_c == 2:
            second_stage.draw_text(6)           # 대사
            play_val.second_stg_count += 1
        second_c += 1



    ## 세 번째 스테이지

    # 콘티 24 ~ 25번
    Cut.cut3()

    third_stage.third_stage()

    if third_stage.is_coll_truck:
        Cut.cut_end()
        end.ending()
        
    elif not third_stage.is_coll_truck:
        for i in range(1,11):
            third_stage.draw_text(i)
        Cut.hid_end_cut()
        end.hid_ending()

    if play_val.end_restart:
        pass
    elif play_val.end_exit:
        break
    
    