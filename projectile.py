# import pygame as pg
# import math
# win_x = 1600
# win_y = 800

# screen = pg.display.set_mode((win_x, win_y))

# posX = 10
# posY = 400

# v = 0
# t = 1
# u = 25
# theta = 55
# x = 0
# y = 0
# px = []
# py = []
# while(1):

#     screen.fill((255, 255, 255))
    
#     pg.draw.circle(screen,(255,0,0),(posX+x,posY-y),20)
#     px.append(posX+x)
#     py.append(posY-y)
#     for i in range(len(px)):
#         pg.draw.circle(screen,(255,0,0),(px[i],py[i]),3)
    
    
    
#     x = u * math.cos(math.radians(theta)) * t
#     y = (u * math.sin(math.radians(theta))*t) - (0.5*(t*t))
#     t += 1

#     if (posY-y >= win_y+55):
#         pg.quit()
#         exit()
#     pg.time.delay(50) #หน่วงเวลา

#     pg.display.update()
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

import pygame as pg
import math
from pygame.locals import *

win_x = 1600
win_y = 800

pg.init()
pg.font.init()

screen = pg.display.set_mode((win_x, win_y))

posX = 10
posY = 400

v = 0
t = 1
u = 25
theta = 20
x = 0
y = 0
px = []
py = []

# create an input box for theta
input_rect = pg.Rect(10, 10, 140, 32)
font = pg.font.SysFont(None, 32)
text = ''
color_active = pg.Color('lightskyblue3')
color_inactive = pg.Color('gray15')
color = color_inactive
active = False

# create start and stop buttons
start_button = pg.Rect(10, 50, 100, 50)
stop_button = pg.Rect(120, 50, 100, 50)
start_color = pg.Color('green')
stop_color = pg.Color('red')

running = False
stop = False

while True:

    screen.fill((255, 255, 255))

    # draw input box for theta
    pg.draw.rect(screen, color, input_rect, 2)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)

    # update theta value from input box
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            color = color_active if active else color_inactive
            # check if start/stop button is clicked
            if start_button.collidepoint(event.pos):
                running = True
                # stop = False
            if stop_button.collidepoint(event.pos):
                running = False
        if event.type == KEYDOWN:
            if active:
                if event.key == K_a:
                    try:
                        theta = int(text)
                        
                    except ValueError:
                        pass
                    text = ''
                elif event.key == K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # draw start and stop buttons
    pg.draw.rect(screen, start_color, start_button)
    pg.draw.rect(screen, stop_color, stop_button)
    start_text = font.render('Start', True, (255, 255, 255))
    stop_text = font.render('Clear', True, (255, 255, 255))
    screen.blit(start_text, (start_button.x+10, start_button.y+10))
    screen.blit(stop_text, (stop_button.x+10, stop_button.y+10))

    if running:
        # draw projectile motion
        pg.draw.circle(screen,(255,0,0),(posX+x,posY-y),20)
        px.append(posX+x)
        py.append(posY-y)
        for i in range(len(px)):
            pg.draw.circle(screen,(255,0,0),(px[i],py[i]),3)

        x = u * math.cos(math.radians(theta)) * t
        y = (u * math.sin(math.radians(theta))*t) - (0.5*(t*t))
        t += 1

        if (posY-y >= win_y+55):
            pg.quit()
            exit()
    # if stop:
    #     while (running != True):
    #         pg.draw.circle(screen,(255,0,0),(posX+x,posY-y),20)
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit()
    #             exit()
    #         if event.type == MOUSEBUTTONDOWN:
    #             if input_rect.collidepoint(event.pos):
    #                 active = True
    #             else:
    #                 active = False
    #             color = color_active if active else color_inactive
    #             # check if start/stop button is clicked
    #             if start_button.collidepoint(event.pos):
    #                 running = True
    #             if stop_button.collidepoint(event.pos):
    #                 stop = True
    #         if event.type == KEYDOWN:
    #             if active:
    #                 if event.key == K_a:
    #                     try:
    #                         theta = int(text)
                            
    #                     except ValueError:
    #                         pass
    #                     text = ''
    #                 elif event.key == K_BACKSPACE:
    #                     text = text[:-1]
    #                 else:
    #                     text += event.unicode


    pg.time.delay(50) #หน่
    pg.display.update()
