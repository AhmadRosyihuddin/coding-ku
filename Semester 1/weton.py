print("Sumber Info : https://astor.id/mitos/primbon-jodoh/")
print("Perhitungan Weton Jawa Pernikahan")
print("===========================")
print("   HARI           PASAR\n---------------------------")
print("1. Minggu      1. Pahing \n2. Senin       2. Pon\n3. Selasa      3. Wage\n4. Rabu        4. Keliwon\n5. Kamis       5. Legi\n6. Juma'at\n7. Sabtu")
print("===========================")

start = True

while start :
    hari = int(input("Masukkan Hari Lahirmu (Masukkan Angka) => "))
    
    #kondisi cowok
    if hari == 1:
        hari = 5
        start = False
    elif hari == 2:
        hari = 4
        start = False
    elif hari == 3:
        hari = 3
        start = False
    elif hari == 4:
        hari = 7
        start = False
    elif hari == 5:
        hari =8
        start = False
    elif hari == 6:
        hari = 6
        start = False
    elif hari == 7:
        hari = 9
        start = False
    else:
        print("Error")

start1 = True
while start1:
    pasar = int(input("Masukkan Pasar Kelahiranmu (Masukkan Angka) => "))
    
    #kondisi cowok
    if pasar == 1:
        pasar = 9
        start1 = False
    elif pasar == 2:
        pasar= 7
        start1 = False
    elif pasar == 3:
        pasar = 4
        start1 = False
    elif pasar == 4:
        pasar = 8
        start1 = False
    elif pasar == 5:
        pasar = 5
        start1 = False
    else:
        print("Error")
        
print("=============================================")
        
stop = True
while stop:
    
    hari1 = int(input("Masukkan Hari Lahir Pasanganmu (Masukkan Angka) => "))
    
    #kondisi cewek
    if hari1 == 1:
            hari1 = 5
            stop = False
    elif hari1 == 2:
            hari1 = 4
            stop = False
    elif hari1 == 3:
            hari1 = 3
            stop = False
    elif hari1 == 4:
            hari1 = 7
            stop = False
    elif hari1 == 5:
            hari1 =8
            stop = False
    elif hari1 == 6:
            hari1 = 6
            stop = False
    elif hari1 == 7:
            hari1 = 9
            stop = False
    else:
            print("Error")
    

stop1 = True
while stop1:
    pasar1 = int(input("Masukkan Pasar Kelahiran Pasanganmu (Masukkan Angka) => "))

#kondisi cewek
    if pasar1 == 1:
            pasar1 = 9
            stop1 = False
    elif pasar1 == 2:
            pasar1 = 7
            stop1 = False
    elif pasar1 == 3:
            pasar1 = 4
            stop1 = False
    elif pasar1 == 4:
            pasar1 = 8
            stop1 = False
    elif pasar1 == 5:
            pasar1 = 5
            stop1= False
    else:
            print("Error")
print("="*40)
cowok = (hari + pasar)
cewek = (hari1 + pasar1)
hasil = (cewek + cowok)
print("Hasil Kalkulasi Weton = ",hasil)

pegat = (1,10,19,28)
ratu = (2,11,20,29)
jodoh = (3,12,21,30)
topo = (4,13,22,31)
tinari = (5,14,23,32)
padu = (6,15,24,33)
sujanan = (7,16,25,34)
pesthi = (8,17,26,35)
pegat1 = (9,18,27,36)


if hasil in pegat:
    print("-"*40)
    print(hasil,"Masuk Dalam PEGAT")
    print("Artinya\nJika hasil penjumlahanmu masuk kedalam Pegat,\nmaka kemungkinan di kedepannya saat kamu telah menikah\nmaka kamu akan sering sekali menemukan berbagai permasalahanmulai dari ekonomi, perselingkuhan, hingga KDRT yang dapat\nmenjadikan perceraian menjadi nyata.\n\nNah yang uniknya, pegat sendiri dalam konotasi bahasa jawa bisa berarti putus, sehingga jika kamu telah menghitung angkanya dan ternyata masuk kedalam kategori Pegat, lebih baik pikirkan lagi hubungan asmaramu itu sebelum masuk ke jenjang pernikahan.")
    
elif hari in ratu:
    print("-"*40)
    print(hasil,"Masuk Dalam RATU")
    print("Artinya\nJika angka yang muncul yaitu masuk kedalam kategori Ratu, maka ini bisa menjadi sebuah kabar bagus lho untuk kamu, dimana kategori ini akan membuat sebuah pasangan menjadi harmonis dan juga langgeng.\n\nJika perhitunganmu dengan pasanganmu masuk kedalam kategori ini, maka yakinilah bahwa yang kamu pilih adalah jodoh paling tepat yang dapat kamu lanjutkan ke jenjang pernikahan.")

