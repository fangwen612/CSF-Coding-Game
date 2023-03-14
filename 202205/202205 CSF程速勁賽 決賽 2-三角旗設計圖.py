data = input()
data = data.split(" ")
data = [ int(i) for i in data ]

line = [0]
curr = []
line_c = 0
for i in range(len(data)):
    curr.append(data[i] * 2 - 1)
    line_c += curr[i] + 1
    line.append(line_c)

maxH = max(data)
Matrix = ["" for y in range(maxH)]

for h in range(maxH): # 高度
    for j in range(len(data)): # 數量
        if curr[j] > 0:
            # 根據起始處，前面填入空格
            while(len(Matrix[h]) < line[j]):
                Matrix[h] += " "
            
            # 起始處開始填空格
            for i in range(h):
                Matrix[h] += " "

            # 填入*
            for i in range(curr[j]):
                Matrix[h] += "*"
            curr[j] -= 2

for i in range(len(Matrix)):
    print(Matrix[i])
