# region Colors

background_color      = (15, 15, 26)
grid_color            = (40, 40, 60)
wall_color            = (52, 152, 219)
walkable_color        = (25, 25, 38)
start_color           = (46, 204, 113)
goal_color            = (231, 76, 60)
visited_color         = (41, 128, 185)
frontier_color        = (241, 196, 15)
final_path_color      = (236, 240, 241)

# endregion


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

