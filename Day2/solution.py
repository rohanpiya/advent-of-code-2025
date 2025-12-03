def isInvalidId(n):
    s = str(n)
    for i in range(1, len(s)//2 + 1):
        if len(s) % i ==0:
            chunk = s[:i]
            if chunk * (len(s)//i) == s:
                return True
    return False
    
    # if len(s) % 2 !=0:
    #     return False
    # half = len(s) // 2
    # return s[:half] == s[half:] 

ranges = []

with open("input.txt", "r") as f:
    line = f.read().strip()
    rangeList = line.split(',')

    for r in rangeList:
        startEndList = r.split('-')
        ranges.append([int(startEndList[0]), int(startEndList[1])])

totalInvalidSum = 0

for start,end in ranges:
    for num in range(start, end+1):
        if isInvalidId(num):
            totalInvalidSum += num

print(f"Answer: {totalInvalidSum}")