# variabel penampung untuk menampung data yang di inputkan user
database=[
    [200411100100,'HASAN','GRESIK','ALPRO C'],
    [200411100053,'JAMET','SURABAYA','ALPRO D'],
    [200411100026,'ARI','SAMPANG','ALPRO E'],
    [200411100132,'ANDI','BANGKALAN','ALPRO C'],
    [200411100166,'YOGA','PAMEKASAN','ALPRO A'],
    [200411100166,'YOGA','PAMEKASAN','ALPRO A']
]
# fungsi tabel untuk membuat sebuah tabel dari database
def tabelData(database):
    # Header tabel
    print('+'+'-'*74+'+')
    print('|'.ljust(0),'Database Mahasiswa'.center(72),'|'.rjust(0))
    print('+'+'-'*74+'+')
    print('|'+'NO'.center(6)+'|'+'NIM'.center(16)+'|'+'Nama'.center(16)+'|'+'Alamat'.center(16)+'|'+'Kelas'.center(16)+'|')
    print('+'+'-'*74+'+')
    # pengecekan apakah variabel database itu memiliki data
    if len(database)==0:
        print('|'.ljust(0),'TIDAK ADA DATA'.center(72),'|'.rjust(0))
        print('+'+'-'*74+'+')
    else:
        # jika ada maka akan di lakukan penampilan data dari data base dengan membuat seperti tabel
        for i in range(len(database)):
            print('|'+str(i+1).center(6)+'|',end='')

            for y in range(4): # proses peloopingan untuk memanggil data dari database menggunakan index y dan i
                panjang = len(str(database[i][y]))
                print(database[i][y],end=''.center(16-panjang)+'|')
            print()
        print('+'+'-'*74+'+')

# fungsi hapus data untuk menghapus sebuah data dari database
def hapusData():
        x = int(input('Masukkan Nomor Data Yang Mau Di hapus : '))
        # inputan user akan di cek apakah ada di database
        if x-1 >= len(database): #jika inputan user melebihi len/ panjang databse maka data tidak di temukan
            print()
            print('<< DATA TIDAK DI TEMUKAN >>'.center(74))
        else:
            del(database[x-1])
            print()
            print('<< DATA BERHASIL DI HAPUS >>'.center(74))

# fungsi tambah data untuk menambah sebuah data
def tambahData():
    x = int(input('Masukkan Jumlah Mahasiswa : '))
    # Proses peloopingan sesuai jumlah yang di inputkan user
    for i in range(x):
        nim = int(input('Masukkan NIM Mahasiswa : '))
        nama = input('Masukkan Nama Mahasiswa : ').upper()
        alamat = input('Masukkan Asal Mahasiswa : ').upper()
        kelas = input('Masukkan Kelas Mahasiswa : ').upper()
        database.append([nim,nama,alamat,kelas]) # data akan di tambahkan ke database 
        print()
    print('<< DATA BERHASIL DI TAMBAHKAN >>'.center(74))

# Fungsi edit data untuk mengedit data yang ada di database
def editData(x):
    edit=[]
    del(database[x-1])
    nim = int(input('Masukkan NIM Mahasiswa : '))
    nama = input('Masukkan Nama Mahasiswa : ').upper()
    alamat = input('Masukkan Asal Mahasiswa : ').upper()
    kelas = input('Masukkan Kelas Mahasiswa : ').upper()
    edit.append(nim)
    edit.append(nama)
    edit.append(alamat)
    edit.append(kelas)
    database.insert(x-1,edit)
    print()

def cari(x):
    print('+'+'-'*74+'+')
    print('|'.ljust(0),'Database Mahasiswa'.center(72),'|'.rjust(0))
    print('+'+'-'*74+'+')
    print('|'+'NO'.center(6)+'|'+'NIM'.center(16)+'|'+'Nama'.center(16)+'|'+'Alamat'.center(16)+'|'+'Kelas'.center(16)+'|')
    print('+'+'-'*74+'+')
    tamp = []
    nomor = 0
    for i in range(len(database)):
        for y in range(4):
            if str(database[i][y]) == x:
                tamp.append(i)
    if len(tamp) != 0:
        for n in tamp:
            nomor += 1
            print('|'+str(nomor).center(6)+'|',end='')
            for j in range(4):
                panjang = len(str(database[n][j]))
                print(database[n][j],end=''.center(16-panjang)+'|')
            print()
        print('+'+'-'*74+'+')
    else:
        print('|'.ljust(0),'DATA TIDAK DI TEMUKAN'.center(72),'|'.rjust(0))
        print('+'+'-'*74+'+')
                
            
def sorting():
    n = len(database)
    for i in range(n):
        for y in range(n-1):
            if database[y] > database[y+1]:
                database[y],database[y+1] = database[y+1],database[y]
        n -= 1
        

start = True
while start:
    print('Menu:\n1. Tampilkan Data (Tekan 1)\n2. Tambah Data (Tekan 2)\n3. Hapus Data (Tekan 3)\n4. Edit Data (Tekan 4)\n5. Cari Data (Tekan 5)\n6. Urutkan data (Tekan 6)\n7. Exit (Tekan 7)')
    print('+'+'-'*74+'+')
    pilih = int(input('Pilih Opsi : '))
    if pilih == 1:
        print()
        tabelData(database)
    elif pilih == 2:
        tambahData()
        tabelData(database)
    elif pilih == 3:
        hapusData()
        tabelData(database)
    elif pilih == 4:
        x = int(input('Masukkan Nomor Data Yang Mau Di Edit : '))
        if x-1 >= len(database):
            print()
            print('<< DATA TIDAK DI TEMUKAN >>'.center(74))
            tabelData(database)
        else:
            editData(x)
            print('<< DATA BERHASIL DI EDIT >>'.center(74))
            tabelData(database)
    elif pilih == 5:
        x = input('Masukkan Data Yang Mau Di Cari : ').upper()
        cari(x)
    elif pilih == 6:
        sorting()
        tabelData(database)
    elif pilih == 7:
        print('Terimaksih Telah Mengakses Sistem kami :)\n'+'+'+'-'*61+'+')
        start = False
    else:
        print('MAAF PILIHAN ANDA TIDAK ADA\n'+'+'+'-'*74+'+')
