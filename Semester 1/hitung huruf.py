vocal = 0
tamp_voc =''
spasi = 0
tamp_spas = ''
konsonan = 0
tamp_kons = ''
a = str(input("masukkan Kata => "))
for i in a:
    if i == "a" or i == "A" or i == "i" or i == "I" or i == "u" or i == "U" or i == "e" or i == "E" or i == "o" or i == "O":
        tamp_voc += i
        tamp_voc += ' '
        vocal += 1
    elif i == ' ':
        spasi += 1
        tamp_spas += i
    else:
        konsonan += 1
        tamp_kons += i
        tamp_kons += ' '
        
print("Jumlah Huruf Vokal = ",vocal,",","Yaitu :",tamp_voc)
print("Jumlah Huruf Konsonan = ",konsonan,",","Yaitu :",tamp_kons)
print("Jumlah Spasi = ",spasi)
