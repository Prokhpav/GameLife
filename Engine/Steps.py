from .Globals import *


def get_mouse_pos(pos):
    return (int(pos[0] // 10), int(pos[1] // 10))


def get_near_sum(pos, desk):  # Количество соседей включая саму клетку
    return np.sum(desk[pos[0]-1:pos[0]+2, pos[1]-1:pos[1]+2])


def is_alive(pos, desk):  # Выживет ли клетка
    s = get_near_sum(pos, desk)
    if 2 < s < 5:
        return True
    return False


def all_near(pos, desk):  # Все пустые соседи
    for pos in np.array(((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))) + pos:
        if not desk[pos[0], pos[1]]:
            yield (pos[0], pos[1])


def is_spawn(pos, desk):  # Появится ли клетка
    s = get_near_sum(pos, desk)
    if s == 3:
        return True
    return False


def set_pos(pos, alive):
    if not (0 < pos[0] < Globals.max_size[0] and 0 < pos[1] < Globals.max_size[1]):
        return
    Globals.desk[pos[0], pos[1]] = alive
    pygame.draw.rect(Globals.screen, (Colors.WHITE if alive else Colors.BLACK), (pos[0] * 10, pos[1] * 10, 9, 9))
    if alive:
        Globals.alive.add(pos)
    elif pos in Globals.alive:
        Globals.alive.remove(pos)


def next_step():
    desk = Globals.desk.copy()

    nears = set()
    for pos in Globals.alive.copy():
        if not is_alive(pos, desk):
            set_pos(pos, 0)
        nears |= set(all_near(pos, desk))

    for pos in nears:
        if is_spawn(pos, desk):
            set_pos(pos, 1)


def next_step1():
    desk = Globals.desk.copy()

    nears = set()
    for pos in Globals.alive.copy():
        if not (2 < get_near_sum(pos, desk) < 5):
            set_pos(pos, 0)
        for near in np.array(((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))) + pos:
            if not desk[near[0], near[1]]:
                nears.add((near[0], near[1]))
    for pos in nears:
        if get_near_sum(pos, desk) == 3:
            set_pos(pos, 1)
