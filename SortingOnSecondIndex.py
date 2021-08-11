l=[["abc",23],["def",45],["ghi",61],["jkl",12],["xyz",45]]
k=[]
for i in range(len(l)):
    k.append(l[i][1])
k.sort()    
print(k)
p=k[-2]
for i in range(len(l)):
    if p==l[i][1]:
        print(l[i][0])