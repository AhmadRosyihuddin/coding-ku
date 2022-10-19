# def squetialSearch(data,x):
    # i = 0
    # iterasi = 0
    # hasil = []
    # while i < len(data):
    #     if data[i] == x:
    #         hasil.append(i)
    #     iterasi += 1
    #     i += 1
    # if hasil == []:
    #     return ('Data Tidak Ada',iterasi)
    # else:
    #     return (hasil,iterasi)

# data = [2,3,5,43,3,3,45,32,2,34,2,4]
# [hasil,iterasi] = squetialSearch(data,2)

# print('Posisi Data=',hasil)
# print('Jumlah Iterasi=',iterasi)

# def OrderSquential(data,x):
#     i = 0
#     iterasi = 0
#     hasil = []
#     while i < len(data) and data[i] <= x:
#         if data[i] == x:
#             hasil.append(i)
#         iterasi += 1
#         i += 1
#     if hasil == []:
#         return ('Data Tidak Ada',iterasi)
#     else:
#         return (hasil,iterasi)

# data = [2,3,4,4,5,6,12,12,34,56,57,66,77,89,90,100,121,134,145]
# [hasil,iterasi] = OrderSquential(data,4)

# print('Posisi Data=',hasil)
# print('Jumlah Iterasi=',iterasi)


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
                print
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
    
data = [1,4,4,4,4,4,4,4,4,4,5,6,7,8,9,10,13,15,16,20,33]
[hasil,iterasi] = BinarySearch(data,1)

print('Posisi Data=',hasil)
print('Jumlah Iterasi=',iterasi)