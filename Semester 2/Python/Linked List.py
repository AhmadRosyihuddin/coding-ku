class Node:
    def _init_(self, data):
        self.data = data
        self.next= None
    def setNext(self, new_next):
        self.next = new_next
class LinkedList:
    def _init_(self):
        self.head = None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def display(self):
        curent = self.head
        while curent != None:
            print(curent.data)
            curent = curent.next
    def insertNext(self, item, position):
        curent = self.head
        while curent is not None:
            if curent.data == item:
                break
            curent = curent.next
        # mengecek apakah item yang dimasukkan ada didalam node atau tidak
        if curent is None:
            print('Lihat item ada didalam node atau tidak')
        else:
            newNode = Node(position)
            newNode.next = curent.next
            curent.next = newNode
    def insertPrevious(self, item , position):
        # mnegecek apakah head kosong atau tidak
        if self.head is None:
            print("List has no element")
            return
        if item == self.head.data:
            newNode = Node(position)
            newNode.next = self.head
            self.head = newNode
            return
        curent = self.head
        while curent.next is not None:
            if curent.next.data == item:
                break
            curent = curent.next
        if curent.next is None:
            print("item not in the list")
        else:
            newNode = Node(position)
            newNode.next = curent.next
            curent.next = newNode
mylist=LinkedList()
mylist.add(45)
mylist.add(34)
mylist.add(70)
mylist.add(84)
mylist.display()
mylist.insertNext(100, 70)
mylist.display()
mylist.insertPrevious(34, 100)
mylist.display()