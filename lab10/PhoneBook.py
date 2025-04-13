import pygame, sys
from pygame.locals import *

from app.uploadDataFromConsole import uploadDataFromConsole
from app.uploadDataFromCSV import uploadDataFromCSV
from app.changeFilter import changeFilter
from app.updateData import updateData
from app.deleteData import deleteData
from app.screenDraw import screenDraw
from app.appQuit import appQuit

def main():
    HEIGHT = 700
    WIDTH = 500
    FPS = 60

    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE  = (0, 0, 255)
    BLACK = (0, 0, 0)
    PURPLE = (255, 0, 255)
    WHITE = (255, 255, 255)

    pygame.init()

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    filter = False
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                appQuit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    uploadDataFromCSV()
                if event.key == K_2:
                    uploadDataFromConsole()
                if event.key == K_3:
                    updateData()
                if event.key == K_4:
                    filter = changeFilter()
                if event.key == K_5:
                    deleteData()

        screenDraw(SCREEN, WIDTH, HEIGHT, filter)

        pygame.display.update()
        CLOCK.tick(FPS)

main()