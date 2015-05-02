from classes.Window import Window
from classes.Graph import Graph
from data.COLORS import *
import pygame
import numpy as np

window = Window()
x = np.linspace(0,1,100)
y = x
graphrect = window.get_rect()
graphrect.size = (500,500)
graph = Graph(graphrect,((0,1),(0,1)),x,y)
window.draw(graph.create())

while True:
	window.check_events()


