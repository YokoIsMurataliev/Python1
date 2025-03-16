import pygame
import os
import datetime

pygame.init()

size = height, width = (780, 600)
screen = pygame.display.set_mode(size)
_image_library = {}

def get_image(path):
  global _image_library
  image = _image_library.get(path)
  if image is None:
    _path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(_path)
    _image_library[path] = image
  return image

def blitRotateCenter(surf, image, topleft, angle):         
    rotated_image = pygame.transform.rotate(image, angle)
    new_im = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_im)

def gradusFromTime(time):
    return 360 - time * 6
  
image = pygame.transform.scale(get_image('img\\backgr.png'), size)
handsec = pygame.transform.scale(get_image('img\\Секундная.png'), (300, 300))
handmin = pygame.transform.scale(get_image('img\\Минутная.png'), (300, 300))

done = False
while not done:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          done = True
          
  screen.fill((255, 255, 255))  
  screen.blit(image, (0, 0))  
  t = datetime.datetime.now()

  ang_sec = gradusFromTime(t.second)
  ang_min = gradusFromTime(t.minute)

  blitRotateCenter(screen, handsec, (height/2 - 150, width/2 - 150), ang_sec)
  blitRotateCenter(screen, handmin, (height/2 - 150, width/2 - 150), ang_min)

  pygame.display.flip()
