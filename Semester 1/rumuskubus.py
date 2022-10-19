while True: #kondisi jika benar
    print("Rumus Kubus") #maka tampilkan Judul
    print("1. Hitung Luas Kubus\n2. Hitung Volume Kubus\n3. Exit") #tampilkan menu
    x = float(input("Masukkan Pilihan Mu : ")) #variabel berisi data user
    if x == 1: #kondisi jika user memilih angka 1
        s = float(input("Sisi Kubus : ")) #maka user di minta memasukkan data
        print("Luas Kubus : ",(s*s)*6) #menapilkan hasil dari rumus
    elif x == 2: #jika user memilih angka 2
        s = float(input("Sisi Kubus : ")) #maka user di minta memasukkan data
        print("Volume Kubus : ",s*s*s) #menampilkan hasil dari rumus
    elif x == 3: #jika user memilih angka 3
        break #menghentikan program looping
    else: #jika user tidak memasukkan dari angka - angka di atas maka 
        print("Error!!!") #tampilkan Error