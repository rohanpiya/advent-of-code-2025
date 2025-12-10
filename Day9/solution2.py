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

edges = []
for i in range(n):
    x1 = pts[i][0]
    y1 = pts[i][1]
    x2 = pts[(i + 1) % n][0]
    y2 = pts[(i + 1) % n][1]
    if x1 == x2:
        if y1 < y2:
            edges.append([x1, x2, y1, y2])
        else:
            edges.append([x1, x2, y2, y1])
    else:
        if x1 < x2:
            edges.append([x1, x2, y1, y2])
        else:
            edges.append([x2, x1, y1, y2])

maxArea = 0

for i in range(n):
    x1 = pts[i][0]
    y1 = pts[i][1]
    for j in range(n):
        x2 = pts[j][0]
        y2 = pts[j][1]

        xSmall = min(x1, x2)
        xBig = max(x1, x2)
        ySmall = min(y1, y2)
        yBig = max(y1, y2)

        width = xBig - xSmall + 1
        height = yBig - ySmall + 1
        area = width * height

        if area > maxArea:
            isValid = True

            for k in range(len(edges)):
                ex1 = edges[k][0]
                ex2 = edges[k][1]
                ey1 = edges[k][2]
                ey2 = edges[k][3]

                if ex2 > xSmall and ex1 < xBig and ey2 > ySmall and ey1 < yBig:
                    isValid = False
                    break

            if isValid:
                maxArea = area

print(maxArea)