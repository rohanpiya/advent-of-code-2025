with open("input.txt", "r") as f:
    grid = [list(line.rstrip("\n")) for line in f if line.strip()]

rows = len(grid)

if rows > 0:
    cols = len(grid[0])
else:
    cols = 0

neighbors = [(-1,-1), (-1,0), (-1,1),
             ( 0,-1),         ( 0,1),
             ( 1,-1), ( 1,0), ( 1,1)]

totRemoved = 0

while True:
    removals = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            adj = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                    if grid[nr][nc] == '@':
                        adj += 1
            if adj < 4:
                removals.append((r, c))

    if not removals:
        break

    # remove them
    for r, c in removals:
        grid[r][c] = '.'

    totRemoved += len(removals)

print("Total rolls removed:", totRemoved)
