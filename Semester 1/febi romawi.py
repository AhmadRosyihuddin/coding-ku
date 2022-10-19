angka = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romawi = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

x = int(input("Masukkan Angka : "))
sisa = x
start = True
jumlah = 0
while start:
    konversi = sisa//angka[jumlah]
    #print(jumlah,sisa,angka[jumlah],konversi)
    if konversi != 0:
        print(konversi*romawi[jumlah],end='')
    sisa = sisa % angka[jumlah]
    #print('sisa :',sisa)
    if sisa == 0:
        start = False
    jumlah += 1