a = input().split()
c = []
for i in range(int(a[0])):
    x = input().split()
    c.append(x)

saklar = 0
lampu = []
for i in range(len(c)):
    if int(c[i][0]) != 0:
        saklar += 1
        if len(c[i])>=2:
            for y in range(1,len(c[i])):
                if c[i][y] not in lampu:
                    lampu.append(c[i][y])

if saklar == int(a[0]) and len(lampu) == int(a[1]):
    print('YA')
else:
    print('TIDAK')   