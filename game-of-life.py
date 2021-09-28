import random

DEAD = 0
ALIVE = 1

def dead_state(width, height):
    return [[DEAD for x in range(width)] for y in range(height)]

def random_state(width, height):
    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            rand = random.random()
            if rand >= 0.5:
                state[i][j] = DEAD
            else:
                state[i][j] = ALIVE
    return state

print(random_state(2, 2))