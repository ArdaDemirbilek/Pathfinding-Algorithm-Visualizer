import pygame
from Node import Node
from settings import SIDE, ROWS

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
