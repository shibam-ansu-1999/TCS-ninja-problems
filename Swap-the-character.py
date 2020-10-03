s1 = input().strip()
s2 = input().strip()
s3 = input()
arr = []
res =[]
res2 = []
for i in s1:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
    i="$"
  res.append(i)
sn1 = "".join(res)
for i in s2:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
    i = i
  else:
    i = "#"
  res2.append(i)
sn2 = "".join(res2)
sn = s3.upper()

arr.append(sn1)
arr.append(sn2)
arr.append(sn)

print("".join(arr))
  
