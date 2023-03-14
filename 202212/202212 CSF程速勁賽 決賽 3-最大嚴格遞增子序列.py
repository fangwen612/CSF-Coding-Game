input_list = input().split(' ')
input_list = [int(x) for x in input_list]

tmp_LIS = [input_list[0]] # 暫時的子序列
pos = [0] # 每個元素能放的最合適位置
flag = 0 # 確認是否為最大元素

for i in range(1, len(input_list)):
    tmp_LIS_index = len(tmp_LIS) - 1
    tmp = input_list[i]
    flag = 0

    while tmp <= tmp_LIS[tmp_LIS_index] and tmp_LIS_index >= 0:
        tmp_LIS_index -= 1
        flag = 1
    
    if flag:
        tmp_LIS[tmp_LIS_index + 1] = tmp
    else:
        tmp_LIS.append(tmp)

    pos.append(tmp_LIS_index + 1)

print(max(pos) + 1)