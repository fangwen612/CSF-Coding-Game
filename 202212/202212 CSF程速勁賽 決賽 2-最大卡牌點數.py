card = input().split(' ')
card = [int(x) for x in card]
ans = 0

game_round = int(len(card) / 3)
card.sort()
for i in range(len(card) - 2, game_round - 1, -2):
    ans += card[i]

print(ans)
