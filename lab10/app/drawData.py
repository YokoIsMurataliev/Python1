import pygame
from app.executeData import executeData

def drawData(SCREEN, filter):
    try:
        font = pygame.font.SysFont("Verdana", 15)

        sql = "select user_name, number from user_numbers"
        if filter:
            sql += filter
        else:
            sql += ';'
        
        data = executeData(sql, None, True)

        height = 5
        if (data is None):
            return
        name = font.render('Name:', True, (0,0,0))
        number = font.render('Number:', True, (0,0,0))

        SCREEN.blit(name, (10, height))
        SCREEN.blit(number, (210, height))

        height += 30
        for row in data:
            name = font.render(row[0], True, (0,0,0))
            number = font.render(row[1], True, (0,0,0))

            SCREEN.blit(name, (10, height))
            SCREEN.blit(number, (210, height))

            height += 20
    except Exception as e:
        print(str(e))

