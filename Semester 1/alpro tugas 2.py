# while True:
#     x = int(input("Masukkan angka (1-9) => "))
#     if x == 1:
#         print("Angka Anda Satu ")
#     elif x == 2:
#         print("Angka Anda Dua ")
#     elif x == 3:
#         print("Angka Anda Tiga")
#     elif x == 4:
#         print("Angka Anda Empat")
#     elif x == 5:
#         print("Angka Anda Lima")
#     elif x == 6:
#         print("Angka Anda Enam")
#     elif x == 7:
#         print("Angka Anda Tujuh")
#     elif x == 8:
#         print("Angka Anda Delapan")
#     elif x == 9:
#         print("Angka Anda Sembilan")
#     else:
#         print("Angka Yang Anda Masukkan Tidak Masuk Ke Kategori")
#         break

while True:
    angka = ['satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan']
    x = int(input("Masukkan Angka => "))
    if x>=1 and x<=5:
        print("angka anda " + angka[x-1])
    elif x >= 6 and x<=9:
        print("Angka Anda "+ angka[x-1])
    else:
        print("Angka Yang Anda Masukkan Salah")
        break