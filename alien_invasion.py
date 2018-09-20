import sys
import pygame

def run_game():
	#创建一个屏幕对象
	pygame.init()
	#设置窗口大小
	screen = pygame.display.set_mode((990,660))
	#设置窗口的标题
	pygame.display.set_caption("Alien Invasion")
	
	while True:
		#监听键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#让最近绘制的屏幕可见
		pygame.display.flip()
run_game()