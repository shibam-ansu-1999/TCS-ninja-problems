s = input().split()
low=int(s[0])
up=int(s[1])
for i in range(low,up+1):
    if(up>=100):
        print("%03d" %i,end=' ')
    elif(up>=10):
        print("%02d" %i,end=' ')
    else:
        print(i,end=' ')
