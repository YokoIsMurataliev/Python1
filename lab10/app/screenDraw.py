import pygame
from app.drawData import drawData

def screenDraw(SCREEN, WIDTH, HEIGHT, filter):
    HEADER_HEIGHT = 60
    BODY_HEIGHT = HEIGHT - HEADER_HEIGHT
    font = pygame.font.SysFont('Verdana', 40)

    SCREEN.fill((255, 255, 255))
    header = pygame.Surface((WIDTH, HEADER_HEIGHT))
    body = pygame.Surface((WIDTH, BODY_HEIGHT))

    header.fill((200, 200, 200))
    header_title = font.render('Phone Book', True, (0,0,0))
    header.blit(header_title, (120, 3))

    body.fill((255, 255, 255))
    pygame.draw.line(body, (200, 200, 200), (200, 0), (200, BODY_HEIGHT))
    drawData(body, filter)

    SCREEN.blit(header, (0,0))
    SCREEN.blit(body, (0, HEADER_HEIGHT))