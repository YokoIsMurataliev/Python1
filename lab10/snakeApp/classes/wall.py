from pygame import Rect, draw
from snakeApp.classes.point import Point
from snakeApp.generalApps.colors import WALL_COLOR
from snakeApp.generalApps.mapReader import mapReader

class Wall:
    def __init__(self, _inner_data_):
        self.body = self.createMap(_inner_data_['map'])

        self.GAME_SCREEN = _inner_data_['game_screen']
        self.HEIGHT = _inner_data_['height']
        self.WIDTH = _inner_data_['width']
        self.BLOCK_SIZE = _inner_data_['block_size']

    def draw(self):
        for point in self.body:
            rect = Rect(self.BLOCK_SIZE * point.x, self.BLOCK_SIZE * point.y, self.BLOCK_SIZE, self.BLOCK_SIZE)
            draw.rect(self.GAME_SCREEN, WALL_COLOR , rect)


    def createMap(self, path):
        _map_ = mapReader(path)
        body = []
        y = 0

        for row in _map_:
            x = 0
            for cell in row:
                if cell == '1':
                    body.append(Point(x, y))
                x += 1
            y += 1

        return body