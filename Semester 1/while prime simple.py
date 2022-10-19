x = int(input("Masukkan Angka => "))
if x > 1:
    i = 3
    while i < x:
        if x % i == 0:
            print("Bukan Prima")
            break
        i += 1
    else:
        print("Prima")
else:
    print("Bukan Prima")