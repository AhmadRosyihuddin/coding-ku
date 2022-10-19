start = True
start1 = True
start2 = True
while start:
    jam = int(input("Kegiatan Di Mulai (Jam 0-23) => "))
    if jam >= 0 and jam <= 23:
        start = False
    else:
        print("Masukkan Dengan Benar")
while start1:
    menit = int(input("Kegiatan Di Mulai (Menit 0-59) => "))
    if menit >= 0 and menit <= 59:
        start1 = False
    else:
        print("Masukkan Dengan Benar")

while start2:
    durasi = int(input("Durasi Kegiatan (Menit) => "))
    if durasi >= 0:
        start2 = False
    else:
        print("Salah Goblok")

print("="*40)
print("Kegiatan Di Mulai Pukul = ",jam,":",menit,"\nDurasi kegiata = ",durasi,"Menit")
menit_akhir = menit + durasi
if menit_akhir >= 60:
    menit = menit_akhir - 60
    jam += 1
    while  menit >= 60:
        menit = menit - 60
        jam += 1
        
    if jam >= 24:
        jam = jam - 24
        
print("Kegiatan Berakhir pukul =",jam,":",menit)
print("="*40)