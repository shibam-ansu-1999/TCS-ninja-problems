n = int(input())
if n > 30:
  print("Invalid Input")
else: 
  if n == 1:
    nth = 1
  elif n == 2:
    nth = 2
  else:
    n1 = 1
    n2= 2
    for i in range(3,n+1):
      nth = n1 + n2
      n1= n2
      n2 = nth
  print(nth)
