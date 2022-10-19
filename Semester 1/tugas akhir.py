daftar = [['MIE AYAM','BAKSO','NASI GORENG','SATE','SOTO','RAWON','PENYETAN'],
          [12000,8000,10000,20000,10000,15000,18000],
          ['JUS JERUK','JUS LEMON','COKLAT','CAPPUCINO','KOPI','ES TEH','LEMON TEA'],
          [5000,12000,14000,9000,7000,4000,10000]]


def menu():
    print('+'.ljust(71,'-')+'+')
    print('|'.ljust(0)+' BUKU MENU '.center(70,'~')+'|'.rjust(0))
    print('+'.ljust(71,'-')+'+')
    print('|','<< MAKANAN >>'.ljust(50),'<< HARGA >>'.ljust(18)+'|')
    print('|'.ljust(71)+'|')
    for i in range(5):
        if i == 3:
            print('|','NB :'.ljust(69)+'|','\n|','Diskon 15% Jika pembelian di atas Rp. 100.000'.ljust(69)+'|')
            print('|'+'SELAMAT MAKAN'.center(70)+'|')
        elif i == 4:
            print('+'.ljust(71,'-')+'+')
        else:    
            for baris in range(7):
                if i == 0:
                    print('|',str(baris+1)+'.',str(daftar[0][baris]).ljust(50,'.'),'Rp.',str(daftar[1][baris]).ljust(11)+'|')
                elif i == 1:
                    print('|'.ljust(71)+'|')
                    print('|','<< MINUMAN >>'.ljust(50),'<< HARGA >>'.ljust(18)+'|')
                    print('|'.ljust(71)+'|')
                    break
                else:
                    print('|',str(baris+1)+'.',str(daftar[2][baris]).ljust(50,'.'),'Rp.',str(daftar[3][baris]).ljust(11)+'|')

def billPembayaran(x):
    for i in range(1,len(x),2):
        for y in range(1):
            x[i][y]



def harga():
    bill = [['BAKSO'],['8000'],['MIE'],['2000']]
    start = True
    while start:
        kategori = int(input('MAU PESAN APA ?\n1. MAKANANA (Tekan 1)\n2. MINUMAN(Tekan 2)\n=> '))
        if kategori == 1:
            makanan = int(input('PILIH MAKANAN (MASUKKAN NOMOR MENU)\n=> '))
            porsi = int(input('BERAPA PORSI ?\n=> '))
            bill.append([daftar[0][makanan-1]])
            harga = daftar[1][makanan-1] * porsi
            bill.append([harga])
            
        elif kategori == 2:
            minuman = int(input('PILIH MINUMAN (MASUKKAN NOMOR MENU)\n=> '))
            porsi = int(input('PESAN BERAPA ?\n=> '))
            bill.append([daftar[0][makanan-1]])
            harga = daftar[1][makanan-1] * porsi
            bill.append([harga])
            
             
        ulang = input('ADA TAMBAHAN ?(Y/1) (N/2)\n=> ').upper()
        if ulang == 'Y' or ulang == '1':
            start = True
        else:
            start = False
    return bill
        
        

mulai = True
while mulai:
    pilih = int(input('VIRTAL RESTAURANT\n1. TAMPILKAN BUKU MENU\n2. PESAN MAKANAN\n3. TAMPILKAN BILL PEMBAYARAN\n4. EXIT\n=> '))
    if pilih == 1:
        menu()
    elif pilih == 2:
        nilai = harga()
    elif pilih == 3:
        billPembayaran(n ilai)    
    
    elif pilih == 4:
        mulai = False
