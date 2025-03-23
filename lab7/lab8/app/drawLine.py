import pygame 

class drawLine():

    def __init__(self, SCREEN, H, W, BACKGROUND_COLOR):
        self.SCREEN = SCREEN
        self.H = H
        self.W = W
        self.BACKGROUND_COLOR = BACKGROUND_COLOR

        self.radius = 15
        self.x = 0
        self.y = 0
        self.mode = 'blue'
        self.points = []

    def draw(self, DrawScreen, *rest):
        ANIMATION_SCREEN = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        ANIMATION_SCREEN.fill((0, 0, 0, 0))
        points = self.points

        self.SCREEN.blit(DrawScreen, (0,0))

        i = 0
        while i < len(points) - 1:
            self.drawLineBetween(ANIMATION_SCREEN, i, points[i], points[i + 1], self.radius, self.mode)
            i += 1
        self.SCREEN.blit(ANIMATION_SCREEN, (0,0))

    def drawLineBetween(self, screen, index, start, end, width, color_mode, *rest):
        c1 = max(0, min(255, 2 * index - 256))
        c2 = max(0, min(255, 2 * index))
        
        if color_mode == 'blue':
            color = (c1, c1, c2)
        elif color_mode == 'red':
            color = (c2, c1, c1)
        elif color_mode == 'green':
            color = (c1, c2, c1)
        elif color_mode == 'black':
            color = (0, 0, 0)
        
        dx = start[0] - end[0]
        dy = start[1] - end[1]
        iterations = max(abs(dx), abs(dy))
        
        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            pygame.draw.circle(screen, color, (x, y), width)

    #_____Обработка событий_____
    def mouseButtonEvent(self, event, *rest):
        if event.button == 1:
            self.radius = min(200, self.radius + 1)
        elif event.button == 3:
            self.radius = max(1, self.radius - 1)
    
    def mouseMotionEvent(self, event, *rest):
        position = event.pos
        self.points = self.points + [position]
        self.points = self.points[-256:]