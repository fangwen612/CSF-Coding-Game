s = input()

romanmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
ans = 0
prev = None
for i in s:
    if (i == 'V' or i =='X') and prev == 'I':
        ans += romanmap[i] - 2
    elif (i == 'L' or i =='C') and prev == 'X':
        ans += romanmap[i] - 20
    elif (i == 'D' or i =='M') and prev == 'C':
        ans += romanmap[i] - 200
    else:
        # Add to count
        ans += romanmap[i]
    prev = i

print(ans)