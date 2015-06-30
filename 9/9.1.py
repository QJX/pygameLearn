# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
import math
# from gameobjects.vector2 import Vector2

class Vector2(tuple):
    def __new__(typ, x=1.0, y=1.0):
        # print(typ, x, y)
        n = tuple.__new__(typ, (int(x), int(y)))
        n.x = x
        n.y = y
        return n

    # def __init__(self, x=1.0, y=1.0):
    #     print(self)

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def __add__(self, other):
        return self.__new__(type(self), self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return self.__new__(type(self), self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return self.__new__(type(self), self.x*other, self.y*other)

    def __div__(self, other):
        print('.=======div==========')
        return self.__new__(type(self), self.x/other, self.y/other)

    def __floordiv__(self, other):
        print('.=======floordiv==========')
        return self.__new__(type(self), self.x/other, self.y/other)

    def __truediv__(self, other):
        print('.=======truediv==========')
        return self.__new__(type(self), self.x/other, self.y/other)

    @staticmethod
    def from_points(P1, P2):
        return Vector2( P2[0] - P1[0], P2[1] - P1[1] )

    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )
        
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
 
background_image_filename = '../res/sushiplate.jpg'
sprite_image_filename = '../res/fugu.png'

pygame.init()
 
screen = pygame.display.set_mode((640, 480), 0, 32)
 
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
 
clock = pygame.time.Clock()
 
position = Vector2(100.0, 100.0)
heading = Vector2()
# print(type(position), position)
 
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
 
    screen.blit(background, (0,0))
    screen.blit(sprite, position)
 
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
 
    # 参数前面加*意味着把列表或元组展开
    destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size())/2
    # 计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vector2.from_points(position, destination)
    # 向量规格化
    vector_to_mouse.normalize()
 
    # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
    # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。
    heading = heading + (vector_to_mouse * .6)    
 
    position += heading * time_passed_seconds
    pygame.display.update()