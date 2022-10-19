from datetime import datetime
database = [
    ['Ahmad Rosyihuddin',20000000000000,'123456','00112233'],
    ['Ahmad Fanani',2000000000000,'111111','00112244'],
    ['Ahmad Hikam Al Afhami',2000000000000,'000000','00112255'],
    ['Arshelia Romadhona',2000000000000,'222222','00112266'],
    ['Nanda Putri Febriantono',200000000000,'333333','00112277'],
    ['Uswatun Chasanah',20000000000,'444444','00112288']
]   # [Nama Nasbah, Saldo ATM, PIN ATM, Nomor Rekening]


def pin_atm(x,c):
    for i in range(len(c)):
        for y in range(len(c[0])):
            if x == c[i][y]:
                return i
    else:
        return 'PIN SALAH!!!'

def info_saldo(x):
    
    print('Saldo Anda Rp. {:,}'.format(database[x][1]))

def tarik_tunai(y,index):
    temp = [100000,300000,1000000,1500000]
    inp = int(input('1. 100.000\n2. 300.000\n3. 1.000.000\n4. 1.500.000\n5. Penarikan Lain\n=> '))
    if inp == 1: 
        if temp[inp-1] < y[index][1]:
            a = y[index][1] - 100000
            del(database[index][1])
            database[index].insert(1,a)
            print('Penarikan Berhasil Silahkan Ambil Uang Anda')
            return 100000
        else:
            return 'Saldo Tidak Cukup'
        
    elif inp == 2:
        if temp[inp-1] < y[index][1]:
            a = y[index][1] - 300000
            del(database[index][1])
            database[index].insert(1,a)
            print('Penarikan Berhasil Silahkan Ambil Uang Anda')
            return 300000
        else:
            return 'Saldo Tidak Cukup'
        
    elif inp == 3:
        if temp[inp-1] < y[index][1]:
            a = y[index][1] - 1000000
            del(database[index][1])
            database[index].insert(1,a)
            print('Penarikan Berhasil Silahkan Ambil Uang Anda')
            return 1000000
        else:
            return 'Saldo Tidak Cukup'
        
    elif inp == 4:
        if temp[inp-1] < y[index][1]:
            a = y[index][1] - 1500000
            del(database[index][1])
            database[index].insert(1,a)
            print('Penarikan Berhasil Silahkan Ambil Uang Anda')
            return 1500000
        else:
            return 'Saldo Tidak Cukup'
        
    elif inp == 5:
        uang = float(input('Jumlah Penarikan => '))
        if uang < y[index][1]:
            a = y[index][1] - uang
            del(database[index][1])
            database[index].insert(1,a)
            print('Penarikan Berhasil Silahkan Ambil Uang Anda')
            return uang
        else:
            return 'Saldo Tidak Cukup'

def pin_baru(x,index_pin):
    pilih = int(input('1. PIN Baru\n2. Batal\n=> '))
    if pilih == 1:
        while x != 6:
            ubah_pin = input('Masukkan PIN Baru => ')
            if len(ubah_pin) == 6:
                del(database[index_pin][2])
                database[index_pin].insert(2,ubah_pin)
                print('PIN Berhasil Di Rubah')
                return 6
            else:
                print('PIN Harus 6 Digit')

def transfer(x,data,index):
    index_rek = -1
    while x != 6:
        NoRek = input('Masukkan Nomor Rekening => ')
        if len(NoRek) == 8:
            x = 6
        else:
            print('Masukkan 8 Digit Angka')
            
        for i in range(len(data)):
            for y in range(len(data[0])):
                if NoRek == data[i][y]:
                    index_rek = i
                    
        if index_rek < 0:
            print('Nomor Rekening Tidak Terdaftar')
            x = 0
                
    temp = [100000,300000,1000000,1500000]
    inp = int(input('1. 100.000\n2. 300.000\n3. 1.000.000\n4. 1.500.000\n5. Menu Lain\n=> '))
    if inp == 1:
        if temp[inp-1] < data[index][1]:
            a = data[index][1] - 100000
            del(database[index][1])
            database[index].insert(1,a)
            
            b = data[index_rek][1] + 100000
            del(database[index_rek][1])
            database[index_rek].insert(1,b)
            
            print('Transfer Berhasil')
            return {'a':index_rek,'b':10000}

        else:
            return 'Saldo Tidak Cukup'
        
    elif inp == 2:
        if temp[inp-1] < data[index][1]:
            a = data[index][1] - 300000
            del(database[index][1])
            database[index].insert(1,a)
            
            b = data[index_rek][1] + 300000
            del(database[index_rek][1])
            database[index_rek].insert(1,b)
            
            print('Transfer Berhasil')
            return {'a':index_rek,'b':300000}

        else:
            return 'Saldo Tidak Cukup'
        
    elif inp == 3:
        if temp[inp-1] < data[index][1]:
            a = data[index][1] - 1000000
            del(database[index][1])
            database[index].insert(1,a)
            
            b = data[index_rek][1] + 1000000
            del(database[index_rek][1])
            database[index_rek].insert(1,b)
            
            print('Transfer Berhasil')
            return {'a':index_rek,'b':1000000}

        else:
            return 'Saldo Tidak Cukup'
        
    elif inp == 4:
        if temp[inp-1] < data[index][1]:
            a = data[index][1] - 1500000
            del(database[index][1])
            database[index].insert(1,a)
            
            b = data[index_rek][1] + 1500000
            del(database[index_rek][1])
            database[index_rek].insert(1,b)
            
            print('Transfer Berhasil')
            return {'a':index_rek,'b':1500000}
        else:
            return 'Saldo Tidak Cukup'
        
    elif inp == 5:
        jumlah = float(input('Jumlah Yang Di Transfer => '))
        if jumlah < data[index][1]:
            a = data[index][1] - jumlah
            del(database[index][1])
            database[index].insert(1,a)

            b = data[index_rek][1] + jumlah
            del(database[index_rek][1])
            database[index_rek].insert(1,b)

            print('Transfer Berhasil')
            return {'a':index_rek,'b':jumlah}
        else:
            return 'Saldo Tidak Cukup'
        
    

