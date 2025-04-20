import pygame
from app.drawApps.drawData import drawData
from app.drawApps.drawTable import drawTable
from app.drawApps.drawScroll import drawScroll
from app.generalApps.executeData import executeData

def screenDraw(SCREEN, WIDTH, HEIGHT, filter, scroll):
    HEADER_HEIGHT = 60
    BODY_HEIGHT = HEIGHT - HEADER_HEIGHT
    header = pygame.Surface((WIDTH, HEADER_HEIGHT))
    body = pygame.Surface((WIDTH, BODY_HEIGHT))
    font = pygame.font.SysFont('Georgia', 40)
    small_font = pygame.font.SysFont("PT Astra Sans", 17)
    cell_height = 25

    header_title = font.render('Phone Book', True, (0,0,0))

    SCREEN.fill((255, 255, 255))
    header.fill((200, 200, 200))
    body.fill((255, 255, 255))

    sql = "select user_name, number from user_numbers"
    if filter:
        sql += filter + ' order by user_name ASC;'
    else:
        sql += ' order by user_name ASC;'
    
    try:
        data = executeData(sql, None, True)
        if (data is not None):
            row_count = len(data)
            total_height = row_count * cell_height + 40
            if HEIGHT >= total_height:
                drawData(body, cell_height, small_font, data, 0)
                drawTable(body, cell_height, BODY_HEIGHT, WIDTH, row_count, 0)
            else:
                drawData(body, cell_height, small_font, data, scroll)
                drawTable(body, cell_height, total_height - scroll, WIDTH, row_count, scroll)
                drawScroll(body, total_height, HEIGHT, WIDTH, scroll)
            return total_height
    except Exception as e:
        print(str(e))
    finally:
        header.blit(header_title, (100, 7))
        SCREEN.blit(header, (0,0))
        SCREEN.blit(body, (0, HEADER_HEIGHT))