from pygame.locals import *
from random import randint

def colorSelect(event):
    if event.key == K_r:
        return (255, 0, 0)
    if event.key == K_g:
        return (0, 255, 0)
    if event.key == K_b:
        return (0, 0, 255)
    if event.key == K_w:
        return (255, 255, 255)
    if event.key == K_p:
        return (255, 0, 255)
    if event.key == K_q:
        return (randint(0, 255), randint(0, 255), randint(0,255))