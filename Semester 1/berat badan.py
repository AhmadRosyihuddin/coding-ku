

def ke2():
     t = float(input("Masukkan tinggi badan => "))
     b = int(input("Masukkan Berat Badan => "))
     a = (t*t)
     c = (b/a)
     print("Hasil Perhitungan =>",c)
     print("="*30)
     
     if c <= 18.5:
         print(c,"= Masuk Kategori Kelebihan Berat Badan")
     elif c >= 18.5 and c <= 24.9:
         print(c,"= Masuk Kategori Ideal")
     elif c >= 25 and c<= 29.9:
         print(c,"= Masuk Kategori Kelebihan Berat Badan")
     elif c >= 30:
         print(c,"= Masuk Kategori Obesitas")   
         
def ke3():
    print("Terimakasih Telah menggunakan Layanan kami")
    
start = True
while start:
    print("\n============================\nMenghitung Berat Badan Ideal\nPilih Metode\n1. Rumus Broca\n2. BMI (Body Massa Index)\n3. Exit\n==============================")
    user = int(input("Pilih Opsi => "))
    
    if user == 1:
        print("1. Laki-Laki\n2. Permpuan")
        pilih = int(input("Pilih Opsi => "))
        
        if pilih == 1:
            tinggi = float(input("Masukkan Tinggi badan => "))
            print("Berat Badan Ideal Kamu Adalah =>",(tinggi-100)-(tinggi-100)*10/100)
        
        if pilih == 2:
            tinggi = float(input("Masukkan Tinggi badan => "))
            print("Berat Badan Ideal Kamu Adalah =>",(tinggi-100)-(tinggi-100)*15/100)
    elif user == 2:  
        ke2()
    elif user == 3:
        ke3()
        break
    else:
        print("Masukkan Dengan Benar")