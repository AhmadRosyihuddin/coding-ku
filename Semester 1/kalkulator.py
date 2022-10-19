def tambah(x,y):
    return x + y
def kurang(x,y):
    return x - y
def bagi(x,y):
    return x / y
def kali(x,y):
    return x * y

print('Keterangan:\n1. ( + ) Penjumlahan\n2. ( - ) Pengurangan\n3. ( * ) Perkalian\n4. ( : ) Pembagian\nNB : Tambahkan spasi saat input contoh 2 + 1')
i = 0
start = True
while start:
    num = input('input data => ').split()
    while '*' in num or ':' in num:
            if num[i] == '*':
                x = kali(float(num[i-1]),float(num[i+1]))
                del(num[i-1:i+2])
                num.insert(i-1,x)
                i = 0

            elif num[i] == ':':
                x = bagi(float(num[i-1]),float(num[i+1]))
                del(num[i-1:i+2])
                num.insert(i-1,x)
                i = 0
            i += 1
            

    while '+' in num or '-' in num:
            if num[i] == '+':
                x = tambah(float(num[i-1]),float(num[i+1]))
                del(num[i-1:i+2])
                num.insert(i-1,x)
                i = 0

            elif num[i] == '-':
                x = kurang(float(num[i-1]),float(num[i+1]))
                del(num[i-1:i+2])
                num.insert(i-1,x)
                i = 0
            i += 1
            
    print('Hasil =',num[0])
    a = int(input('1. ULANG\n2. SELESAI\n=> '))
    if a == 1:
        num.clear()
    elif a == 2:
        start = False

