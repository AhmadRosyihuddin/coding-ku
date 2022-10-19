print("Toko Swalayan \"maju Mundur\"\nMau beli apa?\nbaju/celana/sepatu?")
inp = str(input("Masukkan Pilihan => ")).lower()

if inp == 'baju':
    baju = 100000
    kartu = str(input("Apakah Anda memliki kartu member (y/t) => ")).lower()
    if kartu == 'y':
        dis = baju*20/100
        harga = baju - dis
        print("Harga Baju =",harga)
    else:
        print("Harga Baju =",baju)
        
elif inp == 'celana':
    celana = 150000
    kartu = str(input("Apakah Anda memliki kartu member (y/t) => ")).lower()
    if kartu == 'y':
        dis = celana*20/100
        harga = celana - dis
        print("Harga Celana =",harga)
    else:
        print("Harga Celana =",celana)
        
elif inp == 'sepatu':
    sepatu = 250000
    kartu = str(input("Apakah Anda memliki kartu member (y/t) => ")).lower()
    if kartu == 'y':
        dis = sepatu*20/100
        harga = sepatu - dis
        print("Harga Celana =",harga)
    else:
        print("Harga Celana =",sepatu)
    
else:
    print("Barang Tidak Ada ")