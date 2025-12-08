with open('input.txt', 'r') as f:
    lines = [line.rstrip("\n") for line in f]


width = max(len(line) for line in lines)
i = 0
while i < len(lines):
    if len(lines[i]) < width:
        lines[i] = lines[i].ljust(width)
    i += 1

height = len(lines)
operations = lines[height - 1]
digits = lines[:height - 1]

prob = [-1]
col = 0
while col < width:
    r = 0
    allSpaces = True
    while r < height:
        if lines[r][col] != ' ':
            allSpaces = False
        r += 1
    if allSpaces:
        prob.append(col)
    col += 1
prob.append(width)

total = 0

i = 0
while i < len(prob) - 1:
    left = prob[i]
    right = prob[i + 1]

    if right - left > 1:
        op = ''
        k = left + 1
        while k < right:
            ch = operations[k]
            if ch == '+' or ch == '*':
                op = ch
            k += 1

        nums = []
        r = 0
        while r < len(digits):
            segment = digits[r][left + 1 : right].strip()
            if segment != "":
                nums.append(int(segment))
            r += 1

        if op == '*':
            result = 1
            j = 0
            while j < len(nums):
                result = result * nums[j]
                j += 1
        else:
            result = 0
            j = 0
            while j < len(nums):
                result = result + nums[j]
                j += 1

        total += result
        
    i += 1

print(total)
