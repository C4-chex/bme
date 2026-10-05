
import pygame

import random



pygame.init()
pygame.joystick.init()
fps = pygame.time.Clock()
is_running = True
over = False
last_time = 0
font = pygame.font.SysFont(None, 48)



if pygame.joystick.get_count() == 0:
    print("未检测到手柄")
    exit()
joy = pygame.joystick.Joystick(0)

main_ui = pygame.display.set_mode((1000, 800))



x0 = random.randrange(100, 901,20)
y0 = random.randrange(100, 701,20)
dir_x0 = random.choice([-1, 0, 1])
x = x0
y = y0





if dir_x0 == 0:
    dir_y0 = random.choice([-1, 1])
else:
    dir_y0 = 0

direction = pygame.Vector2(dir_x0, dir_y0)
speed = 20
D =('east', 'north', 'south', 'west')
class Director:
    def __init__(self, d):
        self.direction = d

Head = Director(random.choice(D))

def move():
    if direction.x == 1 and direction.y == 0:
        Head.direction = 'east'


    elif direction.x == 0 and direction.y == -1:
        Head.direction = 'north'
    elif direction.x == 0 and direction.y == 1:
        Head.direction = 'south'
    elif direction.x == -1 and direction.y == 0:
        Head.direction = 'west'


def Aapple():
    while True:
        x1 = random.randrange(0, 1000, 20)
        y1 = random.randrange(0, 800, 20)
        apple = pygame.Rect(x1, y1, 20, 20)
        have = False

        for i in snake:
            if apple.colliderect(i):
                have = True
                break

        if not have:
            return apple




def restart():
    global snake, direction, Head, apple, over, last_time
    x0 = random.randrange(100, 901, 20)
    y0 = random.randrange(100, 701, 20)
    dx = random.choice([-1, 0, 1])
    if dx == 0:
        dy = random.choice([-1, 1])
    else:
        dy = 0
    direction = pygame.Vector2(dx, dy)
    Head = Director(random.choice(('east', 'north', 'south', 'west')))
    snake = [pygame.Rect(x0, y0, 20, 20)]
    apple = Aapple()
    last_time = pygame.time.get_ticks()
    over = False


dt = fps.tick(60)/1000.0
length = 1

snake = [pygame.Rect(x0, y0, 20, 20)]


apple = Aapple()

while is_running:
    main_ui.fill((0, 0, 0))




    now = pygame.time.get_ticks()
    if now - last_time >= 200:

        last_time = now
        snake_new = pygame.Rect(snake[0].x + direction.x * speed, snake[0].y + direction.y * speed, 20, 20)
        snake.insert(0, snake_new)



        if snake[0].colliderect(apple):
            apple = Aapple()
        else:
            snake.pop()



    if  snake[0].x < 0 or snake[0].x > 980 or snake[0].y < 0 or snake[0].y > 780:
        over = True


    pygame.draw.rect(main_ui, pygame.Color('red'), apple)

    if snake[0].collidelist(snake[1:]) != -1:
        over =True

    for seg in snake:
        pygame.draw.rect(main_ui, pygame.Color('green'), seg)

    text = font.render(f'length: {len(snake)}', True, (255, 255, 255))
    main_ui.blit(text, (10, 10))

    if over:
        over_text = font.render('press A to restart', True, (255, 255, 255))
        over_rect = over_text.get_rect(center=(500, 400))
        main_ui.blit(over_text, over_rect)

    events = pygame.event.get()
    fps.tick(60)




    move()

    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
            continue

        if event.type == pygame.JOYBUTTONDOWN:
            if over == True:
                if event.button == 0:
                    restart()
            else:
                if event.button == 0:
                    if Head.direction != 'north':
                        direction.x = 0
                        direction.y = 1
                        move()
                elif event.button == 3:
                    if Head.direction != 'south':
                            direction.x = 0
                            direction.y = -1
                            move()

                elif event.button == 2:
                    if Head.direction != 'east':
                            direction.x = -1
                            direction.y = 0
                            move()


                elif event.button == 1:
                    if Head.direction != 'west':
                            direction.x = 1
                            direction.y = 0
                            move()

    pygame.display.flip()



pygame.quit()