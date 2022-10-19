romawi = str (input('Masukkan Angka Romawi : ')).upper()
data = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
hasil = 0
for i in range (len(romawi)) :
    print(i)
    print('j',data[romawi[i]],data[romawi[i-1]],hasil)
    if i == 0 or data[romawi[i]] <= data[romawi[i-1]] :
        hasil += data[romawi[i]]
    else :
           hasil = hasil + ( data[romawi[i]] - 2 * data[romawi[i-1]] )

print(romawi,'hasil konversi : ',hasil)
