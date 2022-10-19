#Soal 1
print(' Insertion Sort '.center(53,'='))
data = [6,4,9,2]
print('Data Awal =',data)
n = len(data)
for i in range(n):
    for y in range(n-1):
        if data[y]>data[y+1]:
            data[y],data[y+1] = data[y+1],data[y]
            print('Index ke %d Lebih Besar Dari Index Ke %d ='%(y+1,y),data)
        else:
            print('Index Ke %d Lebih Besar Dari Index Ke %d ='%(y,y+1),data)
    n -= 1
print('Data setelah Di Urutkan =',data)
print() 


print(' Quick Sort '.center(53,'='))
def pembagi(data,awal,akhir):
    pivot = data[akhir]
    i = awal - 1
    for j in range(awal, akhir):
        if data[j] < pivot:
            i += 1
            data[i],data[j] = data[j], data[i]
    data[i + 1],data[akhir] = data[akhir],data[i + 1]
    return i + 1


def quicksort(data,awal,akhir):
    if awal >= akhir:
        return
    p = pembagi(data,awal,akhir)
    quicksort(data,awal,akhir - 1)
    quicksort(data, p + 1, akhir)

data=[2,3,4,6,3,7,2,1]
print('Data Awal =',data)
quicksort(data,0,len(data)-1)
print('Data Setelah Di Sorting =',data)


#Soal 2
print()
print(' Squential Search '.center(53,'='))
def cari(data,x):
    for i in range(len(data)): 
        if data[i] == x:
            return i
dat = [2,4,5,3,5,8,9]
print('Data',5,'Dari Data =',dat,'\nAda Di Index =',cari(dat,5))
