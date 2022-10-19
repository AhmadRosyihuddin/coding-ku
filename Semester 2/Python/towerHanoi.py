def main(n, asal, tujuan, bantuan):
    a = [[asal],[i for i in range(1,n+1)]]
    b = [[tujuan], []]
    c = [[bantuan], []]
    print("pemindahan {} lempengan dari {} ke {} dengan menggunakan bantuan {}".format(len(a),"A","C","B"))
    print("A:")
    for i in a[1] :
        print("|",i,"|")
    print("B:\nC:")
    towerOfHanoi(n,a,b,c)

def towerOfHanoi(n, asal, tujuan, bantuan):
    if n == 1:
        print("lempengan - %d dari %s ke - %s"%(n, asal[0][0], tujuan[0][0]))
        tujuan[1].insert(0, asal[1].pop(0))
        print(asal[0][0],":")
        for i in asal[1] :
            print("|",i,"|")
        print(tujuan[0][0],":")
        for y in tujuan[1]:
            print("|",y,"|")
        print(bantuan[0][0],":")
        for z in bantuan[1] :
            print("|",z,"|")
    else :
        towerOfHanoi(n-1, asal, bantuan, tujuan)
        print("pindahkan lempengan #%d dari tower %s ke %s"%(n, asal[0][0], tujuan[0][0]))
        tujuan[1].insert(0, asal[1].pop(0))
        print(asal[0][0],":")
        for i in asal[1] :
            print("|",i,"|")
        print(tujuan[0][0],":")
        for y in tujuan[1]:
            print("|",y,"|")
        print(bantuan[0][0],":")
        for z in bantuan[1] :
            print("|",z,"|")
        towerOfHanoi(n-1, bantuan, tujuan, asal)

main(4,"A","C","B")