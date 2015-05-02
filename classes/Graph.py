import pygame
import numpy as np


WHITE = (255,255,255)
BLACK = (0,0,0)

class Graph:
    def __init__(self, rect, limits, data1, data2):
        self.rect = rect
        self.surface = pygame.Surface(self.rect.size)
        self.xlower = limits[0][0]
        self.xlength = limits[0][1] - limits[0][0]
        self.ylower = limits[1][0]
        self.ylength = limits[1][1] - limits[1][0]
        self.data1 = data1
        self.data2 = data2
        self.background = WHITE
    def create(self):
    	self.surface.fill(self.background)
    	self.draw_dots()
    	return self.surface
    def draw_dots(self):
    	for i in np.arange(self.data1.size):
    		pos = self.calculate_container_pixel(self.data1[i],self.data2[i])
    		self.surface.fill(BLACK,(pos,(2,2)))
    def draw_lines(self):
    	nextpos = self.calculate_container_pixel(self.data1[0],self.data2[0])
    	for i in np.arange(self.data1.size - 1):
    		pos = nextpos
    		nextpos = self.calculate_container_pixel(self.data1[i],self.data2[i])
    		pygame.draw.line(self.surface,BLACK,pos,nextpos)
    def calculate_container_pixel(self,xvalue,yvalue):
    	xnorm = float(xvalue)/float(self.xlength)
    	xfloat = xnorm*self.rect.width
    	xcoord = int(xfloat)
    	#
    	ynorm = yvalue/float(self.xlength)
    	yfloat = ynorm*self.rect.height
    	ycoord = self.rect.height - int(yfloat)
    	#
    	return (xcoord,ycoord)
    def get_background(self):
    	return self.background
