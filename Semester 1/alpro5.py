# Soal 1
# start = True
# while start:
#     n = int(input("Masukkan Size : "))
#     for i in range(n+1):
#         print(" "*(n//2)+"x")
#     print()

#     for i in range(n+1):
#         if i == 0 or i == n:
#             print("x"*n)
#         elif i == (n//2):
#             print("x"*n)
#         elif i > (n//2):
#             print("x")
#         else:
#             print(" "*(n-1)+"x")
#     print()

#     for i in range(n+1):
#         if i == 0 or i == n:
#             print("x"*n)
#         elif i == (n//2):
#             print("x"*n)
#         elif i > (n//2):
#             print("x"+" "*(n-2)+"x")
#         else:
#             print("x")
#     print()
#     a = str(input("Mau Ulang? (y/t) => ")).lower()
#     if a == 'y':
#         continue
#     else:
#         start = False
    
# Soal 2
# x = int(input('Masukkan Angka : '))
# for i in range(2,x+1):
#     if x > 1:
#         for y in range(2,i):
#             if i % y == 0:
#                 break
#         else:
#             print('Bilangan Prima :',i)



# Soal 3
# kendaraan = ['mobil','truck','bus']
# tarif = [50000,75000,85000]
# print('Cek Tarif Masuk TOL\nDaftar Mobil\n1. Mobil\n2. Truck\n3. Bus\n4. Exit')
# start = True
# while start:
#     x = str(input('Tulis Pilihan Anda : ')).lower()
#     for i in range(len(kendaraan)):
#         if kendaraan[i] == x:
#             print('Tarif',x.title(),': Rp.',tarif[i])
#         elif x == 'exit':
#             start = False 
        