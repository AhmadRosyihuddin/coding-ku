def createlist(x):
    data = []
    for i in range(x):
        print('Masukkan Bilangan ke-',i,': ',end='')
        a = int(input())
        data.append(a)
    return data

def isGenap(data):
    genap = []
    ganjil = []
    for i in data:
        if i % 2 == 0 and i not in genap:
            genap.append(i)
        elif i % 2 != 0 and i not in ganjil:
                ganjil.append(i)
    if data == genap:
        return genap
    else:
        return ganjil
    

def isprime(data):
    prime = []
    p = 0
    for i in data:
        for y in range(1,i+1):
            if i % y == 0:
                p += 1
        if p == 2 and i not in prime:
            prime.append(i)
        p =0
    return prime

data = createlist(5)
print('Bilangan =',data)
genap = isGenap(data)
ganjil =isGenap(data)
print(ganjil)
print(genap)
prima = isprime(data)
print('Prima =',prima)


# def pembagi(x):
#     pembagi = []
#     for i in range(1,x+1):
#         if x % i == 0:
#             pembagi.append(i)
#     return pembagi

# x = int(input('Masukkan Angka : '))
# pembagi = pembagi(x)
# print('Bilangan Pembagi =',pembagi)