size = int(input())
r = int(input())
s = input()
pos = [s[0], int(s[1])]

ans = ""

for i in range(r):
    laser = input()
    # print(pos, end = ', laser = ')
    # print(laser)
    if pos[0] in laser:
        if chr(ord(pos[0])+1) in laser or pos[0] == chr(ord('A')+size-1):
            ans+= 'L'
            pos[0] = chr(ord(pos[0])-1)
        elif chr(ord(pos[0])-1) in laser or pos[0] == 'A':
            ans+= 'R'
            pos[0] = chr(ord(pos[0])+1)
    elif str(pos[1]) in laser:
        if str(pos[1]+1) in laser or pos[1] == size:
            ans+= 'U'
            pos[1] -= 1
        elif str(pos[1]-1) in laser or pos[1] == 1:
            ans+= 'D'
            pos[1] += 1
    else:
        ans+= 'S'
print(ans)