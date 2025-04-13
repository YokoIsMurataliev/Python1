from pygame import Rect, draw
from snakeApp.classes.point import Point
from snakeApp.generalApps.colors import SNAKE_BODY, SNAKE_HEAD

class Snake:
    def __init__(self, _inner_data_, point_x = 20, point_y = 15):
        self.body = [Point(point_x, point_y)]
        self.dx = 1
        self.dy = 0

        self.SCREEN = _inner_data_['screen']
        self.GAME_SCREEN = _inner_data_['game_screen']
        self.HEIGHT = _inner_data_['height']
        self.WIDTH = _inner_data_['width']
        self.BLOCK_SIZE = _inner_data_['block_size']

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if (self.body[0].x + 1) * self.BLOCK_SIZE > self.WIDTH:
            self.body[0].x = 0
        
        if (self.body[0].y + 1) * self.BLOCK_SIZE > self.HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = self.WIDTH / self.BLOCK_SIZE - 1
        
        if self.body[0].y < 0:
            self.body[0].y = self.HEIGHT / self.BLOCK_SIZE - 1
             

    def draw(self):
        point = self.body[0]
        rect = Rect(self.BLOCK_SIZE * point.x, self.BLOCK_SIZE * point.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        draw.rect(self.GAME_SCREEN, SNAKE_HEAD, rect)

        for point in self.body[1:]:
            rect = Rect(self.BLOCK_SIZE * point.x, self.BLOCK_SIZE * point.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
            draw.rect(self.GAME_SCREEN, SNAKE_BODY, rect)


    def check_collision(self, entity):
        if self.body[0].x == entity.x:
            if self.body[0].y == entity.y:
                return True
        return False