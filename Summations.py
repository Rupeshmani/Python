a=int(input())
b=int(input())
opr=input()
bynum=int(opr[1])
sum=0
for i in range(a,b+1):
   sum +=eval("%d %c %d"%(i,opr[0],bynum))
print(sum)