import pygame
from settings import SIDE, ROWS
from Grid import Grid
from Node import Node

WIN = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("A* Path Finding Algorithm")


def main():
    start, end = None, None
    run, started = True, False
    grid = Grid()
    while run:
        grid.draw_template(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()