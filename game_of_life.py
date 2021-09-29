import random
import time

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
    for x in range(len(board_state)):
        row = ""
        for y in range(len(board_state[0])):
            if board_state[x][y] == DEAD:
                row += " "
            else:
                row += "$"
        print(f"|{row}|")

# param: initial board state
# calculates and returns next board state
def next_board_state(initial):
    width = len(initial[0])
    height = len(initial)
    new_state = dead_state(width, height)

    for x in range(height):
        for y in range(width):
            new_state[x][y] = next_cell_value(x, y, initial, width, height)
    return new_state

def next_cell_value(x, y, initial, width, height):
    live_neighbors = 0

    for i in range(x-1, x+2):
        if i < 0 or i >= height: continue
        for j in range(y-1, y+2):
            if j < 0 or j >= width: continue
            if i == x and j == y: continue # don't do operation of own cell
            if initial[i][j] == ALIVE: live_neighbors += 1

    if initial[x][y] == DEAD:
        if live_neighbors == 3: return ALIVE
        else: return DEAD
    else:
        if live_neighbors <= 1: return DEAD
        elif live_neighbors <= 3: return ALIVE
        else: return DEAD

def run_forever(initial):
    next_state = initial
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.5)

def load_board_state(path):
    state = []
    with open(path, "r") as file:
        for l in file.readlines():
            temp = [int(s[0]) for s in l.split(",")]
            state.append(temp)
    return state

if __name__ == "__main__":
    #state = random_state(50, 100)
    #render(state)
    run_forever(load_board_state("example_soups/gosper-glide-gun.txt"))