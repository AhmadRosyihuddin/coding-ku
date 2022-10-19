total = 0
urut = 0
x = int(input("Jumlah Angka Bilangan Ganjil => "))
for i in range(x*2):
    if i % 2 == 1:
        total += i   
        urut += 1
        print("Bilangan Ganjil Ke-",urut,":",i)
print("Total Angka Yang Di temukan =",total)
