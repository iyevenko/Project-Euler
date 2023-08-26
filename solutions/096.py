import copy


def parse_puzles():
    puzle_path = "../data/096-sudoku.txt"
    with open(puzle_path, 'r') as f:
        lines = f.readlines()
    puzles = []
    for i in range(0, len(lines), 10):
        grid = []
        for j in range(1, 10): 
            grid.append([int(x) for x in lines[i+j].strip()])
        puzles.append(grid)
    return puzles

def solve_puzle(grid):
    possibilities = {}

    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                possibilities[(row, col)] = find_possibilities(grid, (row, col))

    grid = dfs(grid, possibilities)

    return grid

def dfs(grid, possibilities):
    sorted_combos = sorted(possibilities.items(), key=lambda x: len(x[1]))
    if not sorted_combos:
        return grid
    
    
    if len(sorted_combos[0][1]) > 1:
        coord, vals = sorted_combos[0]
        for val in vals:
            possibilities_copy = copy.deepcopy(possibilities)
            grid_copy = copy.deepcopy(grid)
            # print(f"Trying {val} at {coord}")
            grid_copy[coord[0]][coord[1]] = val
            possibilities_copy = update_possiblities(possibilities_copy, coord, val)
            grid_copy = dfs(grid_copy, possibilities_copy)
            if grid_complete(grid_copy):
                return grid_copy
        return grid
    
    else:
        # assert all(coord in possibilities for coord, _ in sorted_combos), "WTFFFF"
        for coord, vals in sorted_combos:
            if len(vals) != 1:
                break
            if coord not in possibilities:
                continue
            val = vals.pop()
            # print(f'Placing {val} at {coord}')
            grid[coord[0]][coord[1]] = val
            possibilities = update_possiblities(possibilities, coord, val)
        return dfs(grid, possibilities)


def grid_complete(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    assert grid_correct(grid)
    return True


def grid_correct(grid):
    for i in range(9):
        row = [x for x in grid[i]]
        col = [x[i] for x in grid]
        if (set(row) != set(range(1, 10)) or set(col) != set(range(1, 10))):
            return False
        
    for square_index in range(9): 
        num_set = set()
        row, col = divmod(square_index, 3)
        for x in range(9):
            i, j = divmod(x, 3)    
            num_set.add(grid[i + 3*(row)][j + 3*(col)])
        
        if num_set != set(range(1, 10)):
            return False
    
    return True


def find_possibilities(grid, coord):
    row, col = coord
    num_set = set()

    for i in range(9):
        num_set.add(grid[i][col])

    for i in range(9):
        num_set.add(grid[row][i])

    for i in range(3):
        for j in range(3):
            num_set.add(grid[i + 3*(row//3)][j + 3*(col//3)])

    return set(range(10)) - num_set


def update_possiblities(possibilities, new_coords, new_val):
    row, col = new_coords
    possibilities.pop(new_coords)
    for k, v in possibilities.items():
        if row == k[0] or col == k[1] or (row//3 == k[0]//3 and col//3 == k[1]//3):
           possibilities[k] = v - {new_val}

    possibilities = {k: v for k, v in possibilities.items() if len(v) > 0}
    return possibilities
    

def solve():
    s = 0
    for grid in parse_puzles():
        solution = solve_puzle(grid)
        s += sum(10**i * solution[0][(2-i)] for i in range(3))

    return s

print(solve())