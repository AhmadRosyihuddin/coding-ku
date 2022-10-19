import modulstackk as st

def konversiBinner(desimal):
    data = st.stack()
    binner = ''
    nilai = desimal
    while nilai > 0:
        div = nilai%2
        st.push(data,div)
        print('{} Div 2 = {} sisa {} : push(stack,{})'.format(nilai,nilai//2,div,div))
        nilai //= 2
        for i in range(len(data)):
            print('|',data[(len(data)-1)-i],'|')
        print(' ...')
        
    while not st.isEmpty(data):
        binner += str(st.pop(data))
        
    return binner

binner = konversiBinner(25)
print('Biner =',binner)



def  ParenthesesCheck(operasi):
    kurung = {')':'(',']':'[','}':'{'}
    data = st.stack()
    for i in operasi:
        print('Baca "{}"'.format(i))
        print('Stack :')
        if i in kurung.values():
            st.push(data,i)
        elif i in kurung.keys():
            if st.isEmpty(data):
                return '"Kelebihan Tutup Kurung \'{}\'"'.format(i)
            else:
                if data[-1] != kurung[i]:
                    return '"\'{}\' tidak sejenis dengan \'{}\'"'.format(data[-1],i)
                else:
                    st.pop(data)
        for i in range(len(data)):
            print('| {} |'.format(data[(len(data)-1)-i]))
        print('....')
    if not st.isEmpty(data):
        return '"Kelebihan Buka Kurung \'{}\'"'.format(st.pop(data))
    return "'OK'"


matSTR = ParenthesesCheck('([4+5]*[2+8]}')
print(matSTR)