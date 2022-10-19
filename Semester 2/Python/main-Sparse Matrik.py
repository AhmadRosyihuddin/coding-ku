import SparseMatrik as pk

a = int(input('Masukkan Baris => '))
b = int(input('Masukkan Kolom => '))


data1 = pk.createSparseMatrix(a,b)
print(data1)
print(pk.displaySparseMatrix(data1))


a1 = int(input('Masukkan Baris => '))
b1 = int(input('Masukkan Kolom => '))
data2 = pk.createSparseMatrix(a1,b1)
print(data2)
print(pk.displaySparseMatrix(data2))

print("Matrik 1")
print(pk.displaySparseMatrix(data1))
print("Matrik 2")
print(pk.displaySparseMatrix(data2))

hasil = pk.multSparseMatrix(data1,data2)
if hasil==False:
  print("ukuran tidak sama")
else:
  print("Hasil Perkalian Matrik 1 dan Matrik 2")
  print(pk.displaySparseMatrix(hasil))