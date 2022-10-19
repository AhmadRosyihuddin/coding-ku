x = int(input("Masukkan Angka : "))
jumlah = 0
angka = 2
while jumlah < x:
    faktor = 0
    for i in range(1,angka+1):
        if angka % i == 0:
            faktor += 1
    if faktor == 2:
        print(angka,end=' ')
        jumlah += 1
    angka += 1

# def faktor(a,b): 
#     if b == 1:
#         c = 1
#     else:
#         c = faktor(a,b-1) + bagi(a,b)
#     return c

# def cekPrima(x):
#     if faktor(x,x) == 2:
#         c = x
#     #else:
#     #    c = faktor(x,x) + cekPrima(x-1)
#     return c
    
# def bagi(a,b):
#     if a % b ==0:
#         return 1
#     else:
#         return 0

# def deretPrima(a): #5
#     if a-(a-1) > a:
#         return a
#     else:
#         x = cekPrima(a)
#         print(x)
#         return deretPrima(2+1)
    
        
        
# x = int(input("Masukkan Angka : "))
# deretPrima(x)

