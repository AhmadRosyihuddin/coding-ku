temp = 0
nilai = 0
d = int(input("Masukkan Angka => "))
a = int(input("Masukkan Angka => "))
for i in range(2,d+1 and a+1):
    if a % i == 0 and d % i == 0:
        temp += 1
        nilai = i
        print("Pembagi yang sama -",temp,"=",i)
print("Pembagi Yang Sama Yang Terbesar",nilai)