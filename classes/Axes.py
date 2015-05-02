##	NAME:			Axes.py
##	TYPE:			class
##	AUTHOR:			Matthias
##	CREATED:		01.05.15
##	LAST MODIFIED:	01.05.15
#
##	SUMMARY:
##	 A class which handles graph objects and overlay to graph surfaces
#
##	CLASS DESCRIPTION:
##		Member definitions:
##		- constructor:	surface | __init__ 	| .
#
##		Member variables:
##		- 


import pygame
import Graph
import numpy as np

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (50,50,50)
xoff = 10
yoff = 10

class Axes:
    def __init__(self, rect):
    	self.background = WHITE
    	self.axescolor = BLACK
    	self.xtick_inside = 2
    	self.xtick_outside = 2
    	self.ytick_inside = 2
    	self.ytick_outside = 2
    	self.rect = rect
    	self.surface = pygame.Surface(rect.size)
    	self.surface.fill(self.background)
    	self.graphrect = rect
    	self.graphrect.width -= xoff
    	self.graphrect.height -= yoff
    	self.graphrect = self.graphrect.move(xoff,0)
    def add_graph(self,limits,data1,data2):
    	self.graph = Graph.Graph(self.graphrect,limits,data1,data2)
    	self.graphsurf = self.graph.create()
    	self.graphsurf.set_colorkey(self.graph.get_background())
    	self.surface.blit(self.graphsurf,self.graphrect.topleft)
    def get_axes(self):
    	return self.surface
    def add_axes(self,limits,ticks):
    	pygame.draw.line(self.surface,self.axescolor,self.graphrect.topleft,self.graphrect.bottomleft)
    	pygame.draw.line(self.surface,self.axescolor,self.graphrect.bottomleft,self.graphrect.bottomright)
    	xlim = limits[0]
    	ylim = limits[1]
    	xtick = ticks[0]
    	ytick = ticks[1]
    	xtickn = np.floor((xlim[1] - xlim[0])/xtick) + 1
    	ytickn = np.floor((ylim[1] - ylim[0])/ytick) + 1
    	xticks = np.linspace(xlim[0],xtick*xtickn,xtickn)
    	yticks = np.linspace(ylim[0],ytick*ytickn,ytickn)
    	# need to implement drawtick usage
    def drawxtick(self,coords):
    	for coord in coords:
	    	xset = coord
    		yset1 = self.graphrect.bottom - self.xtick_inside
    		yset2 = self.graphrect.bottom + self.xtick_outside
    		start = (xset,yset1)
    		stop = (xset,yset2)
    		pygame.draw.line(self.surface,self.axescolor,start,stop)
    def drawytick(self,coords):
    	for coord in coords:
	    	yset = coord
    		xset1 = self.graphrect.left - self.ytick_outside
    		xset2 = self.graphrect.left + self.ytick_inside
    		start = (xset1,yset)
    		stop = (xset2,yset)
    		pygame.draw.line(self.surface,self.axescolor,start,stop)
    def calc_tick_coord(self,value,v_range,v_off,a_range):
    	return int((value-v_off)/v_range*a_range)



