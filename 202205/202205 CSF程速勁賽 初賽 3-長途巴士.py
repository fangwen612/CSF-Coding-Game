x, p = map(int, input().split(' '))
dp = [0] * 1000
for i in range(p):
    n, f, t = map(int, input().split(' '))
    dp[f] += n
    dp[t] -= n

cnt = 0
for i in range(1000):
    cnt += dp[i]
    if cnt > x:
        print('no')
        break

if cnt <= x:
    print('yes')
