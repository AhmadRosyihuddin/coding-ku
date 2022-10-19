def matric1():
    matric = []
    for i in range(2):
        tamp = []
        for y in range(2):
            a = int(input('['+str(i)+']'+'['+str(y)+']'+' = '))
            tamp.append(a)
        matric.append(tamp)
    return matric
print(matric1())