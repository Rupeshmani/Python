n=int(input())
l=[]
for i in range(n):
    i=list(map(int,input().split()))
    l.extend(i)
print(l)
max1=0
l.remove(max(l))
print(l)
print(max(l))
l.remove(min(l))
print(min(l))