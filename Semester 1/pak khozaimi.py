# Soal 1
# def tabung(r,t):
#     if r % 7 == 0:
#         volume = (22/7)*r**2*t
#     else:
#         volume = 3.14*r**2*t
#     return volume

# r = int(input('Masukkan Jari - Jari : '))
# t = int(input('Masukkan Tinggi Tabung : '))
# print('Volume Tabung :',tabung(r,t))
       


#Soal 2 
sisi1 = int(input('Masukkan sisi 1 : '))
sisi2 = int(input('Masukkan sisi 2 : '))
sisi3 = int(input('Masukkan sisi 3 : '))


if sisi1 > sisi2 and sisi1 > sisi3:
    a,b,c = sisi1,sisi2,sisi3
elif sisi2 > sisi1 and sisi2 > sisi3:
    a,b,c = sisi2,sisi1,sisi3
else:
    a,b,c = sisi3,sisi2,sisi1

if a < (b+c):
    if b==c:
        print('Segitiga Sama Kaki')
    else:
        if a**2 == b**2 + c**2:
            print('Segitiga Siku Siku')
        else:
            print('Segitiga Sembarang')
else:
    print('Tidak Bisa Jadi Segitiga')
    