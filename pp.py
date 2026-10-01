

import pygame_gui
import pygame
import random


L =('north','south','east','west')

#界面设置部分
pygame.init()
main_ui = pygame.display.set_mode((1000, 800))
manager = (pygame_gui.UIManager((1000, 800)))



#蛇部分
x0 = random.randint(100,901)
y0 = random.randint(100,701)
#方向随机
dir_x0 = random.choice([-1,0,1])
while True:

    if dir_x0 == 0:
        dir_y0 = random.choice([-1,1])
    elif dir_x0 !=0:
        dir_y0 = 0
    break



Head_color = pygame.Color('green')
direction = pygame.Vector2(dir_x0,dir_y0)
speed = 20


#apple部分






#运动函数
class director:
    def __init__(self,direction)->None:
        self.direction = direction
Head=director(direction)
def Move():
    if direction.x ==1 and direction.y == 0:
        Head.direction = 'east'
    elif direction.x ==0 and direction.y ==-1:
        Head.direction = 'south'
    elif direction.x ==0 and direction.y ==1:
        Head.direction = 'north'
    elif direction.x ==-1 and direction.y == 0:
        Head.direction = 'west'
Move()

fps = pygame.time.Clock()
is_running = True


while True:
    events = pygame.event.get()

    fps.tick(60)
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
        if event.ev_type != 'Sync':
            if event.code == 'BTN_SOUTH':
                if Head.direction != 'north':
                    direction.x = 0
                    direction.y = -1
            elif event.code == 'BTN_NORTH':
                if Head.direction != 'south':
                    direction.x = 0
                    direction.y = 1
            elif event.code == 'BTN_WEST':
                if Head.direction != 'east':
                    direction.x = -1
                    direction.y = 0
            elif event.code == 'BTN_EAST':
                if Head.direction != 'west':
                    direction.x = 1
                    direction.y = 0















