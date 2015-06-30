# -*- coding: utf-8 -*-
background_image_filename = '../res/sushiplate.jpg'
sprite_image_filename = '../res/fugu.png'
 
import pygame
from pygame.locals import *
from sys import exit
from vector2 import Vector2
 
pygame.init()
 
screen = pygame.display.set_mode((640, 480), 0, 32)
 
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
 
clock = pygame.time.Clock()
 
sprite_pos = Vector2(200, 150)
sprite_speed = 100.
 
while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
 
    screen.blit(background, (0,0))
    screen.blit(sprite, sprite_pos)

    pressed_keys = pygame.key.get_pressed()
 
    key_direction = Vector2(0, 0)
    if pressed_keys[K_a]:
        key_direction.x = -1
    elif pressed_keys[K_d]:
        key_direction.x = +1
    if pressed_keys[K_w]:
        key_direction.y = -1
    elif pressed_keys[K_s]:
        key_direction.y = +1
 
    key_direction.normalize()
 
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
 
    sprite_pos+= key_direction * sprite_speed * time_passed_seconds
 
    pygame.display.update()
