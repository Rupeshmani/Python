s = input()
one = 0
zero = 0
for i in s:
    if i=='1':
        one += 1
    else:
        zero += 1
if(one == 1 or zero == 1):
    print('yes')
else:
    print('no')