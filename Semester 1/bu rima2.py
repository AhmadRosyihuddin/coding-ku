def createMat2D(x,y):
    matrik = []
    for baris in range(x):
        tamp = []
        for kolom in range(y):
            tamp.append(int(input('Matrik '+ '['+str(baris)+']'+'['+str(kolom)+'] = ')))
        matrik.append(tamp)
    return matrik

def disMat2D(mat1,string):
    if mat1 == 0:
        print('Ukuran Matrik Tidak Sama')
    else:
        print(string)
        for i in range(len(mat1)):
            print('|  ',end='')
            for y in range(len(mat1[0])):
                print(mat1[i][y],end='  ')
            print('|')

def addMat(matrik1,matrik2):
    jumlah = []
    if len(matrik1) == len(matrik2):
        for i in range(len(matrik1)):
            tamp = []
            for y in range(len(matrik2[0])):
                tamp.append(matrik1[i][y]+matrik2[i][y])
            jumlah.append(tamp)
        return jumlah
    else:
        return 0
    

print('Create Mat 1')
matrik1 = createMat2D(2,3)
print('Create Mat 2')
matrik2 = createMat2D(2,2)
print('Create Mat 3')
matrik3 = createMat2D(3,2)
hasil = addMat(matrik1,matrik2)
hasil1 = addMat(matrik1,matrik3)
hasil2 = addMat(matrik2,matrik3)
disMat2D(matrik1,'Matrik1 =')
disMat2D(matrik2,'Matrik2 =')
disMat2D(matrik3,'Matrik3 =')
disMat2D(hasil,'Matrik 1 + Matrik 2 =')
disMat2D(hasil1,'Matrik 1 + Matrik 3 =')
disMat2D(hasil2,'Matrik 2 + Matrik 3 =')