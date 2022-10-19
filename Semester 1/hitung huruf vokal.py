a = 0
i = 0
e = 0
u = 0
o = 0
x = str(input("masukkan kata => "))
n = x.lower()
for t in n:
    if t == "a":
        a += 1
    elif t == "i":
        i += 1
    elif t == "e":
        e += 1
    elif t == "u":
        u += 1
    elif t == "o":
        o += 1
print("Jumlah Huruf Vokal a = ",a)
print("Jumlah Huruf Vokal i = ",i)
print("Jumlah Huruf Vokal u = ",u)
print("Jumlah Huruf Vokal e = ",e)
print("Jumlah Huruf Vokal o = ",o)