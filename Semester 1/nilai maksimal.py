a = [6,45,1,89,56,90,24,20,45,13,55,87,34,98,23,67,45,67]
b = 0
for i in range(len(a)):
    if a[b]>a[i]:
        b = b
    else:
        b = i    
print(a[b])