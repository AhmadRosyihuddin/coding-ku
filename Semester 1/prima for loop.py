a = int(input("Masukkan Angka => "))
if a > 1:
    for i in range(2,a):
        if a%i==0:
            print("Bukan Bilangan Prima")
            break
    print("Bilangan Prima")
            
else:
    print("Bukan Bilangan Prima")