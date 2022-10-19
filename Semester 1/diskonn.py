p1 = 0
p2 = 0
p3 = 0
print("="*40)
print("| NO |  Daftar Produk     |   Diskon   |\n| 1. | Sabun   = Rp. 3000 | Diskon 20% |\n| 2. | piring  = Rp. 5000 | Diskon 40% |\n| 3. | cangkir = Rp. 8000 | Diskon 45% |")
print("="*40)
print("SEALAMAT DATANG DI PYTHON MARKET\nSelamat Berbelanja:)")
print("="*40)
while True:
    pilih = int(input("Silahkan Pilih Produk Yang Mau Anda Beli\n==> "))
    if pilih == 1:
            b1 = int(input("Jumlah Pembelian\n==> "))
            sabun = 3000
            diskon = sabun*20/100
            hasil = sabun-diskon
            pilih1 = 'Sabun'
            jumlah1 = b1
            if b1 >= 0:
                p1 = b1*hasil
                print("Ada Tambahan ? (Y : 1 / T : 2)")
                aa = int(input("==> "))
                if aa == 1:
                    continue
                elif aa == 2:
                    print("Terimakasih Telah Berbelanja")
                    break
                
                
    elif pilih == 2:
            b2 = int(input("Jumlah Pembelian\n==> "))
            piring = 5000
            diskon = piring*40/100
            hasil = piring-diskon
            pilih2 = 'Piring'
            jumlah2 = b2
            if b2 >= 0:
                p2 = b2*hasil
                print("Ada Tambahan ? (Y : 1 / T : 2)")
                aa = int(input("==> "))
                if aa == 1:
                    continue
                elif aa == 2:
                    print("Terimakasih Telah Berbelanja")
                    break
                

    elif pilih == 3:
            b3 = int(input("Jumlah Pembelian\n==> "))
            cangkir = 8000
            diskon = cangkir*45/100
            hasil = cangkir-diskon
            pilih3 = 'Cangkir'
            jumlah3 = b3
            if b3 >= 0:
                p3 = b3*hasil
                print("Ada Tambahan ? (Y : 1 / T : 2)")
                aa = int(input("==> "))
                if aa == 1:
                    continue
                elif aa == 2:
                    print("Terimakasih Telah Berbelanja")
                    break
print("Total Harga Belanjaan =>",p1+p2+p3)