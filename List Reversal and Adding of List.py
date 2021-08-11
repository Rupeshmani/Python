n=int(input())
x=[]
z=[]
for i in range(n):
    i = list(map(int, input().split())) 
    x.extend(i)
print(x) 
y=x[::-1]
print(y)
z=list(map(sum,zip(x,y)))
print(z)