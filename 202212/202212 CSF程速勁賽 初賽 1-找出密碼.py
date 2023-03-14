str = input()
ans = ''
for i in str:
    if i.isnumeric():
        ans += i
print(ans)
