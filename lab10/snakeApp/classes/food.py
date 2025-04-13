from pygame import Rect, draw
import datetime
from random import randint
from snakeApp.classes.point import Point
from snakeApp.generalApps.colors import FOOD_COLORS

class Food:
    def __init__(self, _inner_data_, walls):
        self.location = []
        self.current = randint(0, 2)
        self.values = [1, 2, 5]
        self.timer = datetime.datetime.now()

        self.SCREEN = _inner_data_['screen']
        self.GAME_SCREEN = _inner_data_['game_screen']
        self.HEIGHT = _inner_data_['height']
        self.WIDTH = _inner_data_['width']
        self.BLOCK_SIZE = _inner_data_['block_size']
        self.walls = walls

        self.returnLocation()


    def draw(self):
        point = self.location
        rect = Rect(self.BLOCK_SIZE * point.x, self.BLOCK_SIZE * point.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        draw.rect(self.GAME_SCREEN, FOOD_COLORS[self.current], rect)


    def update(self):
        self.current = randint(0, 2)
        self.returnLocation()
        self.timer = datetime.datetime.now()


    def timer_update(self):
        delta = datetime.datetime.now() - self.timer
        if delta.total_seconds() > 10:
            self.update()
    
    def returnLocation(self):
        self.location = Point(randint(0, self.WIDTH/self.BLOCK_SIZE - 1), randint(0, self.HEIGHT/self.BLOCK_SIZE - 1))

        for wall in self.walls:
            if self.location.x == wall.x:
                if self.location.y == wall.y:
                    self.returnLocation()
        