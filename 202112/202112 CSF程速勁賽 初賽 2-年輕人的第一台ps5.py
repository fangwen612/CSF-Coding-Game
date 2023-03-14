x, y = map(int, input().split(' '))  # 把x, y轉成int
ps5 = input().split(' ')
competitor = [0.0] * y  # 拿來放每個網站各有多少分母

for i in range(x):
    websites = input().split(' ')
    for web in websites:
        competitor[int(web)-1] += (1 / len(websites))  # 因為網站從1開始，所以要-1

ans = [0, 0]
for i in range(y):
    prob = min(1.0, int(ps5[i]) / (competitor[i] + 1))  # 要把自己加進分母，最大100%
    if(prob > ans[0]):
        ans = [prob, i]

print(ans[1]+1)
