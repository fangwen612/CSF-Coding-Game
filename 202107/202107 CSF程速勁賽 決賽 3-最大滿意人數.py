
''' 讀取輸入 '''
MAX_SIZE = eval(input())  # 攜帶寶可夢的最大數量
poke_lst = input().split(',')  # 存放寶可夢數值
poke_lst = [eval(x) for x in poke_lst]


def check_valid(lst):
    ''' 檢查是否滿足題目要求
    Parameter:
    lst (list): 一個串列，儲存寶可夢數值
   '''
    global COUNT
    value_sum = 0  # 計算一個訓練家的寶可夢數值加總
    start_i = 0    # 訓練家分配的寶可夢在 lst 的起始索引值

    for i in range(len(lst)):
        # 檢驗一個訓練家的寶可夢數值是否由小到大排序
        if value_sum != 0:
            if lst[i] < lst[i-1]:
                break

        value_sum += lst[i]  # 累加一個訓練家的寶可夢數值

        if value_sum > MAX_VALUE:  # 超出平均分配的數值
            break
        elif value_sum == MAX_VALUE:
            value_sum = 0  # 重新累加下一人的寶可夢數值

            # 檢查所攜帶的寶可夢數量是否超過上限
            if i - start_i + 1 > MAX_SIZE:
                break
            else:
                start_i = i + 1

            # 檢查是否分配完所有寶可夢
            if i == len(lst)-1:
                COUNT += 1


''' 以遞迴方式窮舉所有分配方式，並逐一檢驗 '''


def 計算分配方法數(lst, k=0):
    ''' 依給定條件計算分配方法數
    Parameter:
    lst (list): 一個串列，儲存寶可夢數值
    k (int): 一個整數，代表索引值
   '''

    if k == len(lst):  # 進行分配
        check_valid(lst)
    else:
        # 以遞迴呼叫窮舉所有可能的分配方式
        for i in range(k, len(lst)):
            lst[k], lst[i] = lst[i], lst[k]
            計算分配方法數(lst, k+1)
            lst[k], lst[i] = lst[i], lst[k]


MAX_VALUE = sum(poke_lst)/3  # 平均分配的寶可夢數值總和
COUNT = 0  # 分配方式的方法數

計算分配方法數(poke_lst)

print(COUNT)
