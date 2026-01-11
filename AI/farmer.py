def is_valid(state):
    """Checks if a state is valid."""
    farmer, goat, wolf, cabbage = state
    if (goat == cabbage and farmer != goat) or (goat == wolf and farmer != wolf):
        return False
    return True

def generate_moves(state):
    """Generates possible moves from a given state."""
    farmer, goat, wolf, cabbage = state
    moves = []
    # Farmer moves alone
    moves.append((1 - farmer, goat, wolf, cabbage))
    # Farmer moves with goat
    if goat == farmer:
      moves.append((1 - farmer, 1 - goat, wolf, cabbage))
    # Farmer moves with wolf
    if wolf == farmer:
      moves.append((1 - farmer, goat, 1 - wolf, cabbage))
    # Farmer moves with cabbage
    if cabbage == farmer:
       moves.append((1 - farmer, goat, wolf, 1 - cabbage))
    return moves

def solve_puzzle():
    """Solves the puzzle using a breadth-first search."""
    start_state = (0, 0, 0, 0)
    goal_state = (1, 1, 1, 1)
    queue = [(start_state, [])]  # Queue of (state, path)
    visited = set()

    while queue:
        current_state, path = queue.pop(0)
        if current_state == goal_state:
            return path + [current_state]
        
        if current_state in visited:
            continue
        visited.add(current_state)

        for next_state in generate_moves(current_state):
          if is_valid(next_state):
            queue.append((next_state, path + [current_state]))
    return None

solution = solve_puzzle()
if solution:
    print("Solution found:")
   # for state in solution:
   #     print(state)
else:
    print("No solution found.")
 
# Covert to Human readable format 
# solution is list of tuple(0,0,0,0) replace solution with own 
prev = (0,0,0,0)
moved =[]   
for state in solution:
    character = ["Farmer" , "Goat" , "Wolf" , "Cabbage"]
    char_list = []
    
    for i in range(0,4):
        if state[i] != prev[i]:
            char_list.append(character[i])
            if prev[i] == 0:
                marker = 0
            else:
                marker = 1
    
    if(len(char_list)==2):
        moved.append((char_list[0],char_list[1],marker))
    elif(len(char_list)==1):
        moved.append((char_list[0],"alone",marker))
        
    prev = state
   
direction = ["from east to west","from west to east"]
for item in moved:
    print(f'{item[0]} {item[1]} moved {direction[item[2]]}')
                