def top_up(x,index):
     nominal = int(input('Masukkan Nominal Uang => '))
     a = x[index][1] + nominal
     del(database[index][1])
     database[index].insert(1,a)
     print('Saldo Berhasil Di Tambahkan')

def struk_penarikan(data,index,penarikan):
    for i in range(16):
        if i == 0 or i == 15:
            print('+'.ljust(60,'-')+'+')
        elif i == 1:
            print('|'+'Bank ABC Cabang Samudra Pasifik'.center(59)+'|')
        elif i == 2:
            print('|'+'Jalan Permata Indah No. 5 Selat Hindia'.center(59)+'|')
        elif i == 4:
            print('|',datetime.now().strftime('%d/%m/%y   %H:%M:%S').ljust(58)+'|')
        elif i == 5:
            print('|','No Rekening'.ljust(15)+':', str(data[index][3]).ljust(41) +'|')
        elif i == 6:
            print('|','Nama'.ljust(15)+':', str(data[index][0]).ljust(41) +'|')
        elif i == 8:
            print('|','Jumlah Penarikan'.ljust(20)+': Rp. {:,}'.format(penarikan).ljust(38) +'|')
        elif i == 9:
            print('|','Sisa Saldo'.ljust(20)+': Rp. {:,}'.format(data[index][1]).ljust(38) +'|')
        elif i == 11:
            print('|','Bank ABC Menjaga Uang Anda Agar Bisa Hemat'.ljust(58)+'|')
        elif i == 12:
            print('|','Dan Tahan Lama'.ljust(58)+'|')
        elif i == 14:
            print('|','Terimakasih Telah Menggunakan Layanan Kami :)'.ljust(58)+'|')
        else:
            print('|'.ljust(60)+'|')

def struk_tf(data,index,penarikan):
    for i in range(17):
        if i == 0 or i == 16:
            print('+'.ljust(60,'-')+'+')
        elif i == 1:
            print('|'+'Bank ABC Cabang Samudra Pasifik'.center(59)+'|')
        elif i == 2:
            print('|'+'Jalan Permata Indah No. 5 Selat Hindia'.center(59)+'|')
        elif i == 4:
            print('|',datetime.now().strftime('%d/%m/%y   %H:%M:%S').ljust(58)+'|')
        elif i == 5:
            print('|','No Rekening'.ljust(15)+':', str(data[index][3]).ljust(41) +'|')
        elif i == 6:
            print('|','Nama'.ljust(15)+':', str(data[index][0]).ljust(41) +'|')
        elif i == 8:
            print('|','Transfer ATM Ke'.ljust(58) +'|')
        elif i == 9:
            print('|','Nomor Rekening'.ljust(15)+':',str(data[penarikan.get('a')][3]).ljust(41) +'|')
        elif i == 10:
            print('|','Nama'.ljust(15)+':', str(data[penarikan.get('a')][0]).ljust(41) +'|')
        elif i == 11:
            print('|','Jumlah '.ljust(15)+': Rp. {:,}'.format(penarikan.get('b')).ljust(43) +'|')
        elif i == 13:
            print('|','Bank ABC Menjaga Uang Anda Agar Bisa Hemat'.ljust(58)+'|')
        elif i == 14:
            print('|','Dan Tahan Lama'.ljust(58)+'|')
        elif i == 15:
            print('|','Terimakasih Telah Menggunakan Layanan Kami :)'.ljust(58)+'|')
        else:
            print('|'.ljust(60)+'|')

start = True
while start:
    menu = int(input('1. Masukkan PIN\n2. BATAL\n=> '))
    if menu == 1:
        pin = input('Masukkan PIN => ')
        index_pin = pin_atm(pin,database)
        if index_pin != 'PIN SALAH!!!':
            x = 0
            while x != 6:
                x = int(input('Menu :\n1. Informasi Saldo\n2. Tarik Tunai\n3. Ubah PIN\n4. TOP UP Saldo\n5. Transfer\n6. Keluar\n=> '))
                if x == 1:
                    info_saldo(index_pin)
                elif x == 2:
                    dana = tarik_tunai(database,index_pin)
                    if dana != 'Saldo Tidak Cukup':
                        struk_penarikan(database,index_pin,dana)   
                    else:
                        print(dana)
                elif x == 3:
                    x = pin_baru(x,index_pin)
                elif x == 4:
                    top_up(database,index_pin)
                elif x == 5:
                    tf = transfer(x,database,index_pin)
                    if tf != 'Saldo Tidak Cukup':
                        struk_tf(database,index_pin,tf)
                    else:
                        print(tf)
        else:
            print(index_pin)
    elif menu == 2:
        start = False
    else:
        print('Tidak Ada Menu')

