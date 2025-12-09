import pygame
from settings import HEIGHT, WIDTH, ROWS, HEIGHT
from Grid import Grid
from algorithms import dijkstra_unweighted, a_star

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Algorithm Visualizer")


def main():
    algo1 = None  # Dijkstra
    algo2 = None  # A*
    run = True
    start_node, end_node = (0,0), (ROWS-1, ROWS-1)
    grid = Grid()
    grid.make_grid(start_node, end_node)
    maze_generated, pathfinding_started = False, False
    while run:
        grid.draw(WIN) # At each entry to the loop we revisualize the grid
        # If the pathfinding started we simulate the algorithms
        if pathfinding_started:
            try:
                if algo1: next(algo1)
            except StopIteration:
                algo1 = None

            try:
                if algo2: next(algo2)
            except StopIteration:
                algo2 = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0] and not maze_generated and not pathfinding_started:
                # We need to generate the maze only one time -> 'maze_generated' flag
                grid.maze_generator()
                maze_generated = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and maze_generated and not pathfinding_started:
                    pathfinding_started = True
                    algo1 = dijkstra_unweighted(WIN, grid, (0,0), (ROWS-1, ROWS-1))
                    algo2 = a_star(WIN, grid, (0,0), (ROWS-1, ROWS-1))

    pygame.quit()

if __name__ == "__main__":
    main()