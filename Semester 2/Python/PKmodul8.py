import random

def genarate_random(jumlah,min,max):
    data = []
    for i in range(jumlah):
        data.append(random.randint(min,max))
    return data

def remainderFunction (data,num):
    return (data%num)

def createHashTable(num):
    return [[None] for i in range(num)]

def putData(data,table):
    for i in range(len(data)):
        ind=remainderFunction(data[i],len(table))
        if table[ind][0] == None:
            table[ind][0]=data[i]
        else:
            table[ind].append(data[i])
    return(table)

def searchHash(data,table):
    hashVal=remainderFunction(data,len(table))
    iterasi = 1
    if table[hashVal] != 'none':
        for i in range(len(table[hashVal])):
            if data == table[hashVal][i]:
                print(iterasi)
                return (hashVal,i,True)
            iterasi += 1
    else:
        return False
 
data = genarate_random(500,0,10000)
data1 = [1,3,7,5,12,11,10,44]
data2 = [10,1,3,5,8,7,12,11,44]
# print(data)
numOfSlot = 12
hashTabel = createHashTable(numOfSlot)
hashTabel = putData(data1,hashTabel)
print(hashTabel)
findData = 7
found = searchHash(findData,hashTabel)
if not found:
    print('{} Is Not In The Hash Table'.format(findData))
else:
    print('{} Is In Slot {} Index : {}'.format(findData,found[0],found[1]))
    print('Data In Slot [{}] : {}'.format(found[0],hashTabel[found[0]]))



# class BilanganPecahan:
#     def __init__(self,pembilang,penyebut):
#         self.pembilang = pembilang
#         self.penyebut = penyebut
    
#     def jumlah(self,num1,num2):
#         p1 = num1.penyebut
#         p2 = num2.penyebut
#         start = True
#         while start:
#             if p1 < p2:
#                 p1 += num1.penyebut
#             elif p2 < p1:
#                 p2 += num2.penyebut
#             else:
#                 p_sama = p1
#                 start = False
#         pemb1 = (p_sama/num1.penyebut)*num1.pembilang
#         pemb2 = (p_sama/num2.penyebut)*num2.pembilang
#         self.pembilang = int(pemb1 + pemb2)
#         self.penyebut = p_sama
        
#     def display(self):
#         return ('{}/{}'.format(self.pembilang,self.penyebut))

# num1 = BilanganPecahan(4,6)
# num2 = BilanganPecahan(1,4)
# num3 = BilanganPecahan(0,0)
# num3.jumlah(num1,num2)
# print(num1.display())
# print(num2.display())
# print(num3.display())
