
COIN_LST = [10, 5, 4, 1]        # 硬幣幣值

money = int(input())
change_lst = [0] + [None]*money  # 儲存最小兌換個數

for i in range(1, money+1):
    lst = []  # 記錄 COIN_LST 的最小兌換數

    for c in COIN_LST:
        if i-c < 0:  # 不能兌換
            continue
        elif change_lst[i-c] == None:  # 不能兌換
            continue
        else:   # 計算幣值 c 的兌換個數
            lst.append(change_lst[i-c])

    if len(lst) > 0:    # 取出最小兌換個數
        change_lst[i] = min(lst) + 1

if change_lst[-1] == None:
    print('無法兌換')
else:
    print(change_lst[-1])
