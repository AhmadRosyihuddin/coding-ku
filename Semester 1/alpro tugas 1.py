#Tugas 1
guntur = 3
icha = 5
ratna = 6
print("guntur =",guntur,",","Icha =",icha,",","ratna =",ratna)

totalapel = (guntur+icha+ratna)
print("Total Apel =",totalapel)
a = 7
b = 11
c = 15
hasil = ((a*b)+c)
print("(",a,"*",b,")","+",c,"=",hasil)

#Tugas 2
clue = 1.61
print("="*40)
mill = float(input("Masukkan angka (MILL) => "))
hasil = (mill * clue)
print(mill,"MILL =",hasil,"KM")
print("="*40)
km = float(input("Masukkan Angka (KM) => "))
hasil = (km / clue)
print(km,"KM =",hasil,"MILL")

#Tugas 3
while True:
    jam = int(input("Waktu Mulai Kegiatan (Jam 0-23) => "))
    if jam >= 0 and jam <= 23:
        break
    else:
        print("Masukkan Dengan Benar")
        
while True:
    menit = int(input("Waktu Mulai Kegiatan (menit 0-59) => "))
    if menit >= 0 and menit <= 59:
           break
    else:
        print("Masukkan Dengan Benar")
        
while True:
    durasi = int(input("Durasi Kegiatan (Menit) => "))
    if durasi >= 0:
        break
    else:
        print("Masukkan Dengan Benar")
print("="*40)
print("Mulai Kegiatan Pukul =",jam,":",menit,"\nDurasi Kegiatan Pukul =",durasi)
total = menit + durasi
if total >= 60:
    menit = total - 60
    jam += 1
    while menit >= 60:
        menit = menit - 60
        jam += 1
    if jam >= 24:
        jam = jam - 24
    print("Kegiatan Berakhir Pukul =",jam,":",menit)
    print("="*40)
else:
    print("Kegiatan Berakhir Pukul =",jam,":",total)
    print("="*40)