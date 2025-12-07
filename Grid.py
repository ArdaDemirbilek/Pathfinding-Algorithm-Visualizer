import pygame
from Node import Node

WIDTH = 800
ROWS = 50

class Grid:
    def __init__(self):
        self.side = WIDTH
        self.total_rows = ROWS
        self.node_side = WIDTH / ROWS
        self.nodes = []

    def make_grid(self):
        for i in range(self.total_rows):
            self.nodes.append([])
            for j in range(self.total_rows):
                self.nodes[i].append(Node(i, j, i*self.node_side, j*self.node_side))
