buildNum = int(input())
buildings = [eval(x) for x in input().split(' ')]  # 把input用空格隔開，再轉成int

buildings.sort() # 排序
ans = buildNum

for i in range(buildNum):
    ans = min(ans, buildings[i] + buildNum - i - 1)

print(ans)
