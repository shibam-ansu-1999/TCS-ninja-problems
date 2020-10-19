
print("Enter distances covered y racers in Marathon (Kilometers) please (press q to terminate):")
R = []
s = []
res = []
flag = 0
for i in range(10000):
    c = input()
    if c=="q":
        break
    else:
        R.append(float(c))
for i in R:
    if i < 0 :
        flag = 1
    elif i != 42.195:
        s.append(i)
for i in range(3):
    res.append(max(s))
    s.remove(max(s))

if flag == 0:
    print("Heighest Distance excluding Finishers")
    print(res)
else:
    print("Heighest Distance excluding Finishers")
    print("Invalid Input")

    

