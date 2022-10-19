# Insertion Sort Dari Belakang
# def insertionBack(data):
#     print('Data Awal =',data)
#     for i in range(len(data)-2,-1,-1):
#         key = data[i]
#         ind = i
#         while temp < len(data)-1 and data[ind+1] < key:
#             data[ind] = data[ind+1]
#             ind += 1
#             print('Inner :',data)
#             data[ind] = key
#             print('Sorted :',data)
#             print()
#     return data

# data = [10,2,1,5,20,8,15]
# print('Hasil =',insertionBack(data))

# def faktor(angka1,angka2):
#     hasil = []
#     for i in range(1,angka1+1):
#         if angka1 % i == 0 and angka2 % i == 0:
#             hasil.append(i)
#     return hasil
 
# print(faktor(98,84))


import m1StackModul as st
def stackAscending(data1,data2):
    data = st.stack()
    key = st.pop(data1)
    st.push(data,key)
    n1 = len(data1)
    n2 = len(data2)

    while st.isEmpty(data1) and st.isEmpty(data2):
        if st.peek(data1) > st.peek(data2):
            if st.peek(data1) > st.peek(data):
                st.push(data,st.peek(data1))
            else:
                temp = st.pop(data)
                ind = '
     
stack1 = [45,30,11,10,8,4]
stack2 = [87,56,51,40,38,25,18,12,7,5]