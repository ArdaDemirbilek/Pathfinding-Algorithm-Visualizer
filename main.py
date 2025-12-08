import pygame
from settings import SIDE, ROWS
from Grid import Grid
from algorithms import dijkstra_unweighted

WIN = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("A* Path Finding Algorithm")


def main():
    start, end = None, None
    run, started = True, False
    grid = Grid()
    grid.make_grid()
    maze_generated = False
    while run:
        grid.draw(WIN) # At each entry to the loop we revisualize the grid
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0] and not maze_generated:
                # We need to generate the maze only one time -> 'maze_generated' flag
                grid.maze_generator()
                maze_generated = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and maze_generated:
                    dijkstra_unweighted(WIN, grid, (0,0), (ROWS-1, ROWS-1))


    pygame.quit()

if __name__ == "__main__":
    main()