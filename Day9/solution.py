pts = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            x = int(parts[0])
            y = int(parts[1])
            pts.append([x, y])

n = len(pts)
maxArea = 0

for i in range(n):
    x1 = pts[i][0]
    y1 = pts[i][1]
    for j in range(i+1, n):
        x2 = pts[j][0]
        y2 = pts[j][1]
        width = abs(x1-x2)
        height = abs(y1-y2)
        area = (width + 1) * (height + 1)
        if area > maxArea:
            maxArea = area
print(maxArea)