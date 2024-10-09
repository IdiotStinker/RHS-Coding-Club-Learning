data = [
    'XX....#....',
    '.O#.#......',
    '..#XO#....#',
    'O..##.O....',
    '##.....O...',
    '...........',
    '.......O...',
    '.....##....',
    '..........#',
    '......#....',
    '...........'
]

N = len(data)
grid = []

for row in data:
    grid.append([char for char in row])

def backTrack(row, col):
    if row == N: return True
    if col == N: return backTrack(row + 1, 0)
    if grid[row][col] != ".": return backTrack(row, col + 1)

    for token in "XO":
        grid[row][col] = token
        if valid(row, col) and backTrack(row, col + 1): return True

    grid[row][col] = "."
    return False

def valid(row, col):
    for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        streak = 1
        r, c = row + dr, col + dc
        while 0 <= r < N and 0 <= c < N and grid[r][c] == grid[row][col]:
            streak += 1
            r, c = r + dr, c + dc

        r, c = row - dr, col - dc
        while 0 <= r < N and 0 <= c < N and grid[r][c] == grid[row][col]:
            streak += 1
            r, c = r - dr, c - dc

        if streak >= 3: return False
    return True

def print_sol():
    for row in grid:
        print("".join(row))

backTrack(0, 0)
print_sol()