# # Soal 1
# x = int(input("Masukkan Usia : "))
# if x > 50:
#     print("Tua")
# elif x > 25:
#     print("Dewasa")
# elif x > 17:
#     print("Muda")
# else:
#     print("Anak - Anak")



#soal 2
# nama = str(input("Masukkan Nama : "))
# nim = str(input("Masukkan NIM : "))
# uts = int(input("Masukkan Nilai UTS : ")) 
# uas = int(input("Masukkan NIlai UAS : "))
# print('Nama : ',nama,'\nNIM Anda : ',nim)
# nilai = (uts + uas)/2
# print('Nilai rata rata Anda :',nilai)
# if nilai > 80 and nilai <=100:
#     print('Anda Mendapatkan Nilai A')
# elif nilai > 70:
#     print('Anda Mendapatkan Nilai B')
# elif nilai > 60:
#     print('Anda Mendapatkan Nilai C')
# elif nilai > 40:
#     print('Anda Mendapatkan Nilai D')
# elif nilai >= 0 and nilai <= 40:
#     print('Anda Mendapatkan Nilai E')
    
#Soal 3
skor_jaka = 1100
ipk_jaka = 3.5
skor_ida = 1000
ipk_ida = 3.5
if skor_jaka > 1100 and ipk_jaka >= 3.0:
    print('Jaka Lulus')
else:
    print('Jaka TIDAK LULUS')

if skor_ida > 1100 and ipk_ida >= 3.0:
    print('Ida LULUS')
else:
    print('Ida TIDAK LULUS')