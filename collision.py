import setup

# 충돌함수 구현
print(setup.obs_list[0].posX)


is_Collision = False
def check_collision(count):
    if (setup.obs_list[count].posX) < setup.Puang.posX < (setup.obs_list[count].posX + setup.obs_list[count].width) and 
    