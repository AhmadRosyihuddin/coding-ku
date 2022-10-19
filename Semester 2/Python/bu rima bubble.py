data = [2,4,4,66,5,2,43,5,2,4,0,5,2,1,4,6,8,8,8,8]#[12,0,5,1,11,20,4,2]#[12,11,5,1,0]
n = len(data)
i = 0
cont = 1
min = 0
while i != n-1:
    i = 0
    print('Iterasi ke- {}'.format(cont))
    cont += 1
    for y in range(n-1):
        if data[y] > data[y+1]:
            data[y],data[y+1] = data[y+1],data[y]
            min = 0
        else:
            i += 1
            min += 1
        print(data)
    if min == 0:
        n -= 1
    else:
        n -= min
    print(min)
    print(y)


# data = [12,0,5,1,11,20,4,2]
# n = 0
# i = 0
# cont = 1
# while i != n-1:
#     i = 0
#     print('Iterasi Ke- {}'.format(cont))
#     cont += 1
#     for y in range(len(data)-1,n,-1):
#         if data[y] < data[y-1]:
#             data[y],data[y-1] = data[y-1],data[y]
#         else:
#             i += 1
#         print(data)
#     n += 1