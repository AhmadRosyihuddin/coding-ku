'''
Algoritma menu menghitung luas segitiga
1. menampilkan menu
2. membuat opsi untuk user menginput data
3. membuat kondisi jika user menginput data
4. kondisi jika user menginput angka 1 
5. maka user akan di minta memasukkan data yang di butuhkan
6. memproses data yang di masukkan user 
7. menampilkan hasil
8. selesai

'''
start = True
while start:
    print("Menu\n1. Menghitung Luas Segitiga\n2. Luas Lingkaran\n3. Luas Menentukan Ganjil Genap\n4. Exit")
    pilih = int(input("Pilih Opsi => "))
    if pilih == 1:
        a = float(input("Masukkan Alas => "))
        t = float(input("Masukkan Tinggi => "))
        hasil = 1/2 *a*t
        print("Alas =",a,"tinggi =",t,"Hasilnya =",hasil)

    if pilih == 2:
        r = float(input("Masukkan Jari-Jari\n==> "))
        if r % 7 == 0:
            hasil = 22/7*r*r
            print(hasil)
        else:
            hasil = 3.14*r*r
            print(hasil)
    if pilih == 3:
        x = int(input("Masukkan Angka\n==> "))
        if x%2==0:
            print("Bilangan Genap")
        else:
            print("Bilangan Ganjil")
            
    if pilih == 4:
        break
    
    else:
        print("Invalid Kode")