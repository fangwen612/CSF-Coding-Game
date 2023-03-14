n = int(input())

for i in range(1, n):
    for x in range(n - i):
        print(' ', end='')
    for y in range(i*2-1):
        if y == 0 or y == i*2-2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n):
    for x in range(i):
        print(' ', end='')
    for y in range((n-i)*2-1):
        if y == 0 or y == (n-i)*2-2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
