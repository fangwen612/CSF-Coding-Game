numbers = {'odd': 0, 'even': 0, 'float': 0,  'positive': 0, 'negative': 0}

for index in range(5):
    number = input()
    number = int(number) if number.lstrip('-').isdigit() else float(number)
    if type(number) is int:
        if number % 2 == 0:
            numbers['even'] += 1
        else:
            numbers['odd'] += 1
    elif type(number) is float:
        numbers['float'] += 1

    if number > 0:
        numbers['positive'] += 1
    elif number < 0:
        numbers['negative'] += 1

print('奇數%d個' % (numbers['odd'],))
print('偶數%d個' % (numbers['even'],))
print('正數%d個' % (numbers['positive'],))
print('負數%d個' % (numbers['negative'],))
print('浮點數%d個' % (numbers['float'],))
