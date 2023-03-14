input_info = input().split(' ')
input_info = [int(x) for x in input_info]

booth = input_info[0]
budget = input_info[1]

price = []
n = 0

for i in range(booth):
    info = input().split(' ')
    info = [int(x) for x in info]
    price.append(info[1]/info[0])

n = int(budget//min(price))
print(n)
