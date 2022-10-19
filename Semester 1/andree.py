# Soal 1
# data1 = []
# data2 = []
# penjumlahan = []
# pengurangan = []
# start = True
# while start:
#     x = float(input('Masukkan data ke dalam list 1 : '))
#     data1.append(x)
#     a = input('input y untuk lanjut = ')
#     print()
#     if a != 'y':
#         start = False
# print('List 1 =',data1)
# print()

# while not start:
#     x = float(input('Masukkan data ke dalam list 2 : '))
#     data2.append(x)
#     a = input('input y untuk lanjut = ')
#     print()
#     if a != 'y':
#         start = True
# print('List 2 =',data2)


# if len(data1) == len(data2):
#     for i in range(len(data1)):
#         jumlah = data1[i]+data2[i]
#         kurang = data1[i]-data2[i]
#         penjumlahan.append(jumlah)
#         pengurangan.append(kurang)
#     print('Penjumlahan List1 + list2 =',penjumlahan)
#     print('Pengurangan List1 - list2 =',pengurangan)
# else:
#     print('Warning !!! Panjang List 1 DAn List 2 Tidak Sama')

# Soal 2
start = True
data = []
data2 = []
while start:
    x = str(input('Masukkan data ke dalam list  : ')).lower()
    data.append(x)
    for i in range(len(data)):
        if x not in data2:
            data2.append(x)
            break
    else:
        print()
        data2.remove(x)
        print('Duplikasi Terdeteksi\ndata',x,'ada di index ke-',data2.index(x),'\ndata',x,'sudah terhapus')
        print()
    a = input('input y untuk lanjut = ').lower()
    print()
    if a != 'y':
        start = False
print('My list =',data2)

# Soal 3
# start = 9
# jumlah = 0
# while start:
#     data = ['you','aku','me','kamu','i','love','you',
#             'saya','kamu','mereka','dia','apa','bis','makan','roti',
#             'nama','rosik','febi','lia','aul','febi','febi','febi','lia',
#             'nanda','nanda','zahra','natul']
#     x = input('Masukkan data yang di cari = ').lower()
#     print()
#     for i in range(len(data)):
#         if data[i]==x:
#             print('data',x.upper(),'ada di index ke-',i)
#             jumlah = jumlah + 1
#         elif x not in data:
#             print('Data Tidak Di Temukan')
#             break
#     else:
#         print()
#         print('Jumlah data',x.upper(),'sebanyak =',jumlah)
#     jumlah = 0
#     print()
#     a = input('y untuk cari lagi = ')
#     print()
#     if a != 'y':
#         start = 0