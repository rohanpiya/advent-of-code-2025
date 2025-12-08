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
size = []
for i in range(n):
    parent.append(i)
    size.append(1)

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

# new union returns true if it actually merged two different roots
def union(a, b):
    a2 = find(a)
    b2 = find(b)
    if a2 == b2:
        return False
    if size[a2] < size[b2]:
        parent[a2] = b2
        size[b2] += size[a2]
    else:
        parent[b2] = a2
        size[a2] += size[b2]
    return True

comp = n
k = 0
finalPairA = None
finalPairB = None

while comp > 1 and k < len(pairs):
    dist, a, b = pairs[k]
    merged = union(a, b)
    if merged:
        comp -= 1
        finalPairA = a
        finalPairB = b
    k += 1


multX = pts[finalPairA][0] * pts[finalPairB][0]
print(multX)

