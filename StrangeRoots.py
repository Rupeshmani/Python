from math import*
a=int(input())
root=str(sqrt(a))
sq=str(a**2)
root=root[:5]
k=0
for i in root:
    for j in sq:
        if i==j:
            k+=1
if k>0:
    print("Strange roots")
else:
    print("Not Strange roots")