# class Node:
#     def __init__(self, init_data):
#         self.data=init_data
#         self.next=None
#     def getData(self):
#         return self.data
#     def getNext(self):
#         return self.next
#     def setData(self, newdata):
#         self.data=newdata
#     def setNext(self, new_next):
#         self.next=new_next
        
# class LinkedList:
#     def __init__(self):
#         self.head=None 
#     def isEmpty(self):
#         return self.head==None
#     def add(self, item):
#         temp=Node(item)
#         self.head=temp
#         temp.setNext(self.head)
#     def size(self):
#         curent=self.head
#         count=0
#         while curent!=None:
#             count=count+1
#             curent=curent.getNext()
#             return count
#     def search(self,item):
#         curent=self.head
#         found=False
#         while curent!=None and not found:
#             if curent.getData() ==item:
#                 found=True
#             else:
#                 curent=curent.getNext()
#                 return found
#     def display(self):
#         curent = self.head
#         while curent!=None:
#             print(curent.getData())
#             curent=curent.getNext()

# mylist = LinkedList()
# mylist.add(45)
# mylist.add(4)
# # print(mylist.head)
# mylist.display()




# class node1:
#     def __init__(self,item):
#         self.data = item
#         self.next = None
    
#     def getData(self):
#         return self.data
    
#     def getNext(self):
#         return self.next
    
# class link:
#     def __nit__(self):
#         self.head = None
        
#     def add(self,item):
#         new_node = node1(item)
#         self.head = new_node
#         new_node.next 
    
#     def display(self):
#         curent=self.head
#         while curent!=None:
#             print(curent.data)
#             curent=curent.next
    

# a = link()
# a.add(2)
# a.add(5)
# a.add(4)

# a.display()


        
# import modulqueue as q
# def inputan_data(n):
#     task = []
#     for i in range(n):
#        a = input('Nama Task : ').upper()
#        b = int(input('Waktu : '))
#        task.append([a,b])
#     return task

# def schedulling(limitTime,task):
#     data = q.createQueue()
#     for i in task:
#         q.enqueue(data,i)
#     print('Antrian Proses beserta Waktunya =',data)
#     cont = 1
    
    
#     while not q.isEmpty(data):
#         print('Iterasi Ke-',cont)
#         cont += 1
#         temp = q.dequeue(data)
#         indx = 0  
#         pengurangan_W = temp[1] - limitTime
#         if pengurangan_W > 0:
#             q.enqueue(data,temp) 
#             data[0][1] = pengurangan_W
#             print('Proses {} Sedang Di Proses, Sisa Waktu Proses {} = {}'.format(temp[0],temp[0],pengurangan_W))
#         else:
#             print('Proses {} Telah Selesai Di Proses'.format(temp[0]))

#         print(data)
#         print()
        
#     return data


# # x = inputan_data(3)
# print(schedulling(3,[['A',5],['B',4],['c',2]]))






# data = [13,3,2,5]
# for i in range(len(data)-1,0,-1):
#     print ("genap-ganjil :",i)
#     for y in range(0,i,2):
#         if data[y]>data[y+1]:
#             data[y],data[y+1]=data[y+1],data[y]
#         print(data)

# def selection_sort(data):
#     maksimal = data
#     minimal = data
#     for i in range(len(data)):
#         print('iterasi Ke-',i)
#         minidx = i
#         maxidx = i
#         for y in range(i,len(data)):
#             if data[minidx] > data[y]:
#                 minidx = y
#                 maxidx = minidx
#         print(maxidx,minidx)
#         minimal[minidx],minimal[i] = minimal[i],minimal[minidx]
#         maksimal[maxidx],maksimal[len(data)-1] = maksimal[len(data)-1],maksimal[maxidx]
#         print('Maksimal =',maksimal)
#         print('Minimal =',minimal)
    
#     return data
# selection_sort(data)





