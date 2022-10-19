#menampilkan deret aritmatika
sn = 0
a = int(input('Masukkan Suku Pertama: '))
b = int(input('Masukkan Beda: '))
n = int(input('Masukkan Jumlah Suku: '))
for i in range (n) :
    n= i + 1
    un= a+(n-1)*b
    print(un,end=',')
    sn = un + sn
print(' ')
print('Jumlah deret aritmatika anda adalah : ',sn)