import m1StackModul as st

# Revers 

# def reverseWord(word):
#     data = st.stack()
#     hasil = ''
#     for i in word:
#         st.push(data,i)
#     while not st.isEmpty(data):
#         hasil += st.pop(data)
#     return hasil

# print(reverseWord('aku'))


#delimite

# def delimite(operasi):
#     data = st.stack()
#     for i in operasi:
#         if i == '(':
#             st.push(data,i)
#         elif i == ')':
#             if st.isEmpty(data):
#                 return 'Kelebihan Tututp Kurung'
#             else:
#                 st.pop(data)
#                 a = True
#     if not st.isEmpty(data):
#         a = False
#         return 'Kelebihan Buka Kurung'
#     return a

# print(delimite('2/3(3-4)'))


# Konversi Desimal Ke Binner

# def konversiBinner(desimal):
#     data = st.stack()
#     nilai = desimal
#     while nilai > 0:
#         st.push(data,nilai%2)
#         nilai //= 2
#     binner = ''
#     while not st.isEmpty(data):
#         binner += str(st.pop(data))
#     return binner

# print('Binner =',konversiBinner(11))


# Konversi Infix Ke Postfix

# def InfixToPostfix(infix):
#     prioritas = {'*' : 2, '/' : 2, '+' : 1, '-' : 1}
#     data = st.stack()
#     hasil = ''
#     for i in infix:
#         if i in prioritas.keys():
#             if st.isEmpty(data) or st.peek(data) in '([{' or prioritas[i] > prioritas[st.peek(data)]:
#                 st.push(data,i)
                
#             else:
#                 while not st.isEmpty(data) and st.peek(data) not in '([{' and prioritas[i] <= prioritas[st.peek(data)]:
#                     hasil += st.pop(data)
#                 st.push(data,i)
                
#         elif i in '([{':
#             st.push(data,i)
            
#         elif i in ')]}':
#             while not st.isEmpty(data) and st.peek(data) not in '([{':
#                 hasil += st.pop(data)
#             st.pop(data)
            
#         else:
#             hasil += i
#         print('Infix =',i)
#         print('stack =',data)
#         print('postfix =',hasil)
#         print()
        
#     while not st.isEmpty(data):
#         hasil += st.pop(data)
        
#     return hasil

# a = '(3-(7/9)*(6/8)+6)'
# b = '2/8*6(1-9/9*4)(2+6)'
# c = '3/7*3(2-9/9*4)+5-8'
# d = 'A+B+C*D'
# print('Infix =',d,'\nPostfix =',InfixToPostfix(d))


# def operasi(data1,operator,data2):
#     c = str(data2)+str(operator)+str(data1)
#     return eval(c)
    
    
# def Evalpostfix(postfix):
#     operator = ['*','/','-','+']
#     data = st.stack()
#     for i in postfix:
#         if i in operator:
#             total = operasi(st.pop(data),i,st.pop(data))
#             st.push(data,total)
#         else:
#             st.push(data,i)
#     return st.pop(data)

# print('Hasil =',Evalpostfix('61-'))

for i in range(0,10,2):
    print(i)