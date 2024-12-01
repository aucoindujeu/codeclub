import pgzero
import random
import time

WIDTH = 800
HEIGHT = 800

CELL_SIZE = 10
CELL_COUNT_X = WIDTH // CELL_SIZE
CELL_COUNT_Y = HEIGHT // CELL_SIZE
CELLS = {(x, y): 0 for x in range(0, CELL_COUNT_X) for y in range(0, CELL_COUNT_Y)}

FPS = 4
PAUSE_GAME = False



def draw_vertical_line(x, y, length):
    for y2 in range(y, y + length):
        CELLS[(x, y2)] = 1

def draw_r_penthomino(x, y):
    # r-penthomino (methuselah) https://en.wikipedia.org/wiki/File:Game_of_life_fpento.svg
    CELLS[(x, y)] = 1
    CELLS[(x + 1, y)] = 1
    CELLS[(x - 1, y + 1)] = 1
    CELLS[(x, y + 1)] = 1
    CELLS[(x, y + 2)] = 1


def draw_random_pattern():
    for x in range(CELL_COUNT_X):
        for y in range(CELL_COUNT_Y):
            CELLS[(x, y)] = random.randint(0, 2)


# draw_vertical_line(CELL_COUNT_X // 2, CELL_COUNT_Y // 2 - 10, 8)
# draw_r_penthomino(WIDTH // (2 * CELL_SIZE), HEIGHT // (2 * CELL_SIZE))
draw_random_pattern()


def draw():
    screen.fill((0, 0, 0))
    for x in range(0, WIDTH, CELL_SIZE):
        screen.draw.line((x, 0), (x, HEIGHT), (255, 255, 255))
    for y in range(0, HEIGHT, CELL_SIZE):
        screen.draw.line((0, y), (WIDTH, y), (255, 255, 255))

    for x in range(CELL_COUNT_X):
        for y in range(CELL_COUNT_Y):
            if CELLS[(x, y)] == 1:
                screen.draw.filled_rect(
                    Rect(
                        (x * CELL_SIZE, y * CELL_SIZE),
                        (CELL_SIZE, CELL_SIZE),
                    ),
                    (255, 255, 255),
                )


def update():
    if PAUSE_GAME:
        return

    time.sleep(1 / FPS)

    new_cells = CELLS.copy()

    for x in range(CELL_COUNT_X):
        for y in range(CELL_COUNT_Y):
            live_neighbours = 0
            for x2, y2 in [
                (x - 1, y - 1),
                (x - 1, y),
                (x - 1, y + 1),
                (x, y - 1),
                (x, y + 1),
                (x + 1, y - 1),
                (x + 1, y),
                (x + 1, y + 1),
            ]:
                x2 = x2 % CELL_COUNT_X
                y2 = y2 % CELL_COUNT_Y
                if CELLS[(x2, y2)] == 1:
                    live_neighbours += 1

            # https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules
            if CELLS[(x, y)] == 1 and live_neighbours < 2:
                new_cells[(x, y)] = 0
            elif CELLS[(x, y)] == 1 and live_neighbours > 3:
                new_cells[(x, y)] = 0
            elif CELLS[(x, y)] == 0 and live_neighbours == 3:
                new_cells[(x, y)] = 1

    CELLS.update(new_cells)


def on_key_down(key):
    if key == keys.SPACE or key == keys.P:
        global PAUSE_GAME
        PAUSE_GAME = not PAUSE_GAME


def on_mouse_down(pos):
    # mouse click
    toggle_life(pos)


def on_mouse_move(pos, buttons):
    if mouse.LEFT in buttons:
        # mouse dragged
        toggle_life(pos)


def toggle_life(pos):
    x = pos[0] // CELL_SIZE
    y = pos[1] // CELL_SIZE
    CELLS[(x, y)] = 0 if CELLS[(x, y)] == 1 else 1