# from turtle import *
# color('black','yellow')
# begin_fill()
# posisi = pos()
# while posisi == pos():
#     posisi = (-100,-100)
#     up()
#     goto(-100,-100)
#     down()
#     forward(100)
#     left(70)
#     print('Posis :',pos())
#     print('Posisi :',posisi)
#     print('Absolut Posisi :',abs(pos()))
# end_fill()
# done()

# def tree(branch_len, t):
#     t.speed('slowest')
#     if branch_len>5:
#         t.forward(branch_len)
#         t.right(20)
#         tree(branch_len-15, t)
#         t.left(40)
#         tree(branch_len-15, t)
#         t.right(20)
#         t.backward(branch_len)
# def main():
#     my_win=turtle.Screen()
#     t=turtle.Turtle()
#     t.shape("turtle")
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(60, t)
#     my_win.exitonclick()

# main()

# my_turtle=turtle.Turtle()
# my_win=turtle.Screen()
# my_win.bgcolor('blue')
# my_win.title('Judul Turtle')
# def draw_spiral(my_turtle, line_len):
#     if line_len>0:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle, line_len-5)

# draw_spiral(my_turtle, 90)
# my_win.exitonclick()


# screen = Screen()
# screen.bgcolor('yellow')
# screen.title('Uji Coba Turtle')
# color('green')
# pensize(2)
# speed(0.6)
# y = 150
# x = -150
# up()
# goto(x,y)
# down()
# for j in range(4):
#     forward(300)
#     right(90)
# for i in range(12):
#     y -= 25
#     up()
#     goto(x,y)
#     print(y)
#     down()
#     forward(300)
# left(90)
# for z in range(11):
#     up()
#     x += 25
#     goto(x,y)
#     down()
#     forward(300)
#     write('ggh')
# done()


# import turtle
# def draw(points,t):
#     t.speed('slowest')
#     t.up()
#     t.goto(points[0][0],points[0][1])
#     t.down()
#     t.goto(points[1][0], points[1][1])
#     t.goto(points[2][0], points[2][1])
#     t.goto(points[3][0], points[3][1])
#     t.goto(points[0][0], points[0][1])

#     t.up()
#     t.goto((points[0][0]+points[1][0])//2, (points[0][1]+points[1][1])//2)
#     t.down()
#     t.goto((points[3][0]+points[2][0])//2, (points[3][1]+points[2][1])//2)

#     t.up()
#     t.goto((points[1][0]+points[2][0])//2, (points[1][1]+points[2][1])//2)
#     t.down()
#     t.goto((points[0][0]+points[3][0])//2, (points[0][1]+points[3][1])//2)

# def mid(p1,p2):
#     return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

# def fractal(points,branch_len,t):
#     draw(points,t)
#     t.speed("slowest")
#     if branch_len > 0:
#         fractal([points[0],mid(points[0], points[1]), mid(points[0],points[2]),mid(points[0],points[3])],branch_len-1,t)

# def main():
#     wn = turtle.Screen()
#     t = turtle.Turtle()
#     points = [[-40,40],[40,40],[40,-40],[-40,-40]]
#     fractal(points,2,t)
#     wn.exitonclick()

# main()


# def binSearch(array, element) :
#     mid = 0
#     start = 0
#     end = len(array)-1
#     step = 0
#     found = []
#     i = 0
#     while (start <= end):
#         cek = 0
#         step = step+1
#         mid = (start+end)//2
#         if element == array[mid]:
#             found.append(mid)
#             cek = 1
#             if element == array[mid+1]:
#                 start = mid + 1
#             elif element == array[mid-1]:
#                 end = mid -1
#             else :
#                 cek = 0
#         if cek == 0 :
#             if element < array[mid]:

#                     end = mid - 1
#             else:
#                 start = mid + 1
#         i += 1
#         print(start,end,mid)
#     if found == []:
#         return ["data tidak ada", i]
#     else :
#         return [found, i ]





# a = [1,1,5,5,5,5,5,5,5,5,8,9,10,12,26]
# [hasil, iterasi] = binSearch(a,5)
# print("Posisi data=",hasil)
# print("Jumlah iterasi=",iterasi)

