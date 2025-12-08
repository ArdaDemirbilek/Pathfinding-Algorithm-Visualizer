import pygame, random
from Node import Node
from settings import SIDE, ROWS
from settings import background_color, wall_color, walkable_color, visited_color, final_path_color, start_color, goal_color

class Grid:
    def __init__(self):
        self.side = SIDE
        self.total_rows = ROWS
        self.node_side = SIDE / ROWS
        self.nodes = []

    def make_grid(self, start_node, end_node):
        """ Fills the self.nodes attribute by creating default Node Objects with row, column numbers
        and x,y coordinates """
        for i in range(self.total_rows):
            self.nodes.append([])
            for j in range(self.total_rows):
                # Column shifting is made possible by j*self.node_size
                # Row shifting is made possible by i*self.node_size
                self.nodes[i].append(Node(i, j, j*self.node_side, i*self.node_side))
        row1, col1 = start_node
        self.nodes[row1][col1].color = start_color
        row2, col2 = end_node
        self.nodes[row2][col2].color = goal_color

    def draw(self, win):
        """Draws the grid:
        - Fills background
        - Draws each cell with its current color (walkable / visited / path / start / goal)
        - Draws maze walls based on the neighbors array
        """
        win.fill(background_color)
        s = self.node_side
        for row in self.nodes:
            for node in row:
                node.draw(win, s) # Fill each nodes' area with walkable_color

        # Draw the Edges
        for row in self.nodes:
            for node in row:
                x, y = node.x, node.y
                r, c = node.row, node.col

                # UP: 0
                if node.neighbors[0] == 0: # = 0 means that there is a wall inbetween
                    pygame.draw.line(win, wall_color,
                    (x, y), (x + s, y), width=2)
                # LEFT: 3
                if node.neighbors[3] == 0: # = 0 means that there is a wall inbetween
                    pygame.draw.line(win, wall_color,
                    (x, y), (x, y + s), width=2)
                # DOWN: 2
                if r == self.total_rows - 1 and node.neighbors[2] == 0:
                    pygame.draw.line(win, wall_color,
                    (x, y + s), (x + s, y + s), width=2)
                # RIGHT: 1
                if c == self.total_rows - 1 and node.neighbors[1] == 0:
                    pygame.draw.line(win, wall_color,
                                     (x + s, y), (x + s, y + s), width=2)
        pygame.display.update()

    def maze_generator(self):
        """ Generates a maze structure by modifying the neighbors of each node.
        This method implements the Iterative Backtracking algorithm (using a stack).
        It visits every node in the grid to create a 'Perfect Maze' where:
        1. Every cell is reachable.
        2. There are no loops.
        3. Walls are represented by the state of 'neighbors'.
        The resulting structure is suitable for pathfinding algorithms like A* and Dijkstra. """
        current = self.nodes[0][0]
        visited_nodes, cache = {current}, [current]
        while len(visited_nodes) < self.total_rows*self.total_rows:
            move = [0, 1, 2, 3]
            while True: # Try different moves until no more moves exist
                if not move: # If no more move exist
                    if cache:
                        current = cache.pop() # Try to use cache for an alternative node
                        break
                    else: # If no node exist in cache we must terminate
                        return
                choice = random.choice(move)
                moved = False

                # 0: UP
                if choice == 0:
                    if current.row > 0: # current.row = 0 means we are already at the top
                        target = self.nodes[current.row - 1][current.col] # The node at the top
                        if target not in visited_nodes:
                            # If it is not visited, break the barriers of current and target
                            current.neighbors[0] = 1
                            target.neighbors[2] = 1
                            cache.append(current)
                            current = target
                            visited_nodes.add(current)
                            moved = True

                # 1: RIGHT
                elif choice == 1:
                    # current.col = len(self.nodes[0]) - 1 means we are at the far right
                    if current.col < len(self.nodes[0]) - 1:
                        target = self.nodes[current.row][current.col + 1] # The node at the right
                        if target not in visited_nodes:
                            # If it is not visited, break the barriers of current and target
                            current.neighbors[1] = 1
                            target.neighbors[3] = 1
                            cache.append(current)
                            current = target
                            visited_nodes.add(current)
                            moved = True

                # 2: DOWN
                elif choice == 2:
                    # current.row = len(self.nodes) - 1 means we are at the bottom
                    if current.row < len(self.nodes) - 1:
                        target = self.nodes[current.row + 1][current.col] # The node at the bottom
                        if target not in visited_nodes:
                            # If it is not visited, break the barriers of current and target
                            current.neighbors[2] = 1
                            target.neighbors[0] = 1
                            cache.append(current)
                            current = target
                            visited_nodes.add(current)
                            moved = True

                # 3: LEFT
                elif choice == 3:
                    # current.col = 0 means we are at the far left
                    if current.col > 0:
                        target = self.nodes[current.row][current.col - 1] # The node at the left
                        if target not in visited_nodes:
                            # If it is not visited, break the barriers of current and target
                            current.neighbors[3] = 1
                            target.neighbors[1] = 1
                            cache.append(current)
                            current = target
                            visited_nodes.add(current)
                            moved = True

                if moved:
                    break  # We moved already, we are ready to exit the loop
                else:
                    move.remove(choice)  # We haven't moved, delete that direction and continue
