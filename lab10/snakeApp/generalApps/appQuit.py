import pygame
from sys import exit
from time import sleep
from random import randint
from snakeApp.generalApps.colors import *

from snakeApp.dbApps.saveData import saveData
from snakeApp.generalApps.drawGrid import drawGrid
from snakeApp.classes.snake import Snake
from snakeApp.classes.point import Point


def appQuit(_inner_data_, instantly=False):
    saveData(_inner_data_)

    if instantly:
        pygame.quit()
        exit()
    
    sleep(2)

    SCREEN = _inner_data_['screen']
    WIDTH = _inner_data_['width']
    HEIGHT = _inner_data_['height'] + 60
    BLOCK_SIZE = _inner_data_['block_size']
    GRID = pygame.Surface((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

    font = pygame.font.SysFont("Verdana", 30)
    map = _inner_data_['map']
    _inner_data_['map'] = 'map1.csv'
    _inner_data_['height'] = _inner_data_['height'] + 60
    _inner_data_['game_screen'] = GRID

    snakes = []
    for i in range(3):
        snakes.append(Snake(_inner_data_, randint(0, 40), randint(0, 30)))
        for j in range(5):
            snake = snakes[i].body
            snake.append(Point(snake[0].x, snake[0].y))
    
    text1 = font.render('If you want leave, press Q', True, (255, 255, 255))
    text2 = font.render('If you want restart game, press R', True, (255, 255, 255))
    
    small_screen = pygame.Surface((600, 200), pygame.SRCALPHA)
    small_screen.fill((0,0,0, 100))
    CHANGE_DIRECTION = pygame.USEREVENT + 1
    pygame.time.set_timer(CHANGE_DIRECTION, 3000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _inner_data_['map'] = map
                appQuit(_inner_data_, True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

            if event.type == CHANGE_DIRECTION:
                for snake in snakes:
                    event_key = randint(1, 4)
                    if event_key == 1:
                        if snake.dy == 0: continue
                        snake.dx = 1
                        snake.dy = 0
                    if event_key == 2:
                        if snake.dy == 0: continue
                        snake.dx = -1
                        snake.dy = 0
                    if event_key == 3:
                        if snake.dx == 0: continue
                        snake.dx = 0
                        snake.dy = -1
                    if event_key == 4:
                        if snake.dx == 0: continue
                        snake.dx = 0
                        snake.dy = 1
        
        SCREEN.fill((0,0,0))
        GRID.fill((0,0,0))
        drawGrid(SCREEN, GRID, WIDTH, HEIGHT, BLOCK_SIZE, BORDER_COLOR, 60)

        for snake in snakes:
            snake.move()
            snake.draw()

        SCREEN.blit(GRID, (0, 0))
        SCREEN.blit(small_screen, (100, 160))
        SCREEN.blit(text1, (195, 200))
        SCREEN.blit(text2, (140, 280))

        pygame.display.update()
        CLOCK.tick(6)