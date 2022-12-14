import setup
import pygame
# 충돌함수 구현



is_Collision = False


second_stg_count = 0



third_coll_num = 0



a = setup.Obstacle(pygame.image.load("image\stage2_bubble1.png"))
b = setup.Obstacle(pygame.image.load("image\stage2_bubble2.png"))
c = setup.Obstacle(pygame.image.load("image\stage2_bubble3.png"))
print(setup.Obstacle.obs_list)
del setup.Obstacle.obs_list[0]
print(setup.Obstacle.obs_list)
setup.Obstacle.obs_list.insert(0,setup.Obstacle(pygame.image.load("image\stage2_bubble1.png")))
del setup.Obstacle.obs_list[3]

print(setup.Obstacle.obs_list)