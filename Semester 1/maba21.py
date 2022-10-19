list1 = []
list2 = []
hasil=[]
print('List 1')
banyak1 = int(input('masukkan banyak data : '))
for i in range (banyak1):
    data1 = int(input('masukkan list angka : '))
    list1.append(data1)

print('=============================')
print('List 2')
banyak2 = int(input('masukkan banyak data : '))
for i in range (banyak2):
    data2 = int(input('masukkan list angka : '))
    list2.append(data2)
print('list 1 :',list1)
print('List 2 :',list2)

if len(list1)>len(list2):
    for i in range (len(list1)-len(list2)):
        list2.append(0)
else:
    for i in range (len(list2)-len(list1)):
        list1.append(0)

for x in range (len(list1)):
    hasil.append(int(list1[x]+list2[x]))
print('Hasil akhir :',hasil)