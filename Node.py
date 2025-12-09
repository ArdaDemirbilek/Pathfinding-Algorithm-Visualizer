import pygame
from settings import walkable_color, start_color, goal_color, visited_color, frontier_color


class Node:
    def __init__(self, row, col, x, y):
        self.row = row # Row number of the Node
        self.col = col # Col number of the Node
        self.x = x # x Coordinate: row * (WIDTH / ROWS)
        self.y = y # y Coordinate: col * (WIDTH / ROWS)
        self.color = walkable_color
        self.neighbors = [0, 0, 0, 0] # 0 -> UP, 1 -> RIGHT, 2 -> DOWN, 3 -> LEFT

    def get_pos(self):
        """ Returns the row and column number of the node """
        return self.row, self.col

    def get_status(self):
        """ Returns number codes which indicates the current status of the node """
        if self.color == start_color: return 0
        elif self.color == goal_color: return 1
        elif self.color == visited_color: return 2
        elif self.color == frontier_color: return 3
        else: return 4 # walkable

    def change_status(self, color):
        """ Given the color input the function changes the color attribute to track
        the new status of the node """
        self.color = color

    def heuristic(self, other):
        """ Returns the Manhattan Distance between the nodes: self and other """
        node_x, node_y = self.get_pos()
        other_x, other_y = other.get_pos()
        return abs(node_x - other_x) + abs(node_y - other_y)

    def draw(self, win, side):
        """ The function which makes possible to draw each squares given its location and color """
        pygame.draw.rect(win, self.color, (self.x, self.y, side, side))