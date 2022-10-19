
angka = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romawi = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
x = int(input("Masukkan Angka : "))
for i in range(len(angka)):
    konvers = x // angka[i]
    if konvers!= 0:
        print(romawi[i]*konvers,end='')
    x %= angka[i]