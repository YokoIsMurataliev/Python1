def drawData(SCREEN, cell_height, font, data, scroll):
    name = font.render('Name:', True, (0,0,0))
    number = font.render('Number:', True, (0,0,0))
    height = 5

    SCREEN.blit(name, (10, height - scroll))
    SCREEN.blit(number, (210, height - scroll))

    height += 30 + int(cell_height/4)
    row_count = 0
    for row in data:
        name = font.render(row[0], True, (0,0,0))
        number = font.render(row[1], True, (0,0,0))

        SCREEN.blit(name, (10, height - scroll))
        SCREEN.blit(number, (210, height - scroll))

        height += cell_height
        row_count += 1