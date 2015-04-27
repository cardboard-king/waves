# imports
import numpy as np
import pygame
from pygame.locals import *
import sys

# DEFINITIONS DEFINITIONS DEFINITIONS DEFINITIONS DEFINITIONS DEFINITIONS DEFINITIONS


def acceleration_operator(function, speed, diff_order):
    diff1 = numeric_diff(function, diff_order)
    diff2 = numeric_mydiff(diff1, diff_order)
    result = np.zeros(function.size)
    np.put(result, np.arange(1, diff2.size), diff2)
    result = result*float(speed**2)
    return result
    
def gaussian( mu, sig, start, stop, datapoints):
    x = np.linspace(start, stop, datapoints)
    return np.exp(-np.power(x - mu,  2.)/(2*np.power(sig, 2.)))
    
def start_data_function(mode, parameters):
    values = {
        'zeros'         : np.zeros(parameters[0]), 
        'gaussian' : gaussian(parameters[3], parameters[4], parameters[1], parameters[2], parameters[0])
    }[mode]
    return values
    
class axes:
    def __init__(self):
        pass

class graph:
    def __init__(self):
        pass

class Plotter:
    def __init__(self, surface, colors):
        fpsClock = pygame.time.Clock()
        pygame.display.set_caption('Plotter')
        self.window = surface
        self.sound = False
        self.bg_color = colors[0]
        self.ax_color = colors[1]
        self.vmargin = 50
        self.hmargin = 50
        self.top = self.vmargin
        self.bottom = self.window.get_height() - self.vmargin
        self.mid_vert = self.top + (self.bottom - self.top)/2
        self.left = self.hmargin
        self.right = self.window.get_width() - self.hmargin
        self.ax_width = 1
        self.triag_wing = 3
        self.triag_h = 5
        self.axes_set = False
        self.graph_set = False
        self.transparent = (0, 0, 0, 0)
    def get_values(self, values):
        self.data = values
    def update(self):
        pass
    def listen(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.sound = True
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    self.sound = False
    def heard(self):
        result = self.sound
        return result
    def make_axes(self):
        self.ax = pygame.Surface(self.window.get_size(), flags=pygame.SRCALPHA)
        self.make_x_axes()
        self.make_y_axes()
        self.axes_set = True
    def make_x_axes(self):
        pygame.draw.line(self.ax, self.ax_color, (self.left, self.mid_vert), (self.right, self.mid_vert), self.ax_width)
        pygame.draw.polygon(self.ax, self.ax_color, [[self.right, self.mid_vert + self.triag_wing], [self.right, self.mid_vert - self.triag_wing], [self.right + self.triag_h, self.mid_vert]])
    def make_y_axes(self):
        pygame.draw.line(self.ax, self.ax_color, (self.left, self.top), (self.left, self.bottom), self.ax_width)
        pygame.draw.polygon(self.ax, self.ax_color, [[self.left + self.triag_wing, self.top], [self.left - self.triag_wing, self.top], [self.left, self.top - self.triag_h]])
    def add_graph(self, xrange, yrange):
        self.gr = pygame.Surface(self.window.get_size(), flags=pygame.SRCALPHA)
        self.xmin = xrange[0]
        self.xmax = xrange[1]
        self.ymin = yrange[0]
        self.ymax = yrange[1]
        self.graph_set = True
    def plot_data(self):
        self.gr.fill(self.transparent)
        for i in range(self.data.size):
            value = self.data[i]
            fac1 = i+1
            fac2 = float(self.data.size + 1)
            fac3 = self.right - self.left
            fac4 = self.left
            x_pos = (fac1/fac2)*fac3 + fac4
            x_pos = int(round(x_pos))
            if value < self.ymin:
                value = self.ymin
            elif value > self.ymax:
                value = self.ymax
            y_pos = (self.ymax - value)/(self.ymax - self.ymin)*(self.bottom - self.top) + self.top
            y_pos = int(round(y_pos))
            pygame.draw.circle(self.gr, self.ax_color, (x_pos, y_pos), 1)
    def update(self):
        self.window.fill(self.bg_color)
        if self.axes_set:
            self.window.blit(self.ax, (0, 0))
        if self.graph_set:
            self.window.blit(self.gr, (0, 0))
    def refresh(self):
        self.update()
        pygame.display.update()

        
class Datamanager:
    def __init__(self, data):
        self.data = data
        self.speed = np.zeros(data.size)
        self.acceleration = np.zeros(data.size)
    def give_data(self):
        return self.data
    def calculate(self, c_speed):
        self.data += self.speed
        self.speed += self.acceleration
        self.acceleration = acceleration_operator(self.data, c_speed)

# constants
BLACK = pygame.Color(0, 0, 0, 255)
GREEN = pygame.Color(0, 255, 0, 255)
colors = (BLACK, GREEN)

# changeable values
datapoint_number = 1000
mu = 50
sig = 10
x_start = 0
x_stop = 100
speed = 1
mode='zeros'
parameters = (datapoint_number, x_start, x_stop, mu, sig)

# initialization
pygame.init()

plotter = Plotter( colors)
plotter.add_axes()
plotter.add_plot(0, (-1, 1), (-10, 10))
plotter.add_axes()
plotter.add_plot(1, (-1, 1), (-10, 10))

x = np.linspace(x_start, x_stop, datapoint_number)
start_data  = start_data_function('gaussian', parameters) 

endind = start_data.size - 1
start_data[endind] = 0 
datamanager = Datamanager(start_data)
plotter.get_values(datamanager.give_data())
plotter.plot_data()

if __name__ == "__main__":
    plotter = Plotter()
    # program loop
    while True:
        if plotter.heard():
            datamanager.calculate(speed)
            plotter.get_values(datamanager.give_data())
            plotter.plot_data()
        plotter.update()
        plotter.listen()
        plotter.refresh()
        fpsClock.tick(30)



