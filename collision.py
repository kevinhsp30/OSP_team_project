import setup

# 충돌함수 구현
# print(setup.obs_list[0].posX)


is_Collision = False

def check_collision(count):
    if setup.Puang.posX <= (setup.obs_list[count].posX + setup.obs_list[count].width) and setup.Puang.posX + setup.Puang.width >= setup.obs_list[count].posX:
        if setup.Puang.posY + setup.Puang.height >= setup.obs_list[count].height:
            is_Collision = True
    