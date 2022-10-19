import modStack as st


def InfixToPostfix(infix):
    prioritas = {'*' : 2, '/' : 2, '+' : 1, '-' : 1}
    data = st.stack()
    hasil = ''
    cont = 0
    for i in infix:
        if i in prioritas.keys():
            if st.isEmpty(data) or st.peek(data) in '([{' or prioritas[i] > prioritas[st.peek(data)]:
                st.push(data,i)
                
            else:
                while not st.isEmpty(data) and st.peek(data) not in '([{' and prioritas[i] <= prioritas[st.peek(data)]:
                    hasil += st.pop(data)
                st.push(data,i)
                
        elif i in '([{':
            st.push(data,i)
            
        elif i in ')]}':
            while not st.isEmpty(data) and st.peek(data) not in '([{':
                hasil += st.pop(data)
            st.pop(data)
            
        else:
            hasil += i
        print('Read Token - {} : {}'.format(cont,i))
        print('stack =',data)
        print()
        cont += 1
        
    while not st.isEmpty(data):
        hasil += st.pop(data)
        
    return hasil

a = '(3-(7/9)*(6/8)+6)'
b = '2/8*6(1-9/9*4)(2+6)'
c = '3/7*3(2-9/9*4)+5-8'
d = '(A*(B+C))-D'
print('{} : {}'.format(a,InfixToPostfix(a)))




def Evalpostfix(postfix):
    operator = ['*','/','-','+']
    data = st.stack()
    for i in postfix.split():
        if i in operator:
            temp1 = float(st.pop(data))
            temp2 = float(st.pop(data))
            if i == '+':
                total = temp2 + temp1
            elif i == '-':
                total = temp2 - temp1
            elif i == '*':
                total = temp2 * temp1
            elif i == '/':
                total = temp2 / temp1
            st.push(data,total)
            print('{} {} {} = {}'.format(temp2,i,temp1,total))
        else:
            st.push(data,i)
    return st.pop(data)

print(Evalpostfix('2 3 4 * 10 / + 11 - 9 2 * +'))