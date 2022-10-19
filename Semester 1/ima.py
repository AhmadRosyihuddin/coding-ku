#Soal 1
# data1 = []
# data2 = []
# jumlah = []
# panjang = 0

# ukuran = int(input("Masukkan ukuran list yang pertama = "))
# for i in range(ukuran):
#     print("Masukkan data yang ke-",i,": ",end='')
#     list1 = int(input())
#     data1.append(list1)
    
# ukuran1 = int(input("Masukkan ukuran list yang pertama = "))
# for i in range(ukuran1):
#     print("Masukkan data yang ke-",i,": ",end='')
#     list2 = int(input())
#     data2.append(list2)

# if len(data1) > len(data2):
#     panjang= len(data1)
# else:
#     panjang = len(data2)

# for i in range(panjang):
#     if len(data1) > len(data2):
#         data2.append(0)
#     elif len(data2) > len(data1):
#         data1.append(0)
#     total = data1[i]+ data2[i]
#     jumlah.append(total)

# print('List Pertama\t\t=',data1[0:ukuran])
# print('List Kedua\t\t=',data2[0:ukuran1])
# print('Hasil Penjumlahan\t=',jumlah)


#Soal 2
# hari = ('senin','selasa','rabu','kamis','jumat','sabtu','minggu')
# x = str(input('Masukkan informasi, hari pertama bulan ini, jatuh pada hari : '))
# a = int(input('Masukkan Tanggal : '))
# for i in range(len(hari)):
#     if hari[i] == x:
#         m = i-1
# n = (a+m)%7
# print(n,m)
# print(hari[n])
    
    
    
    
    
    
    
    

#Soal 3
data = []
ganjil = []
genap = []
prima = []
ukuran = int(input("Masukkan Ukuran List = "))
for i in range(ukuran):
    print('Masukkan Data Yang Ke-',i,': ',end='')
    list1 = int(input())
    data.append(list1)

for i in data:
    if i % 2 == 0:
        if i not in genap:
            genap.append(i)
    else:
        if i not in ganjil:
            ganjil.append(i)
p = 0
for i in data:
    for y in range(1,i+1):
        if i%y==0:
            p += 1
    if p == 2:
        if i not in prima:
            prima.append(i)
    p = 0

print('List\t=',data)
print('Ganjil\t=',ganjil)
print('Genap\t=',genap)
print('Prima\t=',prima)