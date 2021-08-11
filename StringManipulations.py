def l1(s,l):
    
    l.append(s)
    return "".join(l)
word=input()
print("The input word is "+word)
u,m,l=[],[],[]
for i in range(len(word)):
    if i%4==0:
        k=l1(word[i],u)
    elif (i%2 ==0 and i%4 !=0) and (i) :
        p=l1(word[i],l)
    else: 
        v=l1(word[i],m)
        
print("The output word is "+k+v+p)