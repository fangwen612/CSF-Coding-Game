seq = input().split(' ')
c = ["  ___  ",
     " /   \ ",
     "|     |",
     " \___/ "]
t = ["      ",
     "  /\  ",
     " /  \ ",
     "/____\\"]
s = [" _____ ",
     "|     |",
     "|     |",
     "|_____|"]
r = ["", "", "", ""]

for w in seq:
    for i in range(4):
        if w == 'c':
            r[i] += (c[i])
        elif w == 't':
            r[i] += (t[i])
        elif w == 's':
            r[i] += (s[i])

for i in range(4):
    print(r[i])
