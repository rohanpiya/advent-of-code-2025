def maxTwoDigitsFromLine(s: str):
    digits = [int(ch) for ch in s]
    n = len(digits)
    suffixMax = [0]*n

    for i in range(n-1, -1, -1):
        if i == n-1:
            suffixMax[i] = -1
        else:
            suffixMax[i] = max(digits[i+1], suffixMax[i+1])

    best = -1
    for i in range(0, n-1):
        rightMax = suffixMax[i]
        if rightMax == -1:
            continue
        candidate = digits[i]*10 + rightMax
        if candidate > best:
            best = candidate

    if best != -1:
        return best
    else:
        return 0

total = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            total += maxTwoDigitsFromLine(line)
print(total)
