# Buuble Sort Biasa (Asscending)
# def Bubble(data):
#     for i in range(len(data)-1):
#         print('Iterasi Ke-',i)
#         for y in range(i+1,len(data)):
#             if data[i] > data[y]:
#                 data[i],data[y] = data[y],data[i]
#             print(data)
#     return data
# data = [12,0,5,1,11,20,4,2]
# print(Bubble(data))
                

# Bubble Sort Modifiksasi Jika data Terurut(Asscending)
# def BubbleMod(data):
#     n = len(data)
#     i = 0
#     cont = 1
#     min = 0
#     while i != n-1:
#         i = 0
#         print('Iterasi ke- {}'.format(cont))
#         cont += 1
#         for y in range(n-1):
#             if data[y] > data[y+1]:
#                 data[y],data[y+1] = data[y+1],data[y]
#                 min = 0
#             else:
#                 i += 1
#             print(data)
#         n -= 1
#     return data

# data = [12,0,5,1,11,20,4,2]
# print('Data Awal :',data)
# print('Hasil :',BubbleMod(data))

# Bubble Sort  Ganjil Genap (Asscending)
# def BubbleGanjilGenap(data):
#     print('Data Awal :',data)
#     ganjil = 1
#     genap = 0
#     nilai = len(data)-1
#     n = 0
#     while ganjil > 0 or genap < nilai*2:
#         ganjil = 0
#         if n == 0:
#             print('Genap - Ganjil Sorting')
#         else:
#             print('Ganjil - Genap Sorting')
#         for i in range(n,len(data)-1,2):
#             if data[i] > data[i+1]:
#                 data[i],data[i+1] = data[i+1],data[i]
#                 genap += 1
#             else:
#                 if n == 0:
#                     ganjil += 1
#         print(data)
#         if n == 0:
#             n += 1
#         else:
#             n -= 1
#     return data

# data = [2,2,2,2,1,1,1,1,1,2,0]
# print('Hasil =',BubbleGanjilGenap(data))

# Selection Sort Biasa (Asscending)
# def Selection(data):
#     for i in range(len(data)):
#         temp = i
#         for y in range(1+i,len(data)):
#             if data[temp] > data[y]:
#                 temp = y
#         data[i],data[temp] = data[temp],data[i]
#         print(data)
#     return data

# data = [4,3,10,1,9,2]
# print('Data Awal :',data)
# print('Hasil :',Selection(data))

# Selectiom Sort Modifikasi Max Min (Asscending)
# def SelectionMod(data):
#     n = len(data)-1
#     print()
#     for i in range(len(data)//2):
#         print('Iterasi Ke-',i+1)
#         temp = i
#         for j in range(i+1,n+1): # Iterasi untuk Mencari Nilai Makasimal
#             if data[temp] > data[j]:
#                 temp = j
#         data[i],data[temp] = data[temp],data[i]
#         print('Minimum : ',data)
        
#         temp = i
#         for y in range(n,-1,-1): # Iterasi Untuk Mencari Nilai Maksimal
#             if data[temp] < data[y]:
#                 temp = y
#         data[n],data[temp] = data[temp],data[n]
#         print('Maksimum : ',data)
#         print()
#         n -= 1
#     return data

# data = [10,2,5,8,1,20,7,12,4]
# print('Data Awal :',data)
# print('Hasil :',SelectionMod(data))


# Insertion Sort Biasa
def insertionSort(data):
    print('Data Awal =',data)
    for i in range(1,len(data)):
        key=data[i]
        ind=i
        while (ind>0 and data[ind-1]>key):
            data[ind]=data[ind-1]
            ind=ind-1
            print('inner :',data)
            data[ind]=key
            print('Sorted :',data)
            print()
    return data

data = [10,2,1,5,20,8,15]
print('Hasil =',insertionSort(data))


# Insertion Sort Dari Belakang
# def insertionBack(data):
#     print('Data Awal =',data)
#     for i in range(len(data)-2,-1,-1):
#         key = data[i]
#         ind = i
#         while ind < len(data)-1 and data[ind+1] < key:
#             data[ind] = data[ind+1]
#             ind += 1
#             print('Inner :',data)
#             data[ind] = key
#             print('Sorted :',data)
#             print()
#     return data

# data = [10,2,1,5,20,8,15]
# print('Hasil =',insertionBack(data))



#FEBI FADLILAH NUR AMINAH (200411100115)
# import random
# def pengecekan(data) :
#     if len(data)%2 == 0 :
#         return (len(data)//2)
#     else :
#         return ((len(data)+1)//2)

# def pengurutan(data) :
#     for i in range (len(data)-1) :
#         if data[i]>data[i+1] :
#             return True
#     return False

# def sorting (data) :
#     print ('Data = ',data)
#     n = pengecekan(data)
#     x = len(data)
#     i = 0
#     while i < (n) :
#         if pengurutan(data) :
#             for f in range (0,x-1,2) :
#                 if data[f] > data[f+1] :
#                     data[f],data[f+1] = data[f+1],data[f]
#             print(f'Genap - ganjil Sorting\n{data}')
#         if pengurutan(data) :
#             for b in range (1,x-1,2) :
#                 if data[b] > data[b+1] :
#                     data[b],data[b+1] = data[b+1],data[b]
#             print(f'Ganjil - genap Sorting\n{data}')
#         i+=1
#     return data


# a = [13,12,10,8,7,5,11,2]
# #a = [1,2,3,4,5]
# #a = random.sample(range(0,20),9)
# print ('Data yang sudah urut = ',sorting(a))


# def jilnap(data):
#     counter = 0
#     n = len(data)
#     urutan = True
#     print('Data = ',data)
#     while urutan:
#         urutan = False
#         for i in range(n-1):
#             if data[i] > data[i+1]:
#                 urutan = True
#         if urutan:
#             if counter %2 == 0 :
#                 print('Genap-Ganjil Sorting')
#                 for i in range(0,n-1,2):
#                     if data[i] > data[i+1]:
#                         data[i],data[i+1] = data[i+1],data[i]
#                 print(data)
#             else:
#                 print('Ganjil-Genap Sorting')
#                 for i in range (1,n-1,2):
#                     if data[i] > data[i+1]:
#                         data[i],data[i+1] = data[i+1],data[i]
#                 print(data)
#         counter+=1
#     print('Hasil = ',data)
# jilnap([2,2,2,2,1,1,1,1,1,2,0])

