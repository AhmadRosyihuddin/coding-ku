#Nilai Awal
print("Nilai Awal")
string = 'data string'
ffloat = 2.3
integer = 3
booleann = True
print(string, type(string))
print(ffloat, type(ffloat))
print(integer, type(integer))
print(booleann,type(booleann))

#Casting ke str
print("=====Casting Ke String=====")
aStr = str(ffloat)
bStr = str(integer)
cStr = str(booleann)
dStr = str(string)
print(aStr, type(aStr))
print(bStr, type(bStr))
print(cStr, type(cStr))
print(dStr, type(dStr))

#Casting ke integer
print("=====Casting Ke Integer=====")
aInt = int(ffloat)
bInt = int(integer)
cInt = int(booleann)
#dInt = int(string) (Tidak Bisa)
print(aInt, type(aInt))
print(bInt, type(bInt))
print(cInt, type(cInt))
#print(dInt, type(dInt)) (Tidak Bisa)

#Casting ke Float
print("=====Casting Ke Float=====")
aFloat = float(ffloat)
bFloat = float(integer)
cFloat = float(booleann)
#dFloat =float(string) #(Tidak Bisa)
print(aFloat, type(aFloat))
print(bFloat, type(bFloat))
print(cFloat, type(cFloat))
#print(dFloat, type(dFloat)) #(Tidak Bisa)

#Casting  ke Boolean
print("=====Casting Ke Boolean=====")
aBool = bool(ffloat)
bBool = bool(integer)
cBool = bool(booleann)
dBool = bool(string)
print(aBool, type(aBool))
print(bBool, type(bBool))
print(cBool, type(cBool))
print(dBool, type(dBool))
