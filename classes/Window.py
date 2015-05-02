import pygame
from pygame.locals import *
import sys, os
import platform

class Window:
	def __init__(self):
		if platform.system() == 'Darwin':
			os.environ['SDL_VIDEODRIVER'] = 'x11'
		pygame.init()
		self.surface = pygame.display.set_mode()
	def check_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
	def get_rect(self):
		return self.surface.get_rect()
	def draw(self,new_surface):
		self.surface.blit(new_surface,(0,0))
		pygame.display.update()
	def draw_region(self,new_region,region_rect):
		self.surface.blit(new_region,region_rect)
		pygame.display.update(region_rect)

