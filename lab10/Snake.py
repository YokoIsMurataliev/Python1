import pygame
from time import sleep
from snakeApp.generalApps.colors import *

#______Импорт всех модулей______
from snakeApp.generalApps.appQuit import appQuit
from snakeApp.generalApps.mainDraw import mainDraw
from snakeApp.generalApps.registrationDraw import registrationDraw
from snakeApp.generalApps.food_eating import food_eating
from snakeApp.generalApps.keyboardWrite import keyboardWrite
from snakeApp.dbApps.executeData import executeData
from snakeApp.classes.snake import Snake
from snakeApp.classes.food import Food
from snakeApp.classes.wall import Wall


def main():
    pygame.init()

    #______Инициализация основных переменных______
    global HEIGHT, WIDTH, BLOCK_SIZE, SCREEN, GAME_SCREEN, name

    HEIGHT = 600
    WIDTH = 800
    BLOCK_SIZE = 20
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT + 60))
    GAME_SCREEN = pygame.Surface((WIDTH, HEIGHT))

    name = registrasion(SCREEN, HEIGHT, WIDTH)
    game()


def game():
    #______Инициализация внутренних переменных______
    CLOCK = pygame.time.Clock()
    map_done = False
    start = True
    isDrawn = False
    font = pygame.font.SysFont("Verdana", 15)
    db_data = executeData(name)
    _inner_data_ = {
        'screen': SCREEN,
        'game_screen': GAME_SCREEN,
        'height': HEIGHT,
        'width': WIDTH,
        'block_size': BLOCK_SIZE,

        'all_maps': ['map1.csv', 'map2.csv', 'map3.csv', 'map5.csv', 'map6.csv', 'map4.csv'],
        'score': 0,
        'speed': 0,
        'food_count': 2,

        'user_id': db_data[0],
        'total_score': int(db_data[2]),
        'highest_score': int(db_data[3]),
        'map': db_data[4]
    }

    #______Создание всех объектов______
    snake = Snake(_inner_data_)
    walls = Wall(_inner_data_)
    all_food = []
    for i in range(_inner_data_['food_count']):
        food = Food(_inner_data_, walls.body)
        all_food.append(food)

    #______Бесконечный цикл______
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                appQuit(_inner_data_, True)
            #______Смена направления движения______
            if event.type == pygame.KEYDOWN:
                if not isDrawn:
                    continue
                if event.key == pygame.K_RIGHT:
                    if snake.dy == 0: continue
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    if snake.dy == 0: continue
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    if snake.dx == 0: continue
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    if snake.dx == 0: continue
                    snake.dx = 0
                    snake.dy = 1
                isDrawn = False
        
        
        #______Движение змеи______
        snake.move()

        #______Проверка колизии с едой и ее обновновление со временем______
        _inner_data_ = food_eating(_inner_data_,snake, all_food)
        for food in all_food:
            food.timer_update()
        
        
        #______Проверка колизии с телом______
        for cell in snake.body[1:]:
            if snake.check_collision(cell):
                appQuit(_inner_data_)
                game()
        
        #______Проверка колизии со стеной______
        for wall in walls.body:
            if snake.check_collision(wall):
                appQuit(_inner_data_)
                game()
        
        #______Смена карты при достижении 'SCORE=70'______
        if not map_done and _inner_data_['score'] > 70:
            map_done = True
            all_maps = _inner_data_['all_maps']
            current_map = _inner_data_['map']
            for i in range(len(all_maps)):
                if all_maps[i] == current_map:
                    if i + 1 == len(all_maps):
                        _inner_data_['map'] = all_maps[0]
                    else:
                        _inner_data_['map'] = all_maps[i+1]
        
        #______Прорисовка всех деталей на экран______
        mainDraw(_inner_data_, snake, walls, all_food, font)
        isDrawn = True

        pygame.display.update()
        CLOCK.tick(6 + _inner_data_['speed'])

        if start: 
            sleep(1)
            start = False


    
#______Вызов экрана регистрации______
def registrasion(SCREEN, HEIGHT, WIDTH):
    name = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                appQuit(True)
            if event.type == pygame.KEYDOWN:
                name = keyboardWrite(event, name)
                if event.key == pygame.K_RETURN:
                    return name

        registrationDraw(SCREEN, name, HEIGHT, WIDTH)

main()
