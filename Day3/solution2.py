def maxKDigits(s, k):
    n = len(s)
    start = 0
    resultChars = []
    for remaining in range(k, 0, -1):
        end = n - remaining + 1 
        w = s[start:end]
        maxDigits = max(w)
        idx = w.index(maxDigits) 
        resultChars.append(maxDigits)
        start = start + idx + 1
    return ''.join(resultChars)


def totalForFile(fileName, k):
    total = 0
    with open(fileName, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            best = maxKDigits(line, k)
            total += int(best)
    return total

total = totalForFile("input.txt", 12)
print(total)
