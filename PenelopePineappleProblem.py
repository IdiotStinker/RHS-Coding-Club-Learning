rowAddValues = [19, 9, 11, 10]
colAddValues = [6, 3, 21, 19]

data = [
    [2, 4, 8, 9],
    [8, 7, 6, 3],
    [4, 8, 1, 7],
    [2, 3, 7, 7]
]

dataTruthiness = [
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]

N = len(data)

grid = []

for row in dataTruthiness:
    grid.append([char for char in row])

def backTrack(row, col):
    if row == N: return True
    if col == N: return backTrack(row + 1, 0)
    
    for value in [True, False]:
        grid[row][col] = value
        if valid(row, col) and backTrack(row, col + 1): return True
    
    grid[row][col] = False
    print("very sad :(")
    return False

def valid(row, col):
    totalValue = 0
    for index, rowVal in enumerate(data[row]):
        if grid[row][index]:
            totalValue += rowVal
    
    if totalValue > rowAddValues[row]:
        return False
    
    if col == N - 1:
        if totalValue != rowAddValues[row]:
            return False
    
    totalValue = 0
    for i in range(N):
        if grid[i][col]:
            totalValue += data[i][col]
    
    if totalValue > colAddValues[col]:
        return False
    
    
    
    #if row != 0 and col == 0:
    #    return validAndEqual(row - 1)

    return True

def validAndEqual(row):
    totalValue = 0
    for index, rowVal in enumerate(data[row]):
        if grid[row][index]:
            totalValue += rowVal

    if rowVal != rowAddValues[row]:
        return False
    else:
        return True


def print_sol():
    for row in grid:
        print("".join(str(row)))

backTrack(0, 0)
print_sol()