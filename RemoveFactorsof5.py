n=int(input())
l=[]
for i in range(n):
    i=list(map(int,input().split()))
    l.extend(i)
print(l)
for j in l:
    if j%5==0:
        l.remove(j)
print(l)