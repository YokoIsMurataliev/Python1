from pygame.draw import rect

def drawScroll(body, total_height, HEIGHT, WIDTH, scroll):
    rect(body, (150, 150, 150), (WIDTH - 20, 0, 20, HEIGHT))
    scroll_height = int((HEIGHT - 60) * (HEIGHT - 60) / total_height)
    scroll_pos = int((scroll * (HEIGHT - 60 - scroll_height)) / (total_height - HEIGHT + 60))
    rect(body, (100, 100, 100), (WIDTH - 20, scroll_pos, 20, scroll_height))
