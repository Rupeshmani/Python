a=int(input())
b=int(input())
r=0
while a>0:
    r=r*10+a%b
    a=a//b

print(str(r)[::-1])
