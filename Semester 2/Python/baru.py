# a = input('Masukkan Data : ')
# c =''
# b = 'HALO DUNIA!'
# def cek():
#     for i in range(len(b)):
#         if a[i].upper() == b[i] :
#             c = 'YA'
#         else:
#             return 'TIDAK'
#     return c
# print(cek())

# a = input().split()
# c = []
# for i in range(int(a[0])):
#     x = input().split()
#     c.append(x)

# saklar = 0
# lampu = []
# for i in range(len(c)):
#     if int(c[i][0]) != 0:
#         saklar += 1
#         if len(c[i])>2:
#             for y in range(1,len(c[i])):
#                 if c[i][y] not in lampu:
#                     lampu.append(c[i][y])

# print(saklar)
# print(lampu)

# if saklar == int(a[0]) and len(lampu) == int(a[1]):
#     print('YA')
# else:
#     print('TIDAK')    


# jmlh_komputer = int(input('=> '))
komputer = list(map(int,input('=> ').split()))
fakotor = []
jaringan = []
temp_jaringan = []
terhubung = False
for i in komputer:
    temp = []
    for y in range(2,i+1):
        if i % y == 0:
            temp.append(y)
    fakotor.append(temp)

for i in range(len(fakotor)-1):
    j = 0
    while terhubung == False and j < len(fakotor[i]):
        if fakotor[i][j] in fakotor[i+1]:
            terhubung = True
        else:
            terhubung = False
        j += 1
    print(terhubung)
    if terhubung == True:
        temp_jaringan.append(komputer[i])
        # print(temp_jaringan)
    else:
        temp_jaringan.append(komputer[i])
        jaringan.append(temp_jaringan)
        temp_jaringan = []
    j = 0
    terhubung = False
print(fakotor)
print(jaringan) 