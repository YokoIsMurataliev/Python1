from snakeApp.generalApps.drawGrid import drawGrid
from snakeApp.generalApps.colors import *

def mainDraw(_inner_data_, snake, wall, all_food, font):
    SCREEN = _inner_data_['screen']
    GAME_SCREEN = _inner_data_['game_screen']
    SCORE = _inner_data_['score']
    SPEED = _inner_data_['speed']
    WIDTH = _inner_data_['width']
    HEIGHT = _inner_data_['height']
    BLOCK_SIZE = _inner_data_['block_size']
    TOTAL_SCORE = _inner_data_['total_score']
    HIGHEST_SCORE = _inner_data_['highest_score']

    SCREEN.fill(GRAY)

    score = font.render('Score: ' + str(SCORE), True, WHITE)
    level = font.render('Speed level: ' + str(SPEED), True, WHITE)
    info = font.render('To pass the map, you need to get 70 points', True, WHITE)
    t_score = font.render('Total Score: ' + str(TOTAL_SCORE + SCORE), True, WHITE)
    h_score = font.render('Highest Score: ' + str(HIGHEST_SCORE), True, WHITE)

    SCREEN.blit(score, (10,8))
    SCREEN.blit(level, (10,25))
    SCREEN.blit(info, (200,8))
    SCREEN.blit(t_score, (600,8))
    SCREEN.blit(h_score, (600,25))

    GAME_SCREEN.fill(GRASS_COLOR)
    wall.draw()
    drawGrid(SCREEN, GAME_SCREEN, WIDTH, HEIGHT, BLOCK_SIZE, BORDER_COLOR)
    for food in all_food:
        food.draw()
    snake.draw()
    SCREEN.blit(GAME_SCREEN, (0, 60))