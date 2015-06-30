# -*- coding: utf-8 -*-
background_image_filename = '../res/sushiplate.jpg'
sprite_image_filename = '../res/fugu.png'
 
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
 
screen = pygame.display.set_mode((640, 480), 0, 32)
 
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
 
# Clock����
clock = pygame.time.Clock()
 
x = 0.
# �ٶȣ�����/�룩
speed = 25.
 
while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
 
    screen.blit(background, (0,0))
    screen.blit(sprite, (x, 100))    
 
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
 
    distance_moved = time_passed_seconds * speed
    x += distance_moved
 
    # ��һ�£������ȥ640��ֱ�ӹ����кβ�ͬ��
    if x > 640.:
        x -= 640.    
 
    pygame.display.update()