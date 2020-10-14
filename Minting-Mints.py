s = input().split()
#input seperated by space
m  = int(s[0])
n = int(s[1])
res = []
res.append(m)
for i in range(2,n+1):
  res.append(sum(res)-1)
print(sum(res))

