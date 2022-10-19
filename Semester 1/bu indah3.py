def createMat2D(x,y):
    matrik = []
    for baris in range(1,x+1):
        tamp = []
        for kolom in range(1,y+1):
            tamp.append(int(input('Matrik '+ '['+str(baris)+']'+'['+str(kolom)+'] = ')))
        matrik.append(tamp)
    return matrik

def disMat2D(mat1):
    x = ''
    if mat1 == 0:
        return 'MATRIK TIDAK SAMA'
    else:
        for i in range(len(mat1)):
            x += '|'.ljust(5)
            for y in range(len(mat1[0])):
                x += str(mat1[i][y]).ljust(5)
            x += '|'+'\n'
    return x

def addMat(matrik1,matrik2):
    if len(matrik1) == len(matrik2) and len(matrik1[0]) == len(matrik2[0]):
        jumlah = []
        for i in range(len(matrik1)):
            tamp = []
            for y in range(len(matrik2[0])):
                tamp.append(matrik1[i][y]+matrik2[i][y])
            jumlah.append(tamp)
        return jumlah
    else:
        return 0


def square(matric):
    return len(matric) == len(matric[0])

def perkalian(matric1,matric2):
    if len(matrik1) == len(matrik2) and len(matrik1[0]) == len(matrik2[0]):
        jumlah = []
        for i in range(len(matrik1)):
            tamp = []
            for y in range(len(matrik2[0])):
                tamp.append(matrik1[i][y]*matrik2[i][y])
            jumlah.append(tamp)
        return jumlah
    else:
        return 0
    
def maks(matric,argumen):
    maks = []
    if argumen == 'baris':
        for i in range(len(matric)):
            x = 0
            tamp = []
            for y in range(len(matric[0])):
                if x > matric[i][y]:
                    x = x
                else:
                    x = matric[i][y]
            tamp.append(x)
            maks.append(tamp)
        return maks
    
    elif argumen == 'kolom':
        maks = []
        tamp = []
        for i in range(len(matric[0])):
            x = 0
            for y in range(len(matric)):
                if x > matric[y][i]:
                    x = x
                else:
                    x = matric[y][i]
            tamp.append(x)
        maks.append(tamp)
        return maks
    
    elif argumen == '*':
        maks = 0
        for i in range(len(matric)):
            for y in range(len(matric[0])):
                if maks > matric[i][y]:
                    maks = maks
                else:
                    maks = matric[i][y]
        return maks

print('Matrik 1')
matrik1 = createMat2D(2,2)
print('Matrik 2')
matrik2 = createMat2D(2,2)

print('Matrik 1 :',disMat2D(matrik1),sep='\n')
print('Is Square?',square(matrik1),'\n')

print('Matrik 2',disMat2D(matrik2),sep='\n')
print('Is Square?',square(matrik2),'\n')

tambah = addMat(matrik1,matrik2)
kali = perkalian(matrik1,matrik2)
maksimal = maks(matrik2,'baris')
maksimal1 = maks(matrik2,'kolom')
maksimal2 = maks(matrik2,'*')

print('Hasil Penjumlahan :',disMat2D(tambah),sep='\n')
print('Hasil Perkalian :',disMat2D(kali),sep='\n')
print('Maksimum - Baris :',disMat2D(maksimal),sep='\n')
print('Maksimum - Kolom :',disMat2D(maksimal1),sep='\n')
print('Maksimum :',maksimal2)