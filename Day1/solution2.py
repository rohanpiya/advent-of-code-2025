current = 50
zeroCount = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        val = int(line[1:])

        for i in range(val):
            if direction.upper() == 'L':
                current = (current - 1) % 100
                if current == 0:
                    zeroCount += 1
            elif direction.upper() == 'R': 
                current = (current + 1) % 100
                if current == 0:
                    zeroCount += 1

print(zeroCount)