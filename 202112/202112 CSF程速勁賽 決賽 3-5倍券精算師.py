goods = [int(eval(x)/100) for x in input().split(' ')]
dp = [False] * 51 # 預設是false
dp[0] = True # 可以湊到0元

for i in range(len(goods)):
    for j in range(50, goods[i] - 1, -1):
        dp[j] = dp[j] or dp[j - goods[i]]
    if dp[50]: # 如果可以成功湊到5000
        print(i+1)
        break
