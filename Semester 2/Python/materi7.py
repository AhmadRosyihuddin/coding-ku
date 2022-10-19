# class BilanganKomplek:
#     def __init__(self,a,b):
#         self.real = a
#         self.im = b

# data = BilanganKomplek(5,6)
# print(data.real)



# class BilanganKomplex2:
#     def __init__(self,a,b):
#         self.real=a
#         self.im=b
#     def display(self):
#         print("{} + {}i".format(self.real,self.im))
#     def jumlah(self,bil1,bil2):
#         self.real = bil1.real + bil2.real
#         self.im = bil1.im + bil2.im
        
#     def jumlah2(self,bil1,bil2):
#         self.real = bil1.real + bil2.real
#         self.im = bil1.im + bil2.im
#         return BilanganKomplex2(self.real,self.im)
    
# num1=BilanganKomplex2(4,2)
# num2=BilanganKomplex2(3,7)
# num1.display()
# num2.display()
# hasil = BilanganKomplex2(0,0)
# hasil.jumlah(num1,num2)
# hasil.display()

# hasil2 = num1.jumlah2(num1,num2)
# hasil2.display()
# num1.display()





# class BinaryTree:
#     def __init__(self, root):
#         self.key = root
#         self.leftChild = None
#         self.rightChild = None
#     def insertLeft(self, leftNode):
#         self.leftChild = leftNode
#     def insertLeft2(self, leftKey):
#         nodeChild = BinaryTree(leftKey)
#         self.leftChild = nodeChild



# tr = BinaryTree("Panas")
# #left1 = BinaryTree("Batuk")
# #tr.insertLeft(left1)
# tr.insertLeft2("Batuk")
# print(tr.key)
# print(tr.leftChild)
# temp=tr.leftChild
# print(temp.key)



# Latihan
# class BinaryTree:
#     def __init__(self,root):
#         self.key = root
#         self.leftChild = None
#         self.rightChild= None
        
#     def insertLeft(self,LeftNode):
#         head = BinaryTree(LeftNode)
#         self.leftChild = head
    
#     def insertRight(self,RightNode):
#         head = BinaryTree(RightNode)
#         self.rightChild = head
    
#     def getLeftChild(self):
#         return self.leftChild
    
#     def getRightChild(self):
#         return self.rightChild
    
#     def getRoot(self):
#         return self.key
    
#     def setRoot(self,obj):
#         self.key = obj

# def hitung(tree):
#     left = tree.getLeftChild().key
#     right = tree.getRightChild().key
#     opr = tree.key
#     print(opr)
#     print(left and right != None)
#     print(type(right) and type(left) == type(opr))
#     if (left and right != None) and (type(right) and type(left) != type(opr)):
#         print('as')
#         if opr == '+':
#             return (left+right)
#         elif opr == '-':
#             return (left-right)
#         elif opr == '*':
#             return (left*right)
#         elif opr == '/':
#             return (left/right)
#     else:
#         print('e')
#         hitung(opr)
    
    
    
    
    
    
# root = BinaryTree('*')
# root.insertRight('+')
# root.insertLeft(3)
# root.getRightChild().insertRight(2)
# root.getRightChild().insertLeft(4)
# print(hitung(root))



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
      currentTree.setRootVal(int(i))
      
      parent = pop(parentStack)
      currentTree = parent
    elif i in ["+","-","*","/"]:
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


pt = buildParseTree(" ( 3 + ( 4 * 5 ) ) ")
print(pt.getRootVal())
tmp = pt.getLeftChild()
#print(pt.getRightChild().key)
print(tmp.getRootVal())

if pt.getLeftChild():
  print("Tree")
  
  
#evaluasi persamaan matematika
import operator
def evaluate(parse_tree):
  opers = {
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv
    }
  left = parse_tree.getLeftChild()
  right = parse_tree.getRightChild()
  
  if left and right:
    fn = opers[parse_tree.key]
    return fn(evaluate(left),evaluate(right))
  else:
    return parse_tree.key
    
print(evaluate(pt))


# class BinaryTree:
#     def __init__(self, root):
#         self.key = root
#         self.leftChild = None
#         self.rightChild = None
#     def insertLeft(self, new_node):
#         if self.leftChild == None:           
#             self.leftChild = BinaryTree(new_node)         
#         else:
#             t = BinaryTree(new_node)
#             t.leftChild = self.leftChild
#             self.leftChild = t
           
#     def insertRight(self, new_node):
#         if self.rightChild == None:
#             self.rightChild = BinaryTree(new_node)            
#         else:
#             t = BinaryTree(new_node)
#             t.rightChild = self.rightChild
#             self.rightChild = t

#     def getRightChild(self):
#         return self.rightChild
#     def getLeftChild(self):
#         return self.leftChild
#     def setRootVal(self, obj):
#         self.key = obj
#     def getRootVal(self):
#         return self.key

# # data=BinaryTree('a')

# # data.insertLeft('b')
# # data.getLeftChild().insertRight('d')
# # # data.getLeftChild().insertLeft('d')
# # print("============")
# # print(data.key)
# # print(data.getLeftChild().key)
# # print(data.getLeftChild().getRightChild().key)
# # print("============")
# # data.insertRight('c')
# # data.getRightChild().insertLeft('e')
# # data.getRightChild().insertRight('f')

# # print(data.key)
# # print(data.getRightChild().key)
# # print(data.getRightChild().getLeftChild().key)
# # print(data.getRightChild().getRightChild().key)

# # baru
# # awal = BinaryTree('*')
# # awal.insertLeft('3')
# # awal.insertRight('5')
# # awal.getLeftChild().getRightChild()
# # awal.getRightChild().getLeftChild()

# # print(awal.key)
# # print(awal.getLeftChild().key)
# # print(awal.getLeftChild().getRightChild())
# # print(awal.getLeftChild().getRightChild())

# # print(awal.getRightChild().key)
# # print(awal.getRightChild().getLeftChild())
# # print(awal.getRightChild().getLeftChild())

# #baru2
# awal = BinaryTree('*')
# awal.insertLeft('3')
# awal.insertRight('+')
# awal.getRightChild().insertRight('2')
# awal.getRightChild().insertLeft('4')

# print(awal.key)
# print(awal.getLeftChild().key)
# print(awal.getRightChild().key)

# print(awal.getRightChild().getLeftChild().key)
# print(awal.getRightChild().getRightChild().key)

# def prosesHitung(tree):
#     left = tree.getLeftChild()
#     right = tree.getRightChild()
#     if left != None and right != None:
#         opr = tree.key
#         if opr == "+":
#             return prosesHitung(left) + prosesHitung(right)
#         elif opr == "-":
#             return prosesHitung(left) - prosesHitung(right)
#         elif opr == "*":
#             return prosesHitung(left) * prosesHitung(right)
#         else:
#             return prosesHitung(left) / prosesHitung(right)
#     else:
#         return int(tree.key)

# print(prosesHitung(awal))


# # baru
# tree1 = BinaryTree('Root')
# tree1.insertLeft('temp')
# tree2 = tree1

# print('tree 1 awal', tree1.key)
# print('tree 1 awal left chiild', tree1.getLeftChild().key)

# print('tree 2 awal', tree2.key)
# print('tree 2 awal left chiild', tree2.getLeftChild().key)



# print('tree1 update tree2',tree1.key)
# print('tree 1 awal left chiild', tree1.getLeftChild().key)

# while tree1!=None:
#     print(tree1.key)
#     tree = tree1.getLeftChild()