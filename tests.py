# unit testing

from game_of_life import next_board_state

if __name__ == "__main__":
    # Test 1: Dead cells with no live neighbors should stay dead
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_board_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED TEST 1")
    else:
        print("FAILED TEST 1")
        print(f"Expected: {expected_next_state1}\nActual: {actual_next_state1}")
    
    # Test 2: Dead cells with exactly 3 neighbors
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print("PASSED TEST 2")
    else:
        print("FAILED TEST 2")
        print(f"Expected: {expected_next_state2}\nActual: {actual_next_state2}")