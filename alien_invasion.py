import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#创建一个屏幕对象
	pygame.init()
	
	ai_settings = Settings()
	#设置窗口大小
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	#设置窗口的标题
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(screen)
	
	while True:
		#监听键盘和鼠标事件
		gf.check_events(ship)
		gf.update_screen(ai_settings,screen,ship)
run_game()