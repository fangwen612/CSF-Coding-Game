money = int(input())
bento = 0
point = 0

while(money >= 0):
    if point >= 5:
        point -= 4
        money -= 100
    else:
        money -= 150
        point += 1
    bento += 1

print(bento - 1)
