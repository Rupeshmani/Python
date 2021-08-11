a=input()
l=len(a)
if l%2==0:
    b=a[:(l//2)]
    c=a[(l//2):]
    if b!=c:
        print("Prime ")
    else:
        print("Not Prime ")
else:
    b=a[:(l//2)+1]
    c=a[(l//2)+1:]
    if b!=c:
        print("Prime")
    else:
        print("Not Prime")