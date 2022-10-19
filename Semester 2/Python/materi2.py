import m2QueueModul as q

# def ularNaga(data,hitungan):
#     que = q.createQueue()
#     for i in data:
#         q.enqueue(que,i)
#     print('Urutan Awal =',que)
#     n = hitungan
#     while q.size(que) > 1:
#         for i in range(n):
#             q.enqueue(que,q.dequeue(que))
#         q.dequeue(que)
#         if n%2 == 0:
#             n -= (n//3)-1
#         else:
#             n += 5
#         # print(que)
#     return que[0]

# data = ['mangga','apel','jeruk','anggur','malkisa','lemon','melon']
# print('Pemenang =',ularNaga(data,10))


def inputan_data(n):
    task = {}
    for i in range(n):
        a = input('Nama Task => ').upper()
        b = int(input('Jumlah Waktu => '))
        task[a] = [b,0]
    return task

def schedulling(limitTime,task):
    data = q.createQueue()
    for i in task.keys():
        q.enqueue(data,i)
    total = 0
    print(task)
    print('Data Awal =',data)

    while not q.isEmpty(data):
        temp = q.dequeue(data)
        pengurangan_W = task[temp][0] - limitTime
        print('{} = {} - {} = {}'.format(temp,task[temp][0],limitTime,pengurangan_W))
        
        if pengurangan_W > 0:
            q.enqueue(data,temp)
            total += limitTime
            task[temp][0] = pengurangan_W
        else:
            total += task[temp][0]
            task[temp][0] = 0
    
        task[temp][1] = total
        
        print(task)
        print(data)
        
    return task


x = inputan_data(3)
print(schedulling(3,x))

