n = input()
odd = []
even = []
for i in range(len(n)):
  r = i + 1
  if r % 2 == 0:
    even.append(int(n[i]))
  else:
    odd.append(int(n[i]))
print(abs(sum(even)-sum(odd)))
