import setup
import pygame
# 충돌함수 구현

pygame.init()

coll_sound = pygame.mixer.Sound('sound\collision.mp3')
# bgm = pygame.mixer.Sound('sound\달빛(Clair de Lune).mp3')


is_Collision = False

first_stg_count = 0

second_stg_count = 0



third_coll_num = 0



end_restart = False
end_exit = False

# a = setup.Obstacle(pygame.image.load("image\stage2_bubble1.png"))
# b = setup.Obstacle(pygame.image.load("image\stage2_bubble2.png"))
# c = setup.Obstacle(pygame.image.load("image\stage2_bubble3.png"))
# print(setup.Obstacle.obs_list)
# del setup.Obstacle.obs_list[0]
# print(setup.Obstacle.obs_list)
# setup.Obstacle.obs_list.insert(0,setup.Obstacle(pygame.image.load("image\stage2_bubble1.png")))
# del setup.Obstacle.obs_list[3]

# print(setup.Obstacle.obs_list)