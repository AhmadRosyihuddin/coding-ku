import turtle as t
t.speed(2)
def kotak(panjang,level):
    warna = ['blue','red','green','purple']
    i = 0
    jumlah = 0
    start = True
    if level >= 1:
        while start:
            print(level)
            t.forward(panjang)
            t.right(90)
            i += 1
            if i == 3:
                jumlah += 1
                i = 0
                t.forward(panjang)
                if jumlah == 4:
                    t.left(90)
                    t.forward(panjang/2)
                    t.left(90)
                    t.forward(panjang/2)
                    print('ewf')
                    t.left(180)
                    start = False
            kotak(panjang/2,level-1)
    else:
        while start:
            print(level)
            t.forward(panjang)
            t.right(90)
            i += 1
            if i == 3:
                jumlah += 1
                i = 0
                t.forward(panjang)
                if jumlah == 4:
                    t.left(90)
                    t.forward(panjang/2)
                    t.left(90)
                    t.forward(panjang/2)
                    print('ewf')
                    t.left(180)
                    start = False 
                    
            # elif a > 0:
            #     a +=1
            #     if a ==
        # t.begin_fill()
        # t.color('black',warna[level])
        # t.right(90)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.right(90)
        # t.forward(panjang)
        # t.end_fill()
#     else:
#         t.begin_fill()
#         t.color('black',warna[level])
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.forward(panjang)
#         t.right(90)
#         t.end_fill()
#         t.forward(panjang/2)
#         t.right(90)
#         t.forward(panjang/2)
#         t.right(180)
#         kotak(panjang/2,level-1)

# kotak(200,1)
# t.done()

def fractal(panjang,level):
    if level > 0 :
        t.forward(panjang/2)
        t.right(90)
        t.forward(panjang/2)
        t.right(90)
        t.forward(panjang/2)
        t.right(90)
        t.forward(panjang)
        # t.forward(panjang/2)
        t.right(90)
        fractal(panjang,level-1)
#         else:
#             fractal(my_pen,line/2,0,lvl-1)
# # main 
fractal(200,6)
t.done()