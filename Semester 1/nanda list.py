nama = []
nilai = []
print('Pendataan Mahasiswa')
jml = int(input("Jumlah Mahasiswa => "))
for i in range(1,jml+1):
    print("Mahasiswa ke-",i)
    inp_nama = str(input('nama mahasiswa => ')).title()
    inp_nilai = int(input("Nilai Mahasiswa => "))
    nama.append(inp_nama)
    nilai.append(inp_nilai)
while True:
    print("\nDaftar Nilai Mahasiswa\nTekan 0 untuk Daftar Mahasiswa Dan NIlai\nTekan 1 untuk Nilai Rata - Rata Mahasiswa\nTekan 2 Untuk Daftar Mahasiswa Yang Melebihi Threshold\nTekan 3 Untuk Nilai Maksimal\nTekan 4 Exit")
    opsi = int(input("Pilih Opsi \n=> "))
    if opsi == 0:
        name = len(nama)
        for i in range(name):
            print(i+1,".",nama[i],'\t=',nilai[i])

    elif opsi == 1:
        total = 0
        score = len(nilai)
        for i in nilai:
            total += i
        print('Nilai Rata - Rata Mahasiswa :',total/score)

    elif opsi == 2:
        inp = int(input("Masukkan Nilai Threshold => "))
        for i in range(jml):
            if nilai[i] > inp:
                print(i+1,'.',nama[i],":",nilai[i])
    
    elif opsi == 3:
        print("Nilai Maksimal Dari Semua Mahasiswa :",max(nilai))
        
    else:
        print("Terimakasih Telah Mengakses Sistem Kami.. :)")
        break
    
    x = str(input("Lagi? (Y/T) => ")).lower()
    if x == 'y':
        continue
    else:
        break