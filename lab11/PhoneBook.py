import pygame, sys
from pygame.locals import *

from app.generalApps.uploadDataFromConsole import uploadDataFromConsole
from app.generalApps.uploadDataFromCSV import uploadDataFromCSV
from app.generalApps.changeFilter import changeFilter
from app.generalApps.updateData import updateData
from app.generalApps.deleteData import deleteData
from app.drawApps.screenDraw import screenDraw

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
    scroll = 0
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    if scroll <= 0:
                        scroll = 0
                        continue
                    scroll -= 50
                if event.button == 5:
                    if total_height - scroll + 60 <= HEIGHT:
                        scroll = total_height - HEIGHT + 60
                        continue 
                    scroll += 50

        total_height = screenDraw(SCREEN, WIDTH, HEIGHT, filter, scroll)

        pygame.display.update()
        CLOCK.tick(FPS)

main()