current = 50
zeroCount = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        val = int(line[1:])

        if direction.upper() == 'L':
            current -= val
            current = current % 100
            if current == 0:
                zeroCount += 1
        elif direction.upper() == 'R':
            current += val
            current = current % 100
            if current == 0:
                zeroCount += 1

print(zeroCount)