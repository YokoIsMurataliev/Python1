import pygame

class drawEqulateralTriangle():

    def __init__(self, SCREEN, H, W, GRAY, GREEN, *rest):
        self.GRAY = GRAY
        self.GREEN = GREEN
        self.SCREEN = SCREEN
        self.W = W
        self.H = H

        self._width_ = 3
        self._x_ = -30
        self._y_ = -30
        self._inner_x_ = 0
        self._inner_y_ = 0
        self.stage = 0


    def draw(self, DrawScreen, color_mode, *rest):
        ANIMATION_SCREEN = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        ANIMATION_SCREEN.fill((0, 0, 0, 0))

        if self.stage == 0:
            self.SCREEN.blit(DrawScreen, (0,0))
            self.drawIcon(ANIMATION_SCREEN, self._x_, self._y_, self.GREEN)
            self.SCREEN.blit(ANIMATION_SCREEN, (0,0))
        
        if self.stage == 1:
            self.SCREEN.blit(DrawScreen, (0,0))
            self.drawFigure(ANIMATION_SCREEN, self._x_, self._y_, self._inner_x_, self._inner_y_, self._width_, self.GRAY)
            self.SCREEN.blit(ANIMATION_SCREEN, (0,0))
        
        if self.stage == 2:
            self.drawFigure(DrawScreen, self._x_, self._y_, self._inner_x_, self._inner_y_, self._width_, color_mode)
            self.stage = 0
    

    def drawIcon(self, surface, x, y, color, *rest):
        pygame.draw.polygon(surface, color, ((x+2, y-5), (x-5, y+7), (x+9, y+7)), 2)  
        pygame.draw.line(surface, color, (x-10, y+10), (x-10, y+19), 2)
        pygame.draw.line(surface, color, (x-5, y+14), (x-14, y+14), 2)
        

    def drawFigure(self, SCREEN, _x_, _y_, _inner_x_, _inner_y_, _width_, color):
        points = self.returnPoints(_x_, _y_, _inner_x_, _inner_y_,)
        pygame.draw.polygon(SCREEN, color, points, _width_)
    

    def returnPoints(self, x1, y1, x2, y2, *rest):
        side = min(abs(x2-x1), abs(y2-y1))
        height = round(side * 0.866)
        x = 1
        y = 1

        if (x2 > x1):
            x = -1
        if (y2 > y1):
            y = -1

        pnt1 = (x2 + round(side/2)*x, y2)
        pnt2 = (x2, y2 + height*y)
        pnt3 = (x2 + side*x, y2 + height*y)
        return (pnt1, pnt2, pnt3)
    

    #_____Обработка событий_____
    def mouseButtonEvent(self, event, *rest):
        if self.stage == 0:
            self._inner_x_ = self._x_
            self._inner_y_ = self._y_
            self.stage = 1

        elif self.stage == 1:
            self.stage = 2 
    

    def mouseMotionEvent(self, event, *rest):
        self._x_ = event.pos[0]
        self._y_ = event.pos[1]