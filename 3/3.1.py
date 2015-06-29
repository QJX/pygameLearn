# -*- coding: utf-8 -*- 
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480) 
Fullscreen = False
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background_image_filename = 'sushiplate.jpg'
# background = pygame.image.load(background_image_filename).convert()
 
while True:
    # event = pygame.event.wait()
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((640, 480), 0, 32)
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            pygame.display.set_caption("Window resized to "+str(event.size))
        
        # screen_width, screen_height = SCREEN_SIZE
        # 这里需要重新填满窗口
        # for y in range(0, screen_height, background.get_height()):
        #     for x in range(0, screen_width, background.get_width()):
        #         screen.blit(background, (x, y))
        # screen.blit(background, (0,0))
        screen.fill((255,255,255))
        pygame.display.update()