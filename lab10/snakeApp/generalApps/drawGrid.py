from pygame import Rect, draw

def drawGrid(SCREEN, GAME_SCREEN, WIDTH, HEIGHT, BLOCK_SIZE, BORDER_COLOR, starting_pos=0):
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            draw.rect(GAME_SCREEN, BORDER_COLOR, rect, 1)
    SCREEN.blit(GAME_SCREEN, (0, 60-starting_pos))