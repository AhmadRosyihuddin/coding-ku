# Sigma
# def CreateList(n):
#     data = []
#     for i in range(n):
#       data.append(int(input('Masukkan Data List => ')))
#     return data

# def sigmaY(data):
#     hasil = 0
#     n = len(data)
#     for i in range(n):
#       hasil += data[i]
#     hasil *= 1/n
#     return hasil

# def sigmaZ(data):
#     hasil = 0
#     n = len(data)
#     for i in range(n):
#       hasil += (data[i]-sigmaY(data))**2
#     hasil *= 1/(n-1)
#     return hasil

# x = CreateList(7)
# print('Data =',x)
# print('Y =',sigmaY(x))
# print('Z =',sigmaZ(x))

# Matrik 1D
# def matriks1D(a):
#     data = []
#     for i in range(a):
#       data.append(int(input('Data Matrik => ')))
#     return data

# def penjumlahan(a,b):
#     if len(a)==len(b):
#         jumlah = []
#         for i in range(len(a)):
#             jumlah.append(a[i] + b[i])
#         return jumlah
#     else:
#         return 'Ukuran Matrik Tidak Sama'

# def perkalian(a,b):
#     if len(a)==len(b):
#         jumlah = []
#         for i in range(len(a)):
#             jumlah.append(a[i] * b[i])
#         return jumlah
#     else:
#         return 'Ukuran  Matrik Tidak Sama'

# def perkalianSaklar(a,matrik):
#     hasil = []
#     for i in range(len(matrik)):
#         hasil.append(a*matrik[i])
#     return hasil

# matrik1 = matriks1D(4)
# matrik2 = matriks1D(3)
# matrik3 = matriks1D(4)
# print('Matrik 1 =',matrik1)
# print('Matrik 2 =',matrik2)
# print('Matrik 3 =',matrik3)

# tambah1 = penjumlahan(matrik1,matrik2)
# print('Hasil Penjumlahan =',tambah1)

# print('Matrik 1 =',matrik1)
# print('Matrik 3 =',matrik3)
# tambah = penjumlahan(matrik1,matrik3)
# print('Hasil Penjumlahan =',tambah)

# saklar = perkalianSaklar(3,tambah)
# print('Perkalian Saklar =',saklar)

# kali = perkalian(matrik1,matrik3)
# print('Perkalian =',kali)


# Matrik 2D
def matriks2D(a,b):
    data = []
    for i in range(a):
        temp = []
        for y in range(b):
            temp.append(int(input('mat['+str(i)+','+str(y)+'] = ')))
        data.append(temp)
    return data

def penjumlahan2D(matrik1,matrik2):
    if len(matrik1) == len(matrik2) and len(matrik1[0]) == len(matrik2[0]):
        jumlah = []
        for i in range(len(matrik1)):
            tamp = []
            for y in range(len(matrik2[0])):
                tamp.append(matrik1[i][y]+matrik2[i][y])
            jumlah.append(tamp)
        return jumlah
    else:
        return 'Ukuran Matrik Tidak Sama'

def perkalian2D(matrik1,matrik2):
    if len(matrik1) == len(matrik2) and len(matrik1[0]) == len(matrik2[0]):
        jumlah = []
        for i in range(len(matrik1)):
            tamp = []
            for y in range(len(matrik2[0])):
                tamp.append(matrik1[i][y]*matrik2[i][y])
            jumlah.append(tamp)
        return jumlah
    else:
        return 'Ukuran Matrik Tidak Sama'

matrik1 = matriks2D(3,2)
matrik2 = matriks2D(3,2)
matrik3 = matriks2D(2,2)
print('mat1 =',matrik1)
print('mat2 =',matrik2)
print('mat3 =',matrik3)

tambah = penjumlahan2D(matrik1,matrik2)
tambah1 = penjumlahan2D(matrik1,matrik3)
print('mat1 + mat2 =',tambah)
print('mat1 + mat3 =', tambah1)

kali = perkalian2D(matrik1,matrik2)
kali1 = perkalian2D(matrik1,matrik3)
print('mat1 * mat2 =',kali)
print('mat1 * mat3 =',kali1)