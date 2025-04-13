from pygame.locals import *

def keyboardWrite(event, name):
    if event.key == K_a:
        name += 'A'
    if event.key == K_b:
        name += 'B'
    if event.key == K_c:
        name += 'C'
    if event.key == K_d:
        name += 'D'
    if event.key == K_e:
        name += 'E'
    if event.key == K_f:
        name += 'F'
    if event.key == K_g:
        name += 'G'
    if event.key == K_h:
        name += 'H'
    if event.key == K_i:
        name += 'I'
    if event.key == K_j:
        name += 'J'
    if event.key == K_k:
        name += 'K'
    if event.key == K_l:
        name += 'L'
    if event.key == K_m:
        name += 'M'
    if event.key == K_n:
        name += 'N'
    if event.key == K_o:
        name += 'O'
    if event.key == K_p:
        name += 'P'
    if event.key == K_q:
        name += 'Q'
    if event.key == K_r:
        name += 'R'
    if event.key == K_s:
        name += 'S'
    if event.key == K_t:
        name += 'T'
    if event.key == K_u:
        name += 'U'
    if event.key == K_v:
        name += 'V'
    if event.key == K_w:
        name += 'W'
    if event.key == K_x:
        name += 'X'
    if event.key == K_y:
        name += 'Y'
    if event.key == K_z:
        name += 'Z'
    if event.key == K_BACKSPACE:
        if len(name) == 0:
            return ''
        name = name[:-1]
        
    return name[:30]