from Engine import *
from UI import *


f = 0
pause = True
while not Input.quit:
    Input.update()
    if 32 in Input.k_pressed:
        pause = not pause
    if 273 in Input.k_pressed:
        Globals.speed /= 1.2
    if 274 in Input.k_pressed:
        Globals.speed *= 1.2
    if 1 in Input.m_hold:
        pos = get_mouse_pos(Input.m_pos)
        set_pos(pos, 1)
    if 99 in Input.k_pressed:
        for pos in Globals.alive.copy():
            set_pos(pos, 0)
    if 3 in Input.m_hold:
        pos = get_mouse_pos(Input.m_pos)
        set_pos(pos, 0)
    if not pause:
        f += 1
        while f > 0:
            next_step1()
            f -= Globals.speed

    pygame.display.update()
    Globals.timer.tick(30)
