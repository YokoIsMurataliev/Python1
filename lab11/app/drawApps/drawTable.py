from pygame.draw import line

def drawTable(SCREEN, cell_height, BODY_HEIGHT, WIDTH, row_count, scroll):
    height = 40 - int((cell_height - 22)/ 4)

    line(SCREEN, (200, 200, 200), (200, 0), (200, BODY_HEIGHT))
    for i in range(row_count + 1):
        line(SCREEN, (200, 200, 200), (0, height - scroll), (WIDTH, height - scroll))
        height += cell_height