import pygame

WIDTH = 800
ROWS = 50

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

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