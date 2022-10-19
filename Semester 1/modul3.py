# #ofsett
# data="ahlaqul karimah"
# nilai=data[1:5]
# print(nilai)

# #upper
# data="ahlaqul karimah"
# print(data.upper(1))

# #find
# data="ahlaqul karimah"
# print(data.find("a"))

#menentukan jumlah huruf vokal
data=input("masukkan data=")
nilai=data
nilai=nilai.lower()
data_vokal=[]
data_konsonan=[]
banyak_vokal=0
banyak_konsonan=0
spasi=0
for ch in data:
  if ch=="a" or ch=="i" or ch=="u" or ch=="e" or ch=="o" :
    banyak_vokal=banyak_vokal+1
    data_vokal.append(ch)
  elif ch==" ":
    spasi=spasi+1
  else:
    banyak_konsonan=banyak_konsonan+1
    data_konsonan.append(ch)
print("banyak huruf vokal =", banyak_vokal, "adalah =", data_vokal)
print("banyak huruf konsonan =", banyak_konsonan, "adalah =", data_konsonan)
print("spasi =", spasi)

# #ofsett karakter
# kalimat=input('Masukkan kalimat = ')
# huruf=input('Masukkan huruf yang di cari = ')
# c=0
# for i in range(len(a)) :
#     if kalimat[i]==huruf or kalimat.upper()[i]==huruf.upper() :
#         c+=1
#         print('huruf',huruf,'atau huruf',huruf.upper(),'ke- ',c,': offset- ',i)

# #konfersi bilangan
# stop=False
# while not(stop) :
#     print('Menu')
#     print('Tekan 1 untuk konversi Desimal ke Biner\nTekan 2 untuk konversi Biner ke desimal')
#     pilih=int(input('Masukkan pilihan anda = '))
#     if pilih==1 :
#         bilangan=int(input('Masukkan Desimal = '))
#         totalDiv=bilangan
#         Biner=''
#         while totalDiv!=0 :
#             totalMod=totalDiv%2
#             totalDiv=totalDiv//2
#             Biner=str(totalMod)+Biner
#             print(totalMod)
#     elif pilih==2 :
#         binstr=input('Masukkan nilai = ')
#         pangkat=0
#         hasil=0
#         for i in range(len(binstr)-1,-1,-1):
#             hasil=hasil+int(binstr[i])*2**pangkat
#             pangkat+=1
#         print(hasil)
#     pilihan=input('Ingin mengulang operasi kembali ? click (y/t) : ')
#     if pilihan=='y' :
#         stop=False
#     else :
#         stop=True

        
