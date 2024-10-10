import sys
sys.setrecursionlimit(10000000)

data = [
    [[0, 0], [0, 1], [0, -1], [1, 0]],
    [[1, 0], [-1, -1], [-1, 0], [-1, 1]],
    [[1, 0], [1, 1], [-1, -1], [0, -1]],
    [[-1, 1], [0, -1], [-1, 1], [-1, 0]]
]

grid = [
    [16, -1, 1, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, -1]
]

N = len(grid)

def backTrack(row, col, value, start = False):
    
    if start:
        for r, fullRow in enumerate(grid):
            for c, value in enumerate(fullRow):
                if value == 1:
                    row = r
                    col = c

    if row == N: 
        print("huh")
        return True
    if col == N: 
        print("heh")
        return backTrack(row + 1, col, value)

    if not (grid[row][col] == -1 or start): 
        print("hm")
        return False

    spots = findSpotsInDirection(row, col)

    for i in range(spots):

        dr = data[row][col][0]
        dc = data[row][col][1]

        grid[row][col] = value
        if backTrack(row + dr * (i + 1), col + dc * (i + 1), value + 1): return True

    grid[row][col] = -1
    return False

def findSpotsInDirection(row, col):
    dr = data[row][col][0]
    dc = data[row][col][1]
    spots = 0
    while 0 <= row + dr <= N and 0 <= col + dc <= N:
        row += dr
        col += dc
        spots += 1
    return spots

def print_sol():
    for row in grid:
        print("".join(str(row)))




print("why")


#if not backTrack(0, 2, 1, True):
#    print ("very sad")
#print_sol()

