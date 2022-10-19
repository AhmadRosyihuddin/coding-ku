#menampilkan bilangan ganjil
x = 0
angka = int(input('Jumlah angka ganjil : '))
for ganjil in range (angka*2) :
    if ganjil % 2 == 1 :
        x = x + 1
        print('Bilangan Ganjil -',x,'=',ganjil)



#range (angka*2),untuk menampilkan sejumlah angka tersebut harus dikali 2,karena dalam 2 angka hanya terdapat 1 ganjil