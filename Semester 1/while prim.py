#Bilangan prima adalah bilangan bulat yang habis di bagi 1 dan bilangan itu sendiri
while True : # kondisi jika benar
    print("Ingin Mengetahui Bilangan Prima? ") # maka akan menampilkan "Ingin Mengetahui Bilangan Prima?"
    print("1. ya\n2. Tidaak") #Menampilakan pilihan
    user_input = float(input("Masukkan Nomor : ")) #meminta data dari user
    if user_input == 1: #jika user mamasukkan angka 1 maka
        x = float(input("Masukkan Angak : ")) #meminta data dari user
        if x > 1 : # jika user memasukkan angka lebih dari 1
            if x == 2: #maka jika angka tersebut adalah 2
                print(x,"Bilangan Prima") # maka tampilkan angka user dan tampilkan angka prima
            else: # jika user tidak memasukkan angka 1 atau 2 maka  
                if x % 2 == 0: # data user di modulus 2 apabila hasilnya sama dengan 0
                    print(x,"Bukan Bilangan Prima") # maka tampilkan data user dan bukan bilangan prima
                else : #atau jika user memasukkan angak lebih dari 3
                    p = 3 # kita buat variabel dengan isi data angka 3
                    while True: #kondisi benar
                        if x == p: # jika user memasukkan angka sama dengan p atau 3
                            print(x,"Bilangan Prima") # maka tampilkan "Bilangan Prima"
                            break # Menghentikan looping
                        else : # jika angka yang di masukkan bukan 3 maka akan di mod lagi dengan 3
                            if x % p > 0: # jika data user di modulus p lebih besar sama dengan 0 maka
                                p += 2 # akan di tambah dengan 2 dan dilooping
                            else: #jika loopingan dari mod p = 0 maka
                                 print(x,"Bukan Bilangan Prima") #tampilkan "bukan bilangan Prima"
                                 break # menghentikan loopingan
        else: #kecuali jika user memasukkan angka kurang dari 1
            print(x,"Bukan Bilangan Prima") # maka Tampilkan "Bukan Bilangan prima"
    elif user_input == 2: #jika user memasukkan angka angka pilihan sama dengan 2
        break #maka hentikan program
    else : #kecuali user memasukkan angka selain 1 dan 2 maka 
        print("WARNING!!!") #tampilkan "WARNING!!!"
        print("Masukkan Pilihan Mu Dengan Benar") # Tampilkan "Masukkan Pilihan MU Dengan Benar"  
    