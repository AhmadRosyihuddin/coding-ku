'''print("========FAKTOR PEMBAGI========")
data=int(input("masukkan bilangan="))
faktor_pembagi=0
faktor=[]
a= 1
while a <=data:
  if (data%a)==0:
    faktor_pembagi=faktor_pembagi+1
    faktor.append(a)
  a=a+1

print("Faktor pembagi dari",data, "adalah", faktor)



#FPB
print("====FAKTOR PERSEKUTUAN TERBESAR/FPB====")
x=[]
y=[]
FPB= []
a= int(input("masukkan bilangan pertama: "))
b= int(input("masukkan bilangan kedua: "))
for i in range(1, a+1):
    if a % i==0:
        x.append(i)
for i in range(1, b+1):
    if b%i==0:
        y.append(i)
for i in range(1, a+1 or b+1):
    if b%i==0 and a%i==0:
        FPB.append(i)
print("faktor pembagi",a,"=",x)
print("faktor pembagi",b,"=",y)
print("faktor pembagi yang sama, yaitu=",FPB,"FPB=",FPB)


#DATA MAHASISWA
print("=====DATA NILAI MAHASISWA=====")#a. input nilai mahasiswa
a=int(input("masukkan banyak mahasiswa="))
for i in range(a):
  print("mahasiswa ke-",i+1)
  b=str(input("masukkan nama mahasiswa="))
  c=int(input("masukkan nilai mahasiswa="))
'''

#MENU DATA MAHASISWA
print("======MENU DATA MAHASIAWA======")
data = []
nilai = []
print("daftar mahasiswa=")
banyak = int(input("Jumlah Mahasiswa = "))
for i in range(1,banyak+1):
    print("Mahasiswa ke-",i)
    inp_data = str(input("nama mahasiswa=")).title()
    inp_nilai = int(input("Nilai Mahasiswa = "))
    data.append(inp_data)
    nilai.append(inp_nilai)
print("\nDashboard\n1. Daftar Mahasiswa Dan NIlai\n2. Nilai Rata - Rata Mahasiswa\n3. Daftar Mahasiswa Yang Melebihi Threshold\n4. Nilai Maksimal")
opsi = int(input("Pilih Opsi \n= "))
if opsi == 1:
    name = len(data and nilai)
    for i in range(name):
        print(i+1,".",data[i],'\t=',nilai[i])

elif opsi == 2:
    jumlah = 0
    score = len(nilai)
    for i in nilai:
        jumlah += i
    print('Nilai Rata - Rata Mahasiswa :',jumlah/score)
    
elif opsi == 3:
    trs = []
    inp = int(input("Masukkan Nilai Threshold => "))
    for i in nilai:
        if i > inp:
            trs.append(i)
    print("Nilai Thresold :",trs)
elif opsi == 4:
    print("Nilai Maksimal Dari Semua Mahasiswa :",max(nilai))

'''
a = int(input('masukkan angka ke-1='))
b = int(input('masukkan angka ke-2='))
faktor_a=[]
faktor_b=[]
Fpb=[]
hasil=0
for i in range (1, a+1):
  if a % i == 0:
    faktor_a.append(i)
for u in range (1, b+1):
  if b % u == 0:
    faktor_b.append(u)
for e in faktor_a:
  for f in faktor_b:
    if e == f :
      Fpb.append(e)
for i in Fpb:
  if i == Fpb[-1]:
print('faktor pembagi',a,'=',faktor_a)
print('faktor pembagi',b,'=',faktor_b)
print('pembaginya',Fpb,'FPB',hasil)
'''



