import random

def genarate_random(jumlah,min,max):
    data = []
    for i in range(jumlah):
        data.append(random.randint(min,max))
    return data

def insertionSort(data):
    for i in range(1,len(data)):
        key=data[i]
        ind=i
        while (ind>0 and data[ind-1]>key):
            data[ind]=data[ind-1]
            ind=ind-1
            data[ind]=key
    return data

def squentail(data,x):
    i = 0
    jumlah = []
    while i < len(data):
        if data[i] == x:
            jumlah.append(i)
        i += 1
    if jumlah == []:
        return '{} Is Not Found'.format(x)
    return '{} Is In : {}'.format(x,jumlah)

def orderSquential(data,x):
    i = 0
    pos = []
    while i < len(data) and data[i] <= x:
        if x == data[i]:
            pos.append(i)
        i += 1
    if len(pos) == 0:
        return '{} is not found , numberOfIteration: {}'.format(x,i)
    else:
        return '{} is in : {} , numberOfIteration: {}'.format(x,pos,i)

def BinarySearch(data,x):
    awal = 0
    akhir = len(data)-1
    found = False
    iterasi = 0
    while awal <= akhir and not(found):
        mid = (awal+akhir)//2
        if data[mid] == x:
            found = True

        elif data[mid] > x:
            akhir = mid - 1
        else:
            awal = mid + 1
        iterasi += 1

    if found:
        return '{} Is In : {} , numberOfIteration : {}'.format(x,mid,iterasi)
    else:
        return '{} Is Not Found , numberOfIteration : {}'.format(x,iterasi)

data = genarate_random(500,0,2000)
# print('Data =',data,'\n')
# print(squentail(data,100))
# print(squentail(data,20))
# print(squentail(data,500))
# print(squentail(data,241))

# insertionSort(data)
# print('Data =',data,'\n' )
# print(orderSquential(data,79))
# print(orderSquential(data,100))
# print(orderSquential(data,1))
# print(orderSquential(data,90))


insertionSort(data)
print('Data =',data,'\n' )
print(BinarySearch(data,79))
print(BinarySearch(data,100))
print(BinarySearch(data,29))
print(BinarySearch(data,188))