# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import time

def save_font_pic(name):
	pygame.init()
	my_font = pygame.font.SysFont("arial", 64)
	my_name = name
	name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
	pygame.image.save(name_surface, "name.png")
# save_font_pic('hello, caogen')

def main():
	pygame.init()
	screen = pygame.display.set_mode((640, 480), 0, 32)
	 
	#font = pygame.font.SysFont("宋体", 40)
	#上句在Linux可行，在我的Windows 7 64bit上不行，XP不知道行不行
	#font = pygame.font.SysFont("simsunnsimsun", 40)
	#用get_fonts()查看后看到了这个字体名，在我的机器上可以正常显示了
	font = pygame.font.Font("simsun.ttc", 40)
	#这句话总是可以的，所以还是TTF文件保险啊
	text_surface = font.render(u"你好", True, (0, 0, 255))
	 
	x = 0
	y = (480 - text_surface.get_height())/2
	 
	background = pygame.image.load("sushiplate.jpg").convert()
	 
	while True:
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            sys.exit()
	 
	    screen.blit(background, (0, 0))
	 
	    x -= 2  # 文字滚动太快的话，改改这个数字
	    if x < -text_surface.get_width():
	        x = 640 - text_surface.get_width()
	 
	    screen.blit(text_surface, (x, y))
	 
	    pygame.display.update()

if __name__ == '__main__':
	main()