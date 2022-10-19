# def remainderFunction (data,num):
#     return (data%num)

# def createHashTable(num):
#     return [[None] for i in range(num)]

# def putData(data,table):
#     for i in range(len(data)):
#         ind=remainderFunction(data[i],len(table))
#         if table[ind][0] == None:
#             table[ind][0]=data[i]
#         else:
#             table[ind].append(data[i])
#     return(table)

# def searchHash(data,table):
#     hashVal=remainderFunction(data,len(table))
#     iterasi = 1
#     if table[hashVal] != 'none':
#         for i in range(len(table[hashVal])):
#             if data == table[hashVal][i]:
#                 print(iterasi)
#                 return (hashVal,i,True)
#             iterasi += 1
#     else:
#         return False


# data = [10,1,3,5,8,7,12,11,44]
# hashTabel = createHashTable(12)
# hashTabel = putData(data,hashTabel)
# findData = 0
# found = searchHash(findData,hashTabel)
# if not found:
#     print('{} Is Not In The Hash Table'.format(findData))
# else:
#     print('{} Is In Slot {} Index : {}'.format(findData,found[0],found[1]))
#     print('Data In Slot [{}] : {}'.format(found[0],hashTabel[found[0]]))


perbandingan = 0
pergeseran = 0
def mergeSort(data):
    global perbandingan,pergeseran
    if len(data) > 1:
        print("splitting",data," = ",end="")
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        
        print(left,",",right)

        mergeSort(left)
        mergeSort(right)
        i,j,k = 0,0,0

        print("merging",left," and ",right," = ",end="")

        while i < len(left) and j < len(right):
            perbandingan += 1 
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
                pergeseran += 1
            else:
                data[k] = right[j]
                j += 1
                pergeseran += 1
            k += 1
        
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
            pergeseran += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
            pergeseran += 1
        print(data,"\n")
    else:
        print("no spliting = ",data)

a = [5,3,2,4,1]
print("Sebelum di urutkan : ",a)
mergeSort(a)
# Pergeseran dilihat dari data yang perbandingannya true
print("Banyak Pergeseran = ",pergeseran)
# Pergeseran dilihat dari banyaknya perbandingan data
print("Banyak Perbandingan = ",perbandingan)
print("Sesudah di urutkan : ",a)