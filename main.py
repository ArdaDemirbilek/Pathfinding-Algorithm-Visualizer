import pygame
from settings import SIDE

WIN = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("A* Path Finding Algorithm")


def main():
    start, end = None, None
    run, started = True, False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()