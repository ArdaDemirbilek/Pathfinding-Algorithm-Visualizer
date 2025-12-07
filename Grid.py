import pygame
from Node import Node
from settings import SIDE, ROWS, background_color, grid_color

class Grid:
    def __init__(self):
        self.side = SIDE
        self.total_rows = ROWS
        self.node_side = SIDE / ROWS
        self.nodes = []

    def make_grid(self):
        for i in range(self.total_rows):
            self.nodes.append([])
            for j in range(self.total_rows):
                self.nodes[i].append(Node(i, j, i*self.node_side, j*self.node_side))

    def draw_template(self, win):
        win.fill(background_color)
        # Each node is drawn
        for row in self.nodes:
            for node in row:
                node.draw(win, self.node_side)
        for i in range(self.total_rows):  # Vertical Lines of the Grid
            pygame.draw.line(win, grid_color,
                             (0, i * self.node_side), (self.side, i * self.node_side))
            for j in range(self.total_rows):  # Horizontal Lines of the Grid
                pygame.draw.line(win, grid_color,
                                 (j * self.node_side, 0), (j * self.node_side, self.side))
        pygame.display.update()

