b =[]
a = int(input("Masukkan Angka => "))
for i in range(1,a+1):
    if a % i == 0:
        b.append(i)
print("Faktor Pembagi Dari",a,b)