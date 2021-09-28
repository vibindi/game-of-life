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

def render(board_state):
    print("-" * (len(board_state)+2))
    for x in range(len(board_state)):
        row = ""
        for y in range(len(board_state[0])):
            if board_state[x][y] == DEAD:
                row += " "
            else:
                row += "$"
        print(f"|{row}|")


render(random_state(5, 5))