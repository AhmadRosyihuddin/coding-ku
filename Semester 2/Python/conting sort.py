def countingSort(A,k):
    C=[]
    B=[]
    # Iterasi untuk inisialisasi array C dengan 0 sejumlah nilai max
    for i in range(k+1):
        C.append(0)
    print('(BEFORE) Array C :',C)
    
    # Iterasi untuk proses perhitungan tiap data dan meinisialisasi array B dengan 0
    for j in range(len(A)):
        C[A[j]] += 1
        B.append(0)
    print('(AFTER) Array C :',C)
    
    # Iterasi menjumlahkan tiap index C 
    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]
    print('(Penjumlahan Tiap Element) Array C :',C)
    
    # Iterasi Penempatan dan pengurutan data
    iterasi = 1
    for j in range(len(A)-1,-1,-1):
        # a= a[j] = 9
        # c = c[a] = 14
        # b = b[C] = 14-1 = 13
        B[C[A[j]]-1]=A[j]
        C[A[j]] -= 1
        iterasi += 1
        print(B)
    return(B,iterasi)

data = [2,1,1,2,5,4,2,8,7,7,9,2,1,9]
print(data)
hasil,jumlah = countingSort(data,max(data))
print('Hasil :',hasil)
print('jumlah iterasi :',jumlah)