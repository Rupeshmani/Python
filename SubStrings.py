l=input()
p=list(map(str,input().split()))
s=list(l)
count=0
for i in range(len(p)):
    if p[i] in l:
        count+=1
print(count)
