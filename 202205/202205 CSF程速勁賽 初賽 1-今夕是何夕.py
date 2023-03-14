data = input()
data = data.split(" ")
data = [ int(i) for i in data ]

M = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, 13):
    M[i] += M[i-1]

ans = M[data[1] - 1]
ans += data[2]

if (data[0] % 400 == 0) or (data[0] % 4 == 0 and data[0] % 100 != 0):
    if data[1] > 2:
        ans += 1

print(ans)