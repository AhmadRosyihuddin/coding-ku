# def maxNumber(x):
#     if len(x) == 1 :
#         return x[0]
#     else:
#         if x[len(x)-1] > x[len(x)-2]:
#             x = x[:len(x)-2]+x[len(x)-1:]
#             print('s',x)
#             return maxNumber(x)
#         else:
#             x = x[:len(x)-1]
#             print(x)
#             return maxNumber(x)
            
# data = [10,5,8,9,18,1,9,2]
# print('Bilangan Maksimal dari',data,'Adalah',maxNumber(data))



# def max(x):
#     if len(x)== 1:
#         return x[0]
#     else:
#         if x[0] > x[1]:
#             del(x[1])
#             return max(x)
#         else:
#             del(x[0])
#             return max(x)

# print(max([10,5,8,6,4,7,3,7,323,4]))


def tambah(x):
    if len(x) == 1:
        return int(x[0])
    else:
        return int(x[0]) + tambah(x[1:len(x)])

n = '1','2','3','4'
print(tambah(n))


# Ilustrasi
# def tambah(x = '1234'):
#     else:
#         return x[0] + tambah(x[1:len(x)]= '234')
#                         else:
#                             return x[0] + tambah(x[1:len(x)] = '34')
#                                         else:
#                                             return x[0] + tambah(x[1:len(x)] = '4')
#                                                 if len(x) == 1:
#                                                     return x[0]

a = '2','3','4'
#print(a[1])
print(len(a))