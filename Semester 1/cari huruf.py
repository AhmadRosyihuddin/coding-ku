huruf =[]
temp = 0
a = str(input("masukkan Kata => ")).lower()
x = str(input("masukkan huruf yang di cari => "))
for i in a:
    huruf.append(i) 
    if x in i:
        temp += 1
        print("Huruf",x,"Atau Huruf",x.upper(),"Ke-",temp,":","offset- ",len(huruf)-1)