import pygame
import os

def get_music(path):
  return path.replace('/', os.sep).replace('\\', os.sep)

music_list = [
  'Imagine Dragons - Bleeding Out.mp3',
  'Imagine Dragons - Boomerang.mp3',
  'Imagine Dragons - Bullet In A Gun.mp3',
  'Imagine Dragons - Cool Out.mp3',
  'Imagine Dragons - Dancing In The Dark.mp3',
  'Imagine Dragons - Demons.mp3'
]

pygame.init()

screen = pygame.display.set_mode((400, 400))
done = False
_is_play_ = False
currentMusic = 0
pygame.mixer.music.load(get_music('audio/' + music_list[currentMusic]))

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      if _is_play_:
        pygame.mixer.music.stop()
        _is_play_ = False
      else:
        pygame.mixer.music.play()
        _is_play_ = True

    if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_LEFT):
      currentMusic -= 1
      if currentMusic < 0:
        currentMusic = len(music_list) - 1
      pygame.mixer.music.load(get_music('audio/' + music_list[currentMusic]))
      pygame.mixer.music.play()

    if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT):
      currentMusic += 1
      if currentMusic > len(music_list) - 1:
        currentMusic = 0
      pygame.mixer.music.load(get_music('audio/' + music_list[currentMusic]))
      pygame.mixer.music.play()
    
  pygame.display.flip()

pygame.quit()
