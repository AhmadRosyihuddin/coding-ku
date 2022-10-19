import m3DequesModul as dq

def Deques(data):
    deq = dq.createDeque()
    for i in data:
        dq.addFront(deq,i)
    hasil = 0
    for i in range(len(deq)//2):
        if dq.removeFront(deq) == dq.removeRear(deq):
            hasil += 1
    return hasil

print(Deques('hannah'))