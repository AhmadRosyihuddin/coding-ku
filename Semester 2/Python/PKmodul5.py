# Insertion Sort Modif
# def insertionBack(data):
#     print('Data : ',data)
#     for i in range(len(data)-2,-1,-1):
#         key = data[i]
#         ind = i
#         print('Key, Data[{}] : {}'.format(i,key))
#         while ind < len(data)-1 and data[ind+1] < key:
#             data[ind] = data[ind+1]
#             ind += 1
#             print('Inner Sorting =',data)
#             data[ind] = key
#         if i == 0 :
#             print('SortedData',data)
#         else:
#             print('Data : ',data)

# data = [10,2,4,5,20,8,15]
# insertionBack(data)

def BubbleMod(data):
    n = len(data)
    i = 0
    cont = 1
    while i < n:
        i = 0
        print('Iterasi ke- {} jumlah iterasi - {}'.format(cont,n-1))
        cont += 1
        for y in range(n-1):
            if data[y] > data[y+1]:
                data[y],data[y+1] = data[y+1],data[y]
            else:
                i += 1
            print('{} = {}'.format(y+1,data))
        n -= 1
    return data

data1 = [-3,0,1,4,6,8,10,12]
data2 = [10,2,5,8,1,20,2,2,4]
data3 = [4,4,3,4,4,4,4]
print('Data Awal :',data3)
print('Hasil :',BubbleMod(data2))