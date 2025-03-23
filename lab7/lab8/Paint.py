import pygame 
from pygame.locals import *

#____Импорт модулей____
from app.callStageTarget import callStageTarget
from app.colorSelect import colorSelect
from app.drawLine import drawLine
from app.drawRectangle import drawRectangle
from app.drawEllipse import drawEllipse
from app.eraser import eraser
from app.drawRightTriangle import drawRightTriangle
from app.drawEqulateralTriangle import drawEqulateralTriangle
from app.drawRhombus import drawRhombus

def main():
    pygame.init()

    #_____Инициализация цветов_____
    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (70, 70, 70)

    #_____Общие переменные_____
    W = 640
    H = 480
    FPS = 60
    SCREEN = pygame.display.set_mode((W, H))
    CLOCK = pygame.time.Clock()
    DrawScreen = pygame.Surface((W, H), pygame.SRCALPHA)
    BACKGROUND_COLOR = BLACK
    DrawScreen.fill(BACKGROUND_COLOR)
    __color_mode__ = WHITE
    __prog_stage__ = False

    #_____Инициализация всех классов_____
    stage0 = drawLine(SCREEN, H, W, BACKGROUND_COLOR)
    stage1 = drawRectangle(SCREEN, H, W, GRAY, GREEN)
    stage2 = drawEllipse(SCREEN, H, W, GRAY, GREEN)
    stage3 = eraser(SCREEN, H, W, BACKGROUND_COLOR)
    stage4 = drawRightTriangle(SCREEN, H, W, GRAY, GREEN)
    stage5 = drawEqulateralTriangle(SCREEN, H, W, GRAY, GREEN)
    stage6 = drawRhombus(SCREEN, H, W, GRAY, GREEN)

    all_stages = []
    all_stages.append(stage0) 
    all_stages.append(stage1)
    all_stages.append(stage2)
    all_stages.append(stage3)
    all_stages.append(stage4)
    all_stages.append(stage5)
    all_stages.append(stage6)

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[K_LALT] or pressed[K_RALT]
        ctrl_held = pressed[K_LCTRL] or pressed[K_RCTRL]
        shift_held = pressed[K_LSHIFT] or pressed[K_RSHIFT]
        
        #_____Обработка ивентов_____
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == KEYDOWN:
                if event.key == K_w and ctrl_held:
                    return
                if event.key == K_F4 and alt_held:
                    return
                if event.key == K_ESCAPE:
                    return

                #_____Смена действующего класса_____
                if event.key == K_1:             #рисование линии
                    __prog_stage__ = 0
                if event.key == K_2:             #рисование квадрата и прямоугольника
                    __prog_stage__ = 1
                if event.key == K_3:             #рисование круга и эллипса
                    __prog_stage__ = 2
                if event.key == K_4:             #стерка
                    __prog_stage__ = 3
                if event.key == K_5:             #рисование прямоугольного треугольника
                    __prog_stage__ = 4
                if event.key == K_6:             #рисование правильного треугольника
                    __prog_stage__ = 5
                if event.key == K_7:             #рисование ромба
                    __prog_stage__ = 6
                if event.key == K_0:             #выключение всех классов
                    __prog_stage__ = False
                    SCREEN.blit(DrawScreen, (0,0))
                

                #_____Смена цвета_____
                color = colorSelect(event)  
                if (color):
                    __color_mode__ = color
            
            #_____Перенаправление ивентов к действующему классу_____ 
            if event.type == MOUSEBUTTONDOWN:
                callStageTarget(all_stages, __prog_stage__, 'mouseButtonEvent', event)
            if event.type == MOUSEMOTION:
                callStageTarget(all_stages, __prog_stage__, 'mouseMotionEvent', event, DrawScreen)
        
        
        #_____Прорисовка функций_____
        if type(__prog_stage__) != type(False):
            callStageTarget(all_stages, __prog_stage__, 'draw', DrawScreen, __color_mode__, shift_held)


        pygame.display.update()
        CLOCK.tick(FPS)
    

main()