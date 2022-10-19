total = 0
a = int(input("Masukkan Suku pertama => "))
b = int(input("Masukkan Beda => "))
sn = int(input("Masukkan Total => "))
for i in range(1,sn):
    n = i
    un = a + (n-1)*b
    total = (n/2)*(a+un)
    if total <= sn:
        print("U Ke-",i,"=",un,"Total =",total)
        