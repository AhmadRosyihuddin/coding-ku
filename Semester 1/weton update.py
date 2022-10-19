def hari():
    hari = [5,4,3,7,8,6,9]
    start = True
    while start:
        x = int(input('Pilih Hari (Masukkan Angka)=> '))
        if x <= len(hari):
            return hari[x-1]
        else:
            print('Pilihan hanya dari 1 sampai 7')

def pasar():
    pasar = [5,9,7,4,8]
    start = True
    while start:
        x = int(input('Pilih Pasar (Masukkan Angka)=> '))
        if x <= len(pasar):
            return pasar[x-1]
        else:
            print('Pilihan hanya dari 1 sampai 5')
    
def ramalan(x):
    ramal = [
        [1,10,19,28],# Pegat
        [2,11,20,29],# Ratu
        [3,12,21,30],# Jodoh
        [4,13,22,31],# Topo
        [5,14,23,32],# Tinari
        [6,15,24,33],# Padu
        [7,16,25,34],# Sujanan
        [8,17,26,35],# Pesthi
        [9,18,27,36]# Pegat
    ]
    a = [
        '''Artinya :
         Jika hasil penjumlahanmu masuk kedalam Pegat,
         maka kemungkinan di kedepannya saat kamu telah menikah
         maka kamu akan sering sekali menemukan berbagai permasalahanmulai dari ekonomi, perselingkuhan,
         hingga KDRT yang dapat menjadikan perceraian menjadi nyata.
         Nah yang uniknya, pegat sendiri dalam konotasi bahasa jawa bisa berarti putus, 
         sehingga jika kamu telah menghitung angkanya dan ternyata masuk kedalam kategori Pegat, 
         lebih baik pikirkan lagi hubungan asmaramu itu sebelum masuk ke jenjang pernikahan.''',
         
         '''Artinya:
         Jika angka yang muncul yaitu masuk kedalam kategori Ratu,
         maka ini bisa menjadi sebuah kabar bagus lho untuk kamu, 
         dimana kategori ini akan membuat sebuah pasangan menjadi harmonis dan juga langgeng.
         Jika perhitunganmu dengan pasanganmu masuk kedalam kategori ini, 
         maka yakinilah bahwa yang kamu pilih adalah jodoh paling tepat yang dapat kamu lanjutkan ke jenjang pernikahan.''',
         
         '''Artinya:
         Kategori ini masuk kedalam kategori yang cukup memberikan kabar kebahagiaan lhu untukmu dan pasanganmu,
         dimana jika perhitungan yang kamu lakukan tadi ternyata masuk kedalam kategori Jodoh 
         maka pasanganmu itu akan sangat menerima segala kelebihan serta kekuranganmu lho.
         Tentunya ruma tanggamu dikemudian hari akan dapat terjalin dan terbina secara harmonis hingga tua nanti.''',
         
         '''Artinya:
         Kategori yang ini juga sebenarnya cukup bagus, akan tetapi dalam melakukan hubungan asmara 
         dan juga rumah tangga akan mengalami berbagai macam kesusahan dan juga pilu pada awalnya, 
         akan tetapi tentunya semua itu akan menjadi ujian bagi kamu dan pasanganmu 
         sehingga kebahagiaanlah pada akhirnya yang akan kamu dapatkan.
         Jika perhitungan primbon jodohmu berada pada kategori Topo, 
         maka sesungguhnya ini merupakan kabar baik walau pada awalnya akan mendapatkan kesusahan. 
         Yakinilah bahwa ini hanyalah ujian sementara.''',
         
         '''Artinya:
         Kategori ini juga akan mendapatkan kabar yang cukup bagus lho, 
         dimana pasangan yang masuk kedalam kategori Tinari akan dapat mudah dalam menemukan kebahagiaan, 
         gampang dalam mencari rezeki dan juga dilimpahi keberuntungan.
         Apabila perhitungan kamu dengan pasanganmu masuk kedalam kategori Tinari, 
         maka selamat, kehidupan rumah tanggamu akan dilimpahi keberuntungan dan juga keberkahan.''',
         
         '''Artinya:
         Pasangan yang masuk kedalam kategori ini sepertinya akan sering menghadapi yang namanya 
         pertengkaran karena seringkali berbeda dalam mengambil keputusan, 
         akan tetapi tidak sampai masuk kedalam perceraian kok.
         Permasalahan tersebut pun muncul karena alasan yang cukup sepele, 
         jadi bagi kamu yang perhitungan primbon jodohnya masuk kedalam kategori ini, 
         tentunya setiap masalah akan menghampiri semua pasangan dalam berkeluarga, tapi yakinlah dengan pasanganmu itu.''',
         
         '''Artinya:
         Kategori ini tentunya cukup buruk lho, dimana jika perhitunganmu masuk kedalam kategori ini, 
         maka saat berumah tangga akan sering sekali mengalami yang namanya pertengkaran dan juga kasus 
         perselingkuhan baik itu dari kamu atau dari pasanganmu.''',
         
         '''Artinya:
         Kategori yang selanjutnya yaitu Pesthi, dimana jika perhitungannya masuk kedalam kategori ini, 
         maka di kedepan harinya kehidupan rumah tangga pasangan tersebut akan harmonis, tenang, 
         damai hingga akhir hayat kedua pasangan tersebut. Bagi kamu yang dalam perhitungannya 
         masuk kedalam kategori ini, maka selamat, hubungan asmaramu hingga lanjut kedalam 
         ranah rumah tangga akan terjalin secara harmonis dan tentram.''',
         
         '''Artinya:
         Jika hasil penjumlahanmu masuk kedalam Pegat, maka kemungkinan di kedepannya saat kamu telah menikah
         maka kamu akan sering sekali menemukan berbagai permasalahanmulai dari ekonomi, perselingkuhan, 
         hingga KDRT yang dapat menjadikan perceraian menjadi nyata.Nah yang uniknya, 
         pegat sendiri dalam konotasi bahasa jawa bisa berarti putus, sehingga jika kamu telah menghitung angkanya
         dan ternyata masuk kedalam kategori Pegat, lebih baik pikirkan lagi hubungan asmaramu itu sebelum masuk ke jenjang pernikahan.'''
         ]
    for i in range(len(ramal)):
        for y in range(len(ramal[0])):
            if x == ramal[i][y]:
                return a[i]
                 


print('HARI'.ljust(15),'PASAR','\n1. MINGU'.ljust(15),'1. LEGI','\n2. SENIN'.ljust(15),'2. PAHING','\n3. SELASA'.ljust(15),'3. PON','\n4. RABU'.ljust(15),'4. WAGE','\n5. KAMIS'.ljust(15),'5. KELIWON','\n6. JUMA\'AT\n7. SABTU')
# Laki - Laki
print('Masukkan Weton Mu')
cowok = hari() + pasar()

# Perempuan
print('Masukkan Weton Pasangan Mu')
cewek = hari() + pasar()

hasil = cowok + cewek
print('Hasil =',hasil,'\n',ramalan(hasil))



