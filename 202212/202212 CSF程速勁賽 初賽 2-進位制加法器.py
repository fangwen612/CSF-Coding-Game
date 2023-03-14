input_list = input().split(' ')
n = int(input_list[0])
a, b = input_list[1], input_list[2]

# 補成相同長度
while len(a) < len(b):
    a = '0' + a
while len(b) < len(a):
    b = '0' + b

ans = ''
carry, tmp = 0, 0
for i in range(len(a) - 1, -1, -1):
    tmp = int(a[i]) + int(b[i]) + carry
    if tmp >= n:
        carry = 1
        tmp -= n
    else: 
        carry = 0
    ans = str(tmp) + ans

if carry != 0:
    ans = str(carry) + ans

print(ans)


