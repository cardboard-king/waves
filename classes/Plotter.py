##  NAME:           Plotter.py
##  TYPE:           class
##  AUTHOR:         Matthias
##  CREATED:        01.05.15
##  LAST MODIFIED:  01.05.15
#
##  SUMMARY:
##   Main program class for instantiating the program, handling events and updating the main loop
#
##  CLASS DESCRIPTION:
##      Member definitions:
##      - 
#
##      Member variables:
##      - 




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
        pygame.init()
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