elif hari in jodoh:
    print("-"*40)
    print(hasil,"Masuk Dalam JODOH")
    print("Artinya\nKategori ini masuk kedalam kategori yang cukup memberikan kabar kebahagiaan lhu untukmu dan pasanganmu, dimana jika perhitungan yang kamu lakukan tadi ternyata masuk kedalam kategori Jodoh maka pasanganmu itu akan sangat menerima segala kelebihan serta kekuranganmu lho.\n\nTentunya ruma tanggamu dikemudian hari akan dapat terjalin dan terbina secara harmonis hingga tua nanti.")

elif hari in topo:
    print("-"*40)
    print(hasil,"Masuk Dalam TOPO")
    print("Artinya\nKategori yang ini juga sebenarnya cukup bagus, akan tetapi dalam melakukan hubungan asmara dan juga rumah tangga akan mengalami berbagai macam kesusahan dan juga pilu pada awalnya, akan tetapi tentunya semua itu akan menjadi ujian bagi kamu dan pasanganmu sehingga kebahagiaanlah pada akhirnya yang akan kamu dapatkan.\n\nJika perhitungan primbon jodohmu berada pada kategori Topo, maka sesungguhnya ini merupakan kabar baik walau pada awalnya akan mendapatkan kesusahan. Yakinilah bahwa ini hanyalah ujian sementara.")
    
elif hari in tinari:
    print("-"*40)
    print(hasil,"Masuk Dalam TINARI")
    print("Artinya\nKategori ini juga akan mendapatkan kabar yang cukup bagus lho, dimana pasangan yang masuk kedalam kategori Tinari akan dapat mudah dalam menemukan kebahagiaan, gampang dalam mencari rezeki dan juga dilimpahi keberuntungan.\n\nApabila perhitungan kamu dengan pasanganmu masuk kedalam kategori Tinari, maka selamat, kehidupan rumah tanggamu akan dilimpahi keberuntungan dan juga keberkahan.")
    
elif hari in padu:
    print("-"*40)
    print(hasil,"Masuk Dalam PADU")
    print("Artinya\nPasangan yang masuk kedalam kategori ini sepertinya akan sering menghadapi yang namanya pertengkaran karena seringkali berbeda dalam mengambil keputusan, akan tetapi tidak sampai masuk kedalam perceraian kok.\n\nPermasalahan tersebut pun muncul karena alasan yang cukup sepele, jadi bagi kamu yang perhitungan primbon jodohnya masuk kedalam kategori ini, tentunya setiap masalah akan menghampiri semua pasangan dalam berkeluarga, tapi yakinlah dengan pasanganmu itu.")
    
elif hari in sujanan:
    print("-"*40)
    print(hasil,"Masuk Dalam SUJANAN")
    print("Artinya\nKategori ini tentunya cukup buruk lho, dimana jika perhitunganmu masuk kedalam kategori ini, maka saat berumah tangga akan sering sekali mengalami yang namanya pertengkaran dan juga kasus perselingkuhan baik itu dari kamu atau dari pasanganmu.")
    
elif hari in pesthi:
    print("-"*40)
    print(hasil,"Masuk Dalam PESTHI")
    print("Artinya\nKategori yang selanjutnya yaitu Pesthi, dimana jika perhitungannya masuk kedalam kategori ini, maka di kedepan harinya kehidupan rumah tangga pasangan tersebut akan harmonis, tenang, damai hingga akhir hayat kedua pasangan tersebut.\n\nBagi kamu yang dalam perhitungannya masuk kedalam kategori ini, maka selamat, hubungan asmaramu hingga lanjut kedalam ranah rumah tangga akan terjalin secara harmonis dan tentram.")
    
elif hari in pegat1:
    print("-"*40)
    print(hasil,"Masuk Dalam PEGAT")
    print("Artinya\nJika hasil penjumlahanmu masuk kedalam Pegat,\nmaka kemungkinan di kedepannya saat kamu telah menikah\nmaka kamu akan sering sekali menemukan berbagai permasalahanmulai dari ekonomi, perselingkuhan, hingga KDRT yang dapat\nmenjadikan perceraian menjadi nyata.\n\nNah yang uniknya, pegat sendiri dalam konotasi bahasa jawa bisa berarti putus, sehingga jika kamu telah menghitung angkanya dan ternyata masuk kedalam kategori Pegat, lebih baik pikirkan lagi hubungan asmaramu itu sebelum masuk ke jenjang pernikahan.")
    