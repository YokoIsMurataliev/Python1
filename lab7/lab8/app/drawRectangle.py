import pygame 

class drawRectangle():

    def __init__(self, SCREEN, H, W, GRAY, GREEN, *rest):
        self.GRAY = GRAY
        self.GREEN = GREEN
        self.SCREEN = SCREEN
        self.W = W
        self.H = H

        self._rectangle_width_ = 3
        self._x_ = -30
        self._y_ = -30
        self._inner_x_ = 0
        self._inner_y_ = 0
        self.stage = 0
        self.shift_held = False


    def draw(self, DrawScreen, color_mode, shift_held, *rest):
        ANIMATION_SCREEN = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        ANIMATION_SCREEN.fill((0, 0, 0, 0))
        self.shift_held = shift_held

        if self.stage == 0:
            self.SCREEN.blit(DrawScreen, (0,0))
            self.drawRectangleIcon(ANIMATION_SCREEN, self._x_, self._y_, self.GREEN)
            self.SCREEN.blit(ANIMATION_SCREEN, (0,0))
        
        if self.stage == 1:
            self.SCREEN.blit(DrawScreen, (0,0))
            self.drawRectangle(ANIMATION_SCREEN, self._x_, self._y_, self._inner_x_, self._inner_y_, self._rectangle_width_, self.GRAY)
            self.SCREEN.blit(ANIMATION_SCREEN, (0,0))
        
        if self.stage == 2:
            rect = self.returnRectangle(self._x_, self._y_, self._inner_x_, self._inner_y_)
            pygame.draw.rect(DrawScreen, color_mode, rect, self._rectangle_width_)
            self.stage = 0
    

    def drawRectangleIcon(self, surface, x, y, color, *rest):
        pygame.draw.rect(surface, color, (x-6, y-5, 15, 15), 2)
        pygame.draw.line(surface, color, (x-11, y+10), (x-11, y+19), 2)
        pygame.draw.line(surface, color, (x-6, y+14), (x-15, y+14), 2)
        

    def drawRectangle(self, SCREEN, _x_, _y_, _inner_x_, _inner_y_, _rectangle_width_, GRAY):
        rect = self.returnRectangle(_x_, _y_, _inner_x_, _inner_y_)
        pygame.draw.rect(SCREEN, GRAY, rect, _rectangle_width_)
    

    def returnRectangle(self, x1, y1, x2, y2, *rest):
        x = x1
        y = y1

        width = abs(x2-x1)
        height = abs(y2-y1)
        if self.shift_held:
            width = min(width, height)
            height = width

        if x1 > x2:
            x = x2
        if y1 > y2:
            y = y2
        return (x, y, width, height)
    

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
