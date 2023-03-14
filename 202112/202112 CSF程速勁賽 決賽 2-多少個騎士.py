m, n = map(int, input().split(' '))

if m > n:  # swap, 讓m會是比較小那個
    t = m
    m = n
    n = t

ans = 0

if m == 1:
    ans = n
elif m == 2:
    if n % 4 > 2:
        ans = 4 * int(n/4) + 4
    else:
        ans = 4 * int(n/4) + 2 * (n % 4)
else:
    ans = int((m * n + 1)/2)

print(ans)
