import heapq
import pygame
from settings import visited_color, final_path_color, start_color, goal_color


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
            reconstruct_path(came_from, end_node, win, grid.node_side, grid)
            return True
        # If the distance from the queue is greater, then we can skip it
        if current_dist > distances[current_node]:
            continue

        # --- Visualization ---
        if current_node != start_node and current_node != end_node:
            current_node.change_status(visited_color)
            grid.draw(win)
            pygame.display.update()
            pygame.time.delay(10) # A little delay for better representation

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