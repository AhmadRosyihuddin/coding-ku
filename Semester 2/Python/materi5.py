# Rekursif
# def penjumlahan(x):
#     if x == 1:
#         return x
#     else:
#         return x * penjumlahan(x-1)

# hasil = penjumlahan(5)
# print('Hasil :',hasil)

'''
Ilustrasi
def tambah(5):
    else:
        return 5 * penjumlahan(x = 5-1)
                    else:
                        return 4 * penjumlahan(x = 4-1)
                                    else:
                                        return 3 * penjumlahan(x = 3-1)
                                                    else:
                                                        return 2 * penjumlahan(x = 2-1)
                                                                if x == 1:
                                                                        return x = 1
'''


# def pangkat(x,n):
#     if n == 1:
#         return x
#     else:
#         return x * pangkat(x,n-1)

# print('Hasil :',pangkat(5,3))








def towerOfHanoi(lempengan,asal,tujuan,bantuan):
    if lempengan == 1:
        print('Pindahkan Lempengan #%d Dari Tower %s Ke Tower %s'%(lempengan,asal,tujuan))
    else:
        towerOfHanoi(lempengan-1,asal,bantuan,tujuan)
        print('a')
        print('Pindahkan Lempengan #%d Dari Tower %s Ke Tower %s'%(lempengan,asal,tujuan))
        towerOfHanoi(lempengan-1,bantuan,tujuan,asal)
        
towerOfHanoi(3,'A','C','B')
'''
2 A B C
1 A C B
PRINT 1 A C
PRINT 
'''


'''
PINDAHKAN 4 LEMPENGAN DARI A KE C
1. (Asumsi) Pindahkan 3 Lempengan Dari A ke B
    1.a. (Asumsi) Pindahkan 2 Lempengan Dari A Ke C
        1.a.a. (Asumsi) Pindahkan 1 Lempengan Dari A ke B
            Pindahkan Lempengan Ke 1 dari A Ke B
        1.a.b. Pindahkan Lempengan Ke 2 Dari A Ke C
        1.a.c. (asumsi) Pindahkan Lempengan Dari B Ke C
            Pindahkan Lempengan Ke 2 Dari B Ke C
    1.b. Pindahkan Lempengan Ke 3 Dari A Ke B
    1.c. (Asumsi) Pindahkan 2 Lempengan Dari C Ke B
        1.c.a. pindahkan 
2. Pindahkan Lempengan ke 4 Dari A Ke C
3. (Asumsi) Pindahkan 3 Lempengan Dari B Ke C
4. 
'''

        
    

