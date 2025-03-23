import pygame

class eraser():

    def __init__(self, SCREEN, H, W, BACKGROUND_COLOR):
        self.SCREEN = SCREEN
        self.H = H
        self.W = W
        self.BACKGROUND_COLOR = BACKGROUND_COLOR

        self.radius = 15
        self.x = -1
        self.y = -1

    #_____Обработка событий_____
    def mouseButtonEvent(self, event, *rest):
        if event.button == 1:
            self.radius = min(200, self.radius + 1)
        elif event.button == 3:
            self.radius = max(1, self.radius - 1)
    
    def mouseMotionEvent(self, event, DrawScreen, *rest):
        self.x = event.pos[0]
        self.y = event.pos[1]

        self.SCREEN.blit(DrawScreen, (0,0))
        pygame.draw.circle(DrawScreen, self.BACKGROUND_COLOR, (self.x, self.y), self.radius)

        ANIMATION_SCREEN = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        ANIMATION_SCREEN.fill((0, 0, 0, 0))
        pygame.draw.circle(ANIMATION_SCREEN, (150, 150, 150), (self.x, self.y), self.radius)
        self.SCREEN.blit(ANIMATION_SCREEN, (0,0))
