import pygame
import sys
import time

import setup
black = (0,0,0)
k_space = False
k_click = False
d_sound = False
w_count = 0
# screen = pygame.display.set_mode((1280, 720))
screen = setup.screen

pygame.init()
R00 = setup.Scene(pygame.image.load('image\Room0_0.png'))
R01 = setup.Scene(pygame.image.load('image\Room0_1.png'))
R020 = setup.Scene(pygame.image.load('image\Room0_2_0.png'))
R31 = setup.Scene(pygame.image.load('image\Room3_1.png'))
Re1 = setup.Scene(pygame.image.load('image/32_4.png'))
Re2 = setup.Scene(pygame.image.load('image/32_6.png'))
RD1 =  setup.Scene(pygame.image.load('image\Room0_D1.png'))
RD2 =  setup.Scene(pygame.image.load('image\Room0_D2.png'))
RD3 =  setup.Scene(pygame.image.load('image\Room0_D3.png'))
RD4 =  setup.Scene(pygame.image.load('image\Room0_D4.png'))
RD5 =  setup.Scene(pygame.image.load('image\Room0_D5.png'))
RD6 =  setup.Scene(pygame.image.load('image\Room0_D6.png'))
RD21 = setup.Scene(pygame.image.load('image\Room2_D1.png'))
RD22 = setup.Scene(pygame.image.load('image\Room2_D2.png'))
RD23 = setup.Scene(pygame.image.load('image\Room2_D3.png'))
RD24 = setup.Scene(pygame.image.load('image\Room2_D4.png'))
RD25 = setup.Scene(pygame.image.load('image\Room2_D5.png'))
RD26 = setup.Scene(pygame.image.load('image\Room2_D6.png'))
RD27 = setup.Scene(pygame.image.load('image\Room2_D7.png'))
RD31 = setup.Scene(pygame.image.load('image\Room3_D1.png'))
RD32 = setup.Scene(pygame.image.load('image\Room3_D2.png'))
RD33 = setup.Scene(pygame.image.load('image\Room3_D3.png'))
NS = setup.Scene(pygame.image.load('image\Room2_5_D1.png'))
endd1 = setup.Scene(pygame.image.load('image/31_1_1.png'))
endd2 = setup.Scene(pygame.image.load('image/31_1_2.png'))
endd3 = setup.Scene(pygame.image.load('image/31_1_3.png'))
t_sound = pygame.mixer.Sound('audio/talk.mp3')
ns_sound = pygame.mixer.Sound('audio/ns.mp3')
end_sound = pygame.mixer.Sound('audio/end.mp3')
car_sound = pygame.mixer.Sound('audio/end_c.mp3')
def sleep():
    screen.blit(R00.scene,(0,0)) 
    pygame.display.flip()     
def sleep2():
    screen.blit(R31.scene,(0,0)) 
    pygame.display.flip()  
def room1():
    screen.blit(R01.scene,(0,0))
    pygame.display.flip()
def room2():
    screen.blit(R020.scene,(0,0))
    pygame.display.flip()
def room3():
    screen.blit(R31.scene,(0,0))
    pygame.display.flip()
def ns():
    screen.blit(NS.scene,(0,0))
    pygame.display.flip()
def d1():
    screen.blit(RD1.scene,(0,0))
    pygame.display.flip()
def d2():
    screen.blit(RD2.scene,(0,0))
    pygame.display.flip()
def d3():
    screen.blit(RD3.scene,(0,0))
    pygame.display.flip()
def d4():
    screen.blit(RD4.scene,(0,0))
    pygame.display.flip()
def d5():
    screen.blit(RD5.scene,(0,0))
    pygame.display.flip()
def d6():
    screen.blit(RD6.scene,(0,0))
    pygame.display.flip()
def d21():
    screen.blit(RD21.scene,(0,0))
    pygame.display.flip()
def d22():
    screen.blit(RD22.scene,(0,0))
    pygame.display.flip()
def d23():
    screen.blit(RD23.scene,(0,0))
    pygame.display.flip()
def d24():
    screen.blit(RD24.scene,(0,0))
    pygame.display.flip()
def d25():
    screen.blit(RD25.scene,(0,0))
    pygame.display.flip()
def d26():
    screen.blit(RD26.scene,(0,0))
    pygame.display.flip()
def d27():
    screen.blit(RD27.scene,(0,0))
    pygame.display.flip()
def d31():
    screen.blit(RD31.scene,(0,0))
    pygame.display.flip()
def d32():
    screen.blit(RD32.scene,(0,0))
    pygame.display.flip()
def d33():
    screen.blit(RD33.scene,(0,0))
    pygame.display.flip()
def end1():
    screen.blit(endd1.scene,(0,0))
    pygame.display.flip()
def end2():
    screen.blit(endd2.scene,(0,0))
    pygame.display.flip()
def end3():
    screen.blit(endd3.scene,(0,0))
    pygame.display.flip()
def hid_end1():
    screen.blit(Re1.scene,(0,0))
    pygame.display.flip()
def hid_end2():
    screen.blit(Re2.scene,(0,0))
    pygame.display.flip()
    