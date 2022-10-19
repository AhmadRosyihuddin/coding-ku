# def Unordersquentail(data,x):
#     i = 0
#     jumlah = 0
#     while i < len(data):
#         if data[i] == x:
#             print('{} Ada Di Index {}'.format(x,i))
#             jumlah += 1
#         i += 1
#     if jumlah == 0:
#         print('Data Not Found')

# squentail([2,3,5,6,7,34,2,4,6],2)

# def orderSquential(data,x):
#     i = 0
#     pos = []
#     while i < len(data) and data[i] <= x:
#         if x == data[i]:
#             pos.append(i)
#         i += 1
#     if len(pos) == 0:
#         return 'Data tidak di temukan'
#     else:
#         return pos

# print(orderSquential([1,2,5,6,7,8,10,13,23,34,56,77,89,100],10))


def BinarySearch(data,x):
    awal = 0
    akhir = len(data)-1
    hasil = []
    iterasi = 0
    while awal <= akhir:
        mid = (awal+akhir)//2
        if data[mid] == x:
            hasil.append(mid)
            idx = mid
            while idx+1 < len(data) and data[idx+1] == x:
                hasil.append(idx+1)
                idx += 1
            idx = mid
            while idx-1 >= 0 and data[idx-1] == x:
                hasil.append(idx-1)
                idx -= 1
            awal = mid+1
            akhir = mid -1
        
        elif data[mid] > x:
            akhir = mid - 1
        else:
            awal = mid + 1
        iterasi += 1

    if hasil == []:
        return ('Data Tidak Ada',iterasi)
    else:
        return (hasil,iterasi)
    
data = [1,4,4,4,4,4,4,4,4,4,5,6,7,8,9,10,13,15,16,20,33,33,33,33]
data1 = [4,10,12,17,19,21,25,27,32]
[hasil,iterasi] = BinarySearch(data,33)

print('Posisi Data=',hasil)
print('Jumlah Iterasi=',iterasi)


# binary Biasa
# def BinarySearch(data,x):
#     awal = 0
#     akhir = len(data)-1
#     found = False
#     while awal <= akhir and not(found):
#         mid = (awal+akhir)//2
#         if data[mid] == x:
#             found = True

#         elif data[mid] > x:
#             akhir = mid - 1
#         else:
#             awal = mid + 1

#     if found:
#         print(mid)
#     else:
#         print('Not Found')
        
# data = [2,3,4,5,11,23,45,77,88,121,334,456]
# BinarySearch(data,456)


# Hashing
# def remainderFunction (data,num):
#     return (data%num)
# def createHashTable(num):
#     temp=[]
#     for i in range(num):
#         temp.append('none')
#     return(temp)
# def putData(data,table):
#     for i in range(len(data)):
#         ind=remainderFunction(data[i],len(table))
#         table[ind]=data[i]
#     return(table)
# def searchHash(data,table):
#     hashVal=remainderFunction(data,len(table))
#     if data==table[hashVal]:
#         return True
#     else:
#         return False
    
# def collusion(data,num):
#     x = data**2
#     print(x)
#     c = str(x)
#     if len(c) != 2:
#         x = c[1:int(len(c)-1)]
#     print(x)

# def strVal(strData):
#     temp=0
#     for i in range (len(strData)):
#         temp=temp+ord(strData[i])
#     return(temp)

# # a = [2,4,5,3,1,3,5,7,8,100,263,9182]
# # data = createHashTable(10)
# # print(putData(a,data))
# # print(collusion(55,10))


# name = ['diah','indah','rini','budi']
# data = createHashTable(10)
# intName = [strVal(i) for i in name]
# print(putData(intName,data))
# print(intName)



