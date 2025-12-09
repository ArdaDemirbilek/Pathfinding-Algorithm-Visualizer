import heapq
import pygame
from settings import visited_color, final_path_color, start_color


def a_star(win, grid, start, end):
    """
    Computes the shortest path on the grid using the A* (A-Star) algorithm.
    Unlike Dijkstra, this method utilizes a heuristic function (Manhattan distance)
    to guide the search towards the target, making it generally faster.
    It expands nodes based on the lowest 'f_score' (cost so far + estimated cost),
    visualizing the exploration in real time. Once the target is reached, the
    path is reconstructed via the 'came_from' mapping. Returns True if a path
    exists, otherwise False.
    """
    # We are working on self.nodes2 (on the right side of the window)
    start_node = grid.nodes2[start[0]][start[1]]
    end_node = grid.nodes2[end[0]][end[1]]

    # g_score: The distance from the start node to a specific node "real distance"
    g_score = {node: float('inf') for row in grid.nodes2 for node in row}
    g_score[start_node] = 0 # From start node to start node distance = 0

    # f_score: g_score + heuristic. Estimated total distance using Manhattan Distance
    f_score = {node: float('inf') for row in grid.nodes2 for node in row}
    f_score[start_node] = start_node.heuristic(end_node) # start nodes g_score is already known

    pq = [(f_score[start_node], start[0], start[1])] # we will store it in ascending order of f_score
    came_from = {}

    while pq:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        # Pop the node with the least f_score (estimated distance to end node)
        current_f, r, c = heapq.heappop(pq)
        current_node = grid.nodes2[r][c]

        if (r, c) == end: # If we reach the end node
            # Draw the final path
            yield from reconstruct_path(came_from, end_node, win, grid.node_side, grid)
            return True

        # --- Visualization ---
        if current_node != start_node and current_node != end_node:
            current_node.change_status(visited_color)
            grid.draw(win)
            pygame.display.update()
            # pygame.time.delay(2) # For preferences the delay can be adjusted

        yield False

        # Visiting the neighbors
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i, direction in enumerate(directions):
            if current_node.neighbors[i] == 1: # If no barrier is found
                dr, dc = direction
                next_r, next_c = r + dr, c + dc
                # Edge Check
                if 0 <= next_r < grid.total_rows and 0 <= next_c < grid.total_rows:
                    neighbor_node = grid.nodes2[next_r][next_c]
                    temp_g_score = g_score[current_node] + 1 # Add 1 since its unweighted

                    # If we manage to reach the node through a shorter path
                    if temp_g_score < g_score[neighbor_node]:
                        came_from[neighbor_node] = current_node
                        g_score[neighbor_node] = temp_g_score
                        # f = g + h
                        f_score[neighbor_node] = temp_g_score + neighbor_node.heuristic(end_node)
                        heapq.heappush(pq, (f_score[neighbor_node], next_r, next_c))

    return False # If no path can be found


def dijkstra_unweighted(win, grid, start, end):
    """
    Computes the shortest path on an unweighted grid using Dijkstra's algorithm.
    Expands nodes in order of increasing distance, updating the frontier through
    a priority queue and visualizing visited nodes in real time. Once the target
    is reached, the path is reconstructed via the 'came_from' mapping. Returns
    True if a path exists, otherwise False.
    """
    distances = {node: float('inf') for row in grid.nodes1 for node in row}
    start_node = grid.nodes1[start[0]][start[1]] # start = row, col
    end_node = grid.nodes1[end[0]][end[1]] # end = row, col
    distances[start_node] = 0 # The distance from start_node to start_node is 0

    pq = [(0, start[0], start[1])] # Drop the start_node in priority queue
    came_from = {}
    while pq:
        # Get the element with the least distance from the priority queue
        current_dist, r, c = heapq.heappop(pq)
        current_node = grid.nodes1[r][c]
        if (r, c) == end: # If we reach the destination
            yield from reconstruct_path(came_from, end_node, win, grid.node_side, grid)
            return True
        # If the distance from the queue is greater, then we can skip it
        if current_dist > distances[current_node]:
            continue

        # --- Visualization ---
        if current_node != start_node and current_node != end_node:
            current_node.change_status(visited_color)
            grid.draw(win)
            pygame.display.update()
            # pygame.time.delay(2) # For preferences the delay can be adjusted

        # After the visualization is done we go back to main function
        yield False

        # Visiting Neighbors
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (row_change, col_change)
        for i, direction in enumerate(directions):
            if current_node.neighbors[i] == 1:
                dr, dc = direction
                next_r, next_c = r + dr, c + dc
                # Border Check (maze generator does it, but for further security)
                if 0 <= next_r < grid.total_rows and 0 <= next_c < grid.total_rows:
                    neighbor_node = grid.nodes1[next_r][next_c]
                    new_dist = current_dist + 1

                    # If a new, shorter road to neighbor_node is found, push it to priority queue
                    if new_dist < distances[neighbor_node]:
                        distances[neighbor_node] = new_dist # Cache the new shorter distance is distances dict
                        heapq.heappush(pq, (new_dist, next_r, next_c))
                        # Shows through which node can this node be reached in shortest
                        came_from[neighbor_node] = current_node

    return False # If no path can be found


def reconstruct_path(came_from, current, win, node_side, grid):
    """ Traverses back to find the shortest path """
    while current in came_from:
        current = came_from[current]
        if current.color != start_color: # Don't color the start node
            current.change_status(final_path_color)
            # current.draw(win, node_side)
            grid.draw(win)
            pygame.display.update()
            yield True