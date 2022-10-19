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
def square(matric):
    return len(matric) == len(matric[0])

def jumlah(matric):
    temp = []
    if len(matric) == len(matric[0]):
        for i in range(len(matric)):
            for j in range(len(matric[0])):
                if i == 0 and j == len(matric[0])-2:
                    temp.append(matric[i][j]+matric[i][j+1])
                elif i == len(matric)-1 and j == 1:
                    temp.append(matric[i][j-1]+matric[i][j])
    return temp


x = createMat2D(3,3)
print('Matrik =',disMat2D(x),sep='\n')
print('Berbentuk Bujursangkar? =',square(x))
print(jumlah(x))




def deret(data):
    if len(data) == 1:
        return data[0]
    else:
        return data[0] + deret(data[1:])

hasil = deret([1,3,5,7,9])
print(hasil)


