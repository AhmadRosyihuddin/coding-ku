# Soal 1
def createlist(a):
    data_list = []
    for i in range(a):
        print('Masukkan data ke -',i,': ',end='')
        x = int(input())
        data_list.append(x)
    return data_list

def isprime(data):
    p = 0
    for i in data:
        for y in range(1,i+1):
            if i % y == 0:
                p += 1
        p = 0
    return p
def createlistPrime(data):
    prima = []
    if isprime(data) == 2:
        prima.append(isprime)
    return prima

data = createlist(10)
print('data list =',data)
prima = createlistPrime(data)
print('data prima =',prima)

# Soal 2
# def createList(a):
#     data_list1 = []
#     data_list12 = []
#     for i in range(a):
#         print('Masukkan data ke -',i,': ',end='')
#         x = int(input())
#         data_list1.append(x)
    
        
#     for i in range(a):
#         print('Masukkan data ke -',i,': ',end='')
#         x = int(input())
#         data_list12.append(x)
        
#     return data_list1, data_list12

# data1=createList(4)
# print('data - 1',data1)