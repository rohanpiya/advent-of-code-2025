pts = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])
            pts.append([x, y, z])

n = len(pts)
pairs = []
i = 0
while i < n:
    j = i + 1
    x2 = pts[i][0]
    y2 = pts[i][1]
    z2 = pts[i][2]
    while j < n:
        x3 = x2 - pts[j][0]
        y3 = y2 - pts[j][1]
        z3 = z2 - pts[j][2]
        dist2 = x3*x3 + y3*y3 + z3*z3
        pairs.append([dist2, i, j])
        j += 1
    i += 1


pairs.sort()
parent = []
for i in range(n):
    parent.append(i)
size = [1] * n

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    a2 = find(a)
    b2 = find(b)
    if a2 == b2:
        return
    if size[a2] < size[b2]:
        parent[a2] = b2
        size[b2] += size[a2]
    else:
        parent[b2] = a2
        size[a2] += size[b2]

k = 0
while k < 1000 and k < len(pairs):
    dist, a, b = pairs[k]
    union(a, b)
    k += 1

circuit_sizes = {}

i = 0
while i < n:
    root = find(i)
    if root not in circuit_sizes:
        circuit_sizes[root] = 0
    circuit_sizes[root] += 1
    i += 1

sizes = sorted(circuit_sizes.values(), reverse=True)
mult = sizes[0] * sizes[1] * sizes[2]
print(mult)