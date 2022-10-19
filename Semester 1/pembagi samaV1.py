b = []
c = []
temp = 0
mak = 0
d = int(input("Masukkan Angka => "))
a = int(input("Masukkan Angka => "))
for i in range(2,a+1):
    if a % i == 0:
        b.append(i)

for i in range(2,d+1):
    if d % i == 0:
        c.append(i)

for i in c:
    if i in b:
        temp += 1
        mak = i
        print("Pembagi yang sama -",temp,"=",i)
print("Nilai terbesar Yang Sama =",mak)
