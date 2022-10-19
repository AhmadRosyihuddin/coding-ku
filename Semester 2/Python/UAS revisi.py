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
#         self.y += data # Revisi kesalahan dicrement aslinya incremen
#     def moveBackward(self,data):
#         self.y -= data # Revisi Kesalahan Increment aslinya Dicremenyt
#     def distance(self,pixel2): # Revisi Menambahakan method distance karena kwmarin belum sempat bikin
#         x1 = self.x
#         y1 = self.y
#         x2 = pixel2.x
#         y2 = pixel2.y
#         return ((x1-x2)**2+(y1-y2)**2)**0.5
#     def display(self):
#         print (f'{self.nama} : ({float(self.x)},{float(self.y)})')

# pix1 = pixel("point 1",5,7)
# pix2 = pixel("point 2",6,5)
# pix1.display()
# pix2.display()
# pix1.moveBackward(5)
# pix1.display()
# jarak = pix1.distance(pix2)
# print('Jarak =',jarak)
# pix2.moveForward(3)
# pix2.display()
# pix2.moveLeft(1)
# pix2.display()
# pix2.moveRight(15)
# pix2.display()



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
#   print(tokenList)
  currentTree = expTree
  for i in tokenList:
    if i == "(":
      print('if 1',i)
      currentTree.insertLeft(' ')
      push(parentStack, currentTree)
      currentTree = currentTree.getLeftChild()
    elif i not in ["a","b","c",")"]:
      print('if 2',i)
      currentTree.setRootVal(i)
      parent = pop(parentStack)
      currentTree = parent
    elif i in ["a","b","c"]:
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

def ParsingTree(root):
    Node = root.getRootVal()
    left = root.getLeftChild()
    right = root.getRightChild()
    # print('Left :',left)
    # print('Right :',right)
    if left and right:
        # print(left.key)
        print(f'Left Child {Node} is : {left.key}')
        ParsingTree(left)
        
        # print('Isi :',right.key)
        print(f'Right Child {Node} is : {right.key}')
        ParsingTree(right)
    else:
        print(f'Node {Node} is a Leaf')

a = buildParseTree(" ( ( d b e ) a ( f c g ) ) ")
b = buildParseTree("( ( d c s ) a ( s b f ) )")
print('Root :',a.getRootVal())
ParsingTree(a)