import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf

def run_game():
	#创建一个屏幕对象
	pygame.init()
	
	ai_settings = Settings()
	#设置窗口大小
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	#设置窗口的标题
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings,screen)
	bullets = Group()
	alien = Alien(ai_settings,screen)
	while True:
		#监听键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,alien,bullets)
run_game()