n=input()
a=int(n[:1])*10+int(n[len(n)-1:])
if int(n)%a==0:
    print("Gapful number")
else:
    print("Not a Gapful number")