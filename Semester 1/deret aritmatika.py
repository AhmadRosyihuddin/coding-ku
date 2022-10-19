#(n) : menunjukkan suku ke berapa
#(a) : suku pertama
#(b) : lompatan tiap suku

a = int(input("Masukkan Angka (Suku Pertama) => "))
b = int(input("Masukkan Angka (Beda) => "))
n = int(input("Masukkan Angka (Suku Ke n) => "))

c = 0
for i in range(1,n+1):
    n=i
    un = a +(n - 1)*b
    print("U-",i,"=",un)
    c += 1
print("Total : ",c)
sn = (n/2)*(a+un)
print("sn :",sn)

#algoritma deret aritmatika
# 1. Masukan Suku Pertama
# 2. Masukkan Beda 
# 3. Masukkan Suku Ke n
# 4. Buat Var Penampung
# 5. looping angka dari 1 sampai angka yang di inginkan user
# 6. samakan nilai var i dengan var n
# 7. masukan rumus ke var
# 8. cetak setiap urutan suku dan nilai nya
# 9. tambahkan var penampung dengan angka 1
# 10. cetak total semua angka yang di temukan 
# 11. masukkan rumus untuk mencari jumlah semua suku yang di temukan
# 12. cetak var dari rumus