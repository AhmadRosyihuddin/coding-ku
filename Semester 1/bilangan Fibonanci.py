a = 1
b = 1
c = 0
x = int(input("masukkan Angka :" ))
for i in range(x):
    print(a,'',end='')
    c = a+b
    a = b
    b = c

#0 1 1 2
#a b c
#  a b c
#    a b c