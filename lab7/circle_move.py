import pygame

pygame.init()

size = height, width = (390, 390)
x, y = height/2 , width/2
vel = 20     
circleRadius = 15
plane = pygame.display.set_mode(size)
pygame.display.set_caption("Moving ball")   

done = False
while not done:
    plane.fill((255, 255, 134))
    pygame.draw.circle(plane, "red", (x, y), circleRadius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if (x - vel - circleRadius < 0): break
            x -= vel

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if (x + vel + circleRadius > width): break
            x += vel

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if (y - vel - circleRadius < 0): break
            y -= vel

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if (y + vel + circleRadius > height): break
            y += vel

    pygame.display.update()
