

def penjumlahan(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + penjumlahan(x[1:])

data2 = [1,1,1,1]   
hasil = penjumlahan(data2)
print(data2,hasil)