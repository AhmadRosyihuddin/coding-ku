n1 = int(input("Masukkan Suku Yang Di Ketahui => "))
n2 = int(input("Masukkan Suku Yang Di Ketahui => "))
besar1 = int(input("Masukkan Besar nilai Suku Yang Di Ketahui => "))
besar2 = int(input("Masukkan Besar Nilai Suku Yang Di Ketahui => "))
elim = (n1-1) - (n2-1) 
b = besar1 - besar2
c = b/elim
print("Nilai b =",c)
rumus = (n1-1)*c
n = besar1 - rumus
print("Nilai a =",n)


# Un = a + (n-1)*b
# U3 = a + 2b = 9
# U7 = a + 6b = 17
#         -4b = -8
#           b = -8/-4 = 2

# a + 2b   = 9
# a + 2(2) = 9
# a + 4 = 9
# a = 9 - 4
# a = 5