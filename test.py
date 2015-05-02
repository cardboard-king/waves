from classes.Window import Window
from classes.Axes import Axes
from data.COLORS import *
import pygame
import numpy as np

window = Window()
xlim = (0,1)
x = np.linspace(xlim[0],xlim[1],100)
y = x
ylim = (np.min(y),np.max(y))
rect = window.get_rect()
rect.size = (500,500)
axes = Axes(rect)
axes.add_graph((xlim,ylim),x,y)
axes.add_axes((xlim,ylim),(0.1,0.2))
window.draw(axes.get_axes())

while True:
	window.check_events()


