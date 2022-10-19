a = int(input("Masukkan Angka => "))
if a > 1:
    kunci = 0
    for i in range(1,a+1):
        if a%i==0:
            kunci += 1
    if kunci == 2:
        print(a,"Bilangan Prima")
    else:
        print(a,"Bukan Bilangan Prima")
            
else:
    print(a,"Bukan Bilangan Prima")