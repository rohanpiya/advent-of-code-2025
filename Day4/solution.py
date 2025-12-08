with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)

if rows > 0:
    cols = len(grid[0])
else:
    cols = 0

neighbors = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1)
]

aCount = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != '@':
            continue
        adj = 0
        for dr, dc in neighbors:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    adj += 1

        # Check the rule: fewer than 4 adjacent '@'
        if adj < 4:
            aCount += 1

print(f"Accessible rolls: {aCount}")