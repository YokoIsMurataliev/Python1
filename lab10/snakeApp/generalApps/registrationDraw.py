import pygame
from snakeApp.generalApps.colors import *

def registrationDraw(SCREEN, name, HEIGHT, WIDTH):
    font = pygame.font.SysFont("Verdana", 30)
    small_font = pygame.font.SysFont("Verdana", 20)
    h1_font = pygame.font.SysFont("Verdana", 60)
    small_screen = pygame.Surface((500, 200), pygame.SRCALPHA)

    SCREEN.fill(BLACK)
    small_screen.fill((0,0,0, 200))

    h1 = h1_font.render('Snake Game', True, WHITE)
    h1_shadow = h1_font.render('Snake Game', True, BLACK)
    h2 = font.render('Write your name:', True, WHITE)
    
    if name == '':
        name = '_______________________'
    p = small_font.render(name, True, WHITE)
    
    background = pygame.transform.scale( pygame.image.load('snakeApp\img\Background.png'), (WIDTH+20, HEIGHT + 60) )

    SCREEN.blit(background, (-10,0))
    SCREEN.blit(h1_shadow, (213, 63))
    SCREEN.blit(h1, (210, 60))
    small_screen.blit(h2, (120, 40))
    small_screen.blit(p, (50, 120))
    SCREEN.blit(small_screen, ((WIDTH - 500)/2, (HEIGHT - 140)/2))

    pygame.display.update()