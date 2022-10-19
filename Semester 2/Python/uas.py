# # Bagian0
# def urut(a,b,n):
#     if n == 1:
#         hasil = a
#     else:
#         hasil = b + urut(a,b,n-1)
#     return hasil

# print(urut(1,3,4))

# Bagian1
# class pixel:
#     def __init__(self,nama,x,y):
#         self.nama = nama 
#         self.x = (x)
#         self.y = (y)
#     def moveLeft(self,data):
#         self.x -= data
#     def moveRight(self,data):
#         self.x += data
#     def moveForward(self,data):
#         self.y -= data
#     def moveBackward(self,data):
#         self.y += data
#     def display(self):
#         print (f'{self.nama} : ({self.x},{self.y})')

# pix1 = pixel("point 1",0,0)
# pix1.moveLeft(3)
# pix1.moveForward(1)
# pix1.display()

#Bagian2
# def createHashTable(num):
#       return [[None]] * num
# def remainder(data,num):
#   return data % num
# def nilai(strData):
#     temp = 0
#     for i in strData:
#         temp += ord(i)
#     return temp
# def putData(data,table):
#     for i in data:
#         slot = remainder(nilai(i),len(table))
#         if table[slot] == [None]:
#             table[slot] = [i]
#         else:
#             table[slot].append(i)
#     return table
# def searchHash(data,table):
#     slot = remainder(nilai(data),len(table))
#     cek = 0
#     for ind,num in enumerate(table[slot]):
#         if num == data:
#             cek += 1
#             return (f'data {data} berada di slot ke- {slot} dan indeks ke- {ind}')
#     if cek == 0:
#         return (f'data {data} tidak ada')

# data = ['diah','dina','andi','hadi','tiara']
# hashTabel = createHashTable(11)
# hashTabel = putData(data,hashTabel)

# print(searchHash('indah',hashTabel))
# print(searchHash('dina',hashTabel))
# print(searchHash('andi',hashTabel))
# print(searchHash('hadi',hashTabel))
# print(searchHash('diah',hashTabel))

#Bagian3
def stack():
    s = []
    return s

def push(s,data):
    s.append(data)
  
def pop(s):
    data = s.pop()
    return data

def peek(s):
    return s[len(s)-1]
  
def isEmpty(s):
    return s == []

def size(s):
    return len(s)
  
class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,leftNode):
        nodeChild = BinaryTree(leftNode)
        if self.leftChild == None:
          self.leftChild = nodeChild
        else:
          nodeChild.leftChild = self.leftChild
          self.leftChild = nodeChild

    def insertRight(self,rightNode):
        nodeChild = BinaryTree(rightNode)
        if self.rightChild == None:
          self.rightChild = nodeChild
        else:
          nodeChild.rightChild = self.rightChild
          self.rightChild = nodeChild
    def getRightChild(self):
      return self.rightChild
    def getLeftChild(self):
      return self.leftChild
    def setRootVal(self,obj):
      self.key = obj
    def getRootVal(self):
      return self.key
    
def buildParseTree(mathExp):
  tokenList = mathExp.split()
  parentStack = stack()
  expTree = BinaryTree(" ")
  push(parentStack, expTree)
  print(tokenList)
  currentTree = expTree
  for i in tokenList:
    if i == "(":
      print('if 1',i)
      currentTree.insertLeft(' ')
      push(parentStack, currentTree)
      currentTree = currentTree.getLeftChild()
    elif i not in ["+","-","*","/",")"]:
      print('if 2',i)
      currentTree.setRootVal(i)
      
    #   parent = pop(parentStack)
    #   currentTree = parent
    elif i in ["a","b","c",]:
      print('if 3',i)
      currentTree.setRootVal(i)
      currentTree.insertRight(' ')
      push(parentStack, currentTree)
      currentTree = currentTree.getRightChild()
    elif i == ")":
      currentTree = pop(parentStack)
    else:
      raise valueError
 
  return expTree

pt = buildParseTree("( d b d ) a ( f e b )")
print(pt.key)
print(f'Left Child of Node - {pt.key} is : {pt.getLeftChild().key}')
print(f'Left Child of Node - {pt.getLeftChild().key} is : {pt.getLeftChild().getLeftChild().key}')
print(f'Left Child of Node - {pt.getLeftChild().getLeftChild().key} is a leaf') #{pt.getLeftChild().getLeftChild().getLeftChild()}
print(f'Left Child of Node - {pt.getLeftChild().getLeftChild().key} is : {pt.getLeftChild().getLeftChild().getRightChild()}') #{pt.getLeftChild().getLeftChild().getLeftChild()}

