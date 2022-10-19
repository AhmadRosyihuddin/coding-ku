# Fungsi tanpa parameter dan tanpa return
def contoh1():
    a = 'contoh'
    print(a)
contoh1()
print()

# Fungsi dengan parameter dan tanpa return
def contoh2(a):
    print(a*2)
contoh2(2)
print()

# Fungsi tanpa parameter dan dengan return
def contoh3(): #= 1
    return 1
print(contoh3())
print()

# Fungsi dengan parameter dan dengan return
def contoh4(a,b): # 
    v = a*b #= 8
    c = a+b #= 6
    return c
print(contoh4(4,2)+contoh4(2,2))


# data = [2,4,5,6,7]
# x = 5
# def displayData(data,x):
#     lst = []
#     for i in range(x):
#         lst.append(data[i])