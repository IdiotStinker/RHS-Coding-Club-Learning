'''
dataArrow = [
    [[0, 1], [0, 1], [0, 1], [1, 1], [1, 1], [1, -1], [0, -1]],
    [[1, 0], [0, 1], [1, 0], [1, -1], [0, -1], [1, 0], [1, 0]],
    [[0, 1], [-1, -1], [-1, 0], [1, -1], [-1, 0], [0, -1], [0, -1]],
    [[0, 1], [0, 1], [1, 0], [1, -1], [0, -1], [1, 0], [1, -1]],
    [[-1, 1], [0, 1], [-1, 0], [1, 0], [1, 0], [1, 1], [0, -1]],
    [[-1, 0], [0, -1], [0, 1], [0, 1], [-1, 1], [-1, -1], [-1, -1]],
    [[-1, 1], [0, 1], [0, 1], [0, 1], [0, -1], [-1, -1], [0, 0]],
]

data = [
    [1, -1, 2, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, 6, 33, -1, -1, -1, -1],
    [-1, -1, 32, -1, -1, -1, 28],
    [11, -1, -1, -1, -1, -1, -1],
    [17, -1, 47, -1, 45, -1, 49]
]
'''

dataArrow = [
    [[0, 0], [0, 1], [0, -1], [1, 0]],
    [[1, 0], [-1, -1], [0, -1], [1, -1]],
    [[0, 1], [1, 1], [-1, -1], [0, -1]],
    [[-1, 1], [0, -1], [-1, 1], [-1, 0]]
]

data = [
    [16, -1, 1, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, -1]
]

grid = []

for row in data:
    grid.append([char for char in row])

N = len(grid)

def backTrack(row, col, value, start = False):
    
    if start:
        for r, fullRow in enumerate(grid):
            for c, val in enumerate(fullRow):
                if val == 1:
                    row = r
                    col = c

    if row == N: 
        print("huh")
        return True
    if col == N:
        print("heh")
        return backTrack(row + 1, col, value)

    if not (grid[row][col] == -1 or start):
        return False

    spots = findSpotsInDirection(row, col)

    for spotIndex in range(spots):
        dr = dataArrow[row][col][0]
        dc = dataArrow[row][col][1]
        grid[row][col] = value
        if backTrack(row + dr * (spotIndex + 1), col + dc * (spotIndex + 1), value + 1): return True

    if value == N*N - 1:
        return True
    grid[row][col] = -1
    return False

def findSpotsInDirection(row, col):
    dr = dataArrow[row][col][0]
    dc = dataArrow[row][col][1]
    spots = 0
    if dr == 0 and dc == 0:
        print("error")
        return 0
    
    while 0 <= row + dr < N and 0 <= col + dc < N:
        row += dr
        col += dc
        spots += 1

    return spots

def print_sol():
    for row in grid:
        print("".join(str(row)))


for r in range(N):
    for c in range(N):
        if r == 0 and c == 0:
            pass
        else:
            findSpotsInDirection(r, c)

if not backTrack(0, 0, 1, True):
    print ("very sad")
print_sol()